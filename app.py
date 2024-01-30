from flask import Flask, request, jsonify, render_template, session, redirect
from pyrebase import pyrebase

from models.models_route import get_model
from models.image.stabilityai.sdxl import sdxl
from models.image.anything.anythingv5 import anythingv5
from models.modelsData import *
from config import firebaseConfig
from api.key import generate_api_key

#import ends here

app = Flask(__name__)

app.secret_key = "test123"

firebase = pyrebase.initialize_app(config=firebaseConfig)
auth = firebase.auth()
db = firebase.database()

#routes start here

@app.route("/")
def index_page():
    trend = Website.trending_models
    return render_template("index.html", trending=trend)

@app.route("/login", methods=["POST", "GET"])
def login():
    if 'user' in session:
        return redirect("/models")  # Redirect if the user is already logged in

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            
            print("succesfull")

            # Fetch additional user data from the database using UID
            user_data = db.child('users').child(user['localId']).get().val()
            
            user_data = db.child('users').child(user['localId']).get().val()

            if user_data:
                session["user"] = user_data.get('username', '')
                session["api_key"] = user_data.get('api_key', '')
                session["email"] = user_data.get('email', '')
                
                return redirect("/models")

            else:
                return "error"
            
        except Exception as e:
            return f"Error during registration: {e}"

    return render_template("login.html")

#USER ROUTES
@app.route("/register", methods=["POST", "GET"])
def register():
    if 'user' in session:
        return redirect("/models")  # Redirect if the user is already logged in

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')
        
        try:
            # Create user in Firebase
            user = auth.create_user_with_email_and_password(email, password)
            
            # Generate a random API key
            api_key = generate_api_key()

            # Store user details in the database (you need to adjust this based on your Firebase structure)
            user_data = {
                "email": email,
                "username": username,
                "api_key": api_key
            }
            # Example: Assuming you have a 'users' collection in Firestore
            db.child('users').child(user['localId']).set(user_data)

            # Store user information in session
            session["user"] = username
            
            session["email"] = email
            
            session["api_key"] = api_key
             
            return redirect("/models")
        except Exception as e:
            return f"Error during registration: {e}"

    return render_template("register.html")

@app.route('/logout')
def logout():
    try:
        session.pop('user')
        session.pop('email')
        session.pop('api_key')
    
        return redirect("/login")
    except:
        return redirect("/")

@app.route("/profile")
def profile(): 
    if 'user' in session:
        return render_template("profile.html")
    else:
        return render_template("register.html")

#MODEL ROUTES
@app.route("/models")
def models_page():
    return render_template("models.html", image = Website.image_models, text = Website.text_models, video = Website.video_models, new = Website.new_models)

@app.route("/api/prediction")
def api_page():
    prompt = request.args.get("prompt")
    neg_prompt = request.args.get("neg_prompt")
    model = request.args.get("model")
    cfg = request.args.get("cfg")
    seed = request.args.get("seed")
    steps = request.args.get("steps")
    
    print({prompt, neg_prompt, model, cfg, seed, steps})
    
    data = get_model(prompt=prompt, model=model, neg_prompt=neg_prompt, cfg=cfg, seed=seed, steps=steps)
    
    return data
     
@app.route("/api/response")
def response_page():
    id = request.args.get("id")
    
    try:
        data = sdxl.get_image(id)
        return data
    except:
        data = anythingv5.get_image(id)
        if data["status"] == "succeeded":
            return {"status":"succeeded", "output":f"https://images.prodia.xyz/{data['job']}.png"}
        else:
            return data

@app.route("/<author>/<model>")
def generateImage_page(author, model):
    
    #image models
    
    if model == "sdxl" and author == "stability-ai":
       return render_template("image.html", data=Image.sdxl, prompt=Image.prompts)
    elif model == "stable-diffusion" and author == "stability-ai":
       return render_template("image.html", data=Image.stable_diff, prompt=Image.prompts)
    elif model == "kandinsky-2.2" and author == "ai-forever":
       return render_template("image.html", data=Image.kandinsky, prompt=Image.prompts)
    elif model == "latent-consistency-model" and author == "fofr":
       return render_template("image.html", data=Image.latentConsistency, prompt=Image.prompts)
    elif model == "anythingv5" and author == "anything":
       return render_template("image.html", data=Image.anythingv5, prompt=Image.prompts)

    #text models 
     
    elif model == "llama-2-70b-chat" and author == "meta":
       return render_template("text.html", data=Text.llama70)
    elif model == "mistral-7b-instruct-v0.1" and author == "mistralai":
       return render_template("text.html", data=Text.mistral7)
    elif model == "codellama-13b" and author == "meta":
       return render_template("text.html", data=Text.codellama13b)
   
    #video models
    
    elif model == "animate-diff" and author == "lucataco":
       return render_template("video.html", data=Video.animateDiff, prompt=Video.prompts)
    elif model == "zeroscope-v2-xl" and author == "anotherjesse":
       return render_template("video.html", data=Video.zeroScope, prompt=Video.prompts)

   
    else:
        return "404"
   
#API ROUTES START HERE
def check_key(api_key_to_check):
    data = db.child('users').get().val()

    print(data)  # Optional: Print the data for debugging purposes

    # Check if the provided API key exists in any of the user entries
    for user_id, user_data in data.items():
        if 'api_key' in user_data and user_data['api_key'] == api_key_to_check:
            return True
    
    return False

@app.route("/api/request")
def request_api():
    prompt = request.args.get("prompt")
    model = request.args.get("model")
    key = request.args.get("key")
    
    #image models
    
    if check_key(key):
        get_model(prompt=prompt, model=model)
    else:
        return jsonify({"error": "invalid api key"})
