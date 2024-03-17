from flask import Flask, request, jsonify, render_template, session, redirect, send_from_directory
from pyrebase import pyrebase
import asyncio, datetime,requests

from models.models_route import get_model
from models.image.stabilityai.sdxl import sdxl
from models.image.anything.anythingv5 import anythingv5
from models.modelsData import *
from config import firebaseConfig
from api.key import generate_api_key

#import ends here

app = Flask(__name__)

app.secret_key = "sessionnew1111"

app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=5)

#firebase initialise

firebase = pyrebase.initialize_app(config=firebaseConfig)
auth = firebase.auth()
db = firebase.database()

#routes start here

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(days=5)

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
                return "error while creating your session please try again later"
            
        except Exception as e:
            error_message = str(e)  # Convert the exception to a string
            if "TOO_MANY_ATTEMPTS_TRY_LATER" in error_message:
                issue = "Your account has been temporarily restricted Due to too many login attempts please try again later!."
            else:
                issue = "Invalid login credentials."
            return render_template("login.html", issue=issue)


    return render_template("login.html", issue="")

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
        api_key = session["api_key"]
        data = db.child('profile').child(api_key).get().val()
        if data == None:
            data == ""
        return render_template("profile.html", data=data)
    else:
        return render_template("register.html")

#MODEL ROUTES
@app.route("/models")
def models_page():
    return render_template("models.html", image = Website.image_models, text = Website.text_models, video = Website.video_models, new = Website.new_models, trend=Website.trending_models, anime=Website.anime_models, real=Website.realistic_models, semi=Website.semi_real_models)

@app.route("/search")
def search_page():
    query = request.args.get('query', '')
    search_data = Website.text_models + Website.image_models + Website.video_models
    matching_models = [model for model in search_data if query.lower() in model["desc"].lower()]

    if matching_models:
        response = {"status": "found", "results": matching_models}
    else:
        response = {"status": "not found"}

    return render_template("search.html", data=response)

@app.route("/api/prediction")
async def api_page():
    prompt = request.args.get("prompt")
    neg_prompt = request.args.get("neg_prompt")
    model = request.args.get("model")
    cfg = request.args.get("cfg")
    seed = request.args.get("seed")
    steps = request.args.get("steps")
    
    url = "https://discord.com/api/webhooks/1203452921853775962/JvtQvRvNEaji8O4BoftsRxE-lUvYSdxWDw949yMMQh1pxl7RlLuvw6wV63sWOnIZYFWy"
    payload = {
    "embeds": [
        {
            "title": "Prediction Request",
            "description": f"Prompt: {prompt}\nNegative Prompt: {neg_prompt} \nModel: {model}",
            "color": 16711680  # Hex color code (decimal representation)
        }
        ]
    }

    # Send a POST request to the webhook URL with the payload
    response = requests.post(url, json=payload)
    
    print(response)
        
    data = await handle_async_task(prompt, model, neg_prompt, cfg, seed, steps)
    
    return data

async def handle_async_task(prompt, model, neg_prompt, cfg, seed, steps):
    await asyncio.sleep(2)
    data = get_model(prompt=prompt, model=model, neg_prompt=neg_prompt, cfg=cfg, seed=seed, steps=steps)
    return data
  
from flask import request
import requests

@app.route("/api/response")
def response_page():
    id = request.args.get("id")
    
    try:
        data = sdxl.get_image(id)
        return data
    
    except:
        data = anythingv5.get_image(id)
        if data["status"] == "succeeded":
            image_url = f"https://images.prodia.xyz/{data['job']}.png"
            url = "https://discord.com/api/webhooks/1218812046758514718/C8w7JvFjOiLKe2VEKQqQg3QVSDJNdA1JouaDWTt3LH-CUoAYf80dgGyaD3p2cME0xlgN"
            payload = {
                "embeds": [
                    {
                        "title": "Prediction Response",
                        "color": 16711680,  # Hex color code (decimal representation)
                        "image": {"url": image_url}  # Image URL
                    }
                ]
            }

            # Send a POST request to the webhook URL with the payload
            response = requests.post(url, json=payload)
            
            print(response)
            
            return {"status": "succeeded", "output": image_url}
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
    elif model == "dreamshaper8" and author == "lykon":
       return render_template("image.html", data=Image.dreamshaper8, prompt=Image.prompts)
    elif model == "absolutereality" and author == "lykon":
       return render_template("image.html", data=Image.absoluteReality, prompt=Image.prompts)
    elif model == "counterfeitv3" and author == "rqdwdw":
        return render_template("image.html", data=Image.counterfeitv3, prompt=Image.prompts)
    elif model == "am-i-real" and author == "lostdog":
        return render_template("image.html", data=Image.am_i_real, prompt=Image.prompts)
    elif model == "guofeng3" and author == "wrs111":
        return render_template("image.html", data=Image.guofeng3, prompt=Image.prompts)
    elif model == "juggernaut_aftermath" and author == "kandooai":
        return render_template("image.html", data=Image.juggernaut_aftermath, prompt=Image.prompts)
    elif model == "toonyou6" and author == "bradcatt":
        return render_template("image.html", data=Image.toonyou6, prompt=Image.prompts)
    elif model == "openjourneyv4" and author == "prompthero":
        return render_template("image.html", data=Image.openjourneyv4, prompt=Image.prompts)
    elif model == "pastel_mix" and author == "pastel":
        return render_template("image.html", data=Image.pastel_mix, prompt=Image.prompts)
    
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
    elif model == "stable-video-diffusion" and author == "stability-ai":
       return render_template("video.html", data=Video.stablevidDiff, prompt="")
    else:
        return "404" + model + author
   
#API ROUTES START HERE
def check_key(api_key_to_check):
    data = db.child('users').get().val()

    if data is not None:
        for user_node in data.values():
            if 'api_key' in user_node and user_node['api_key'] == api_key_to_check:
                print("Key found")
                return True
        print("Key not found")
    else:
        print("No data found in the 'users' node")

    return False


@app.route("/api/request", methods=["POST"])
async def request_api():
    key = request.args.get("key")
    print(key)
    
    prompt = request.args.get("prompt")
    if prompt == None or "":
        return jsonify({"error": "please enter prompt"})
        
    neg_prompt = request.args.get("neg_prompt")
    if neg_prompt == None:
        neg_prompt == ""

    model = request.args.get("model")
    if model == None or "":
        return jsonify({"error": "please enter a proper model"})
    
    cfg = request.args.get("cfg")
    if cfg == None:
        cfg == "7"
        
    seed = request.args.get("seed")
    if seed == None:
        seed == "-1"
        
    steps = request.args.get("steps")
    if steps == None:
        steps == "20"
        
    chk = check_key(key)
    print(chk)
        
    if check_key(key):
        data = await handle_async_task(prompt, model, neg_prompt, cfg, seed, steps)
        return data
    else:
        return jsonify({"error": "invalid api key"})

#User uploads

@app.route("/uploads", methods=["GET"])
def uploads():
    
    print("recived request")
    
    print(request.args)
    
    image = request.args.get("image")

    prompt = request.args.get("prompt")

    neg_prompt = request.args.get("neg_prompt")

    cfg = request.args.get("cfg")

    steps = request.args.get("steps")

    seed = request.args.get("seed")

    username = session["user"]
    email = session["email"]

    model = request.args.get("model")
    
    user_data = {
                "image":image,
                "email": email,
                "user": username,
                "prompt":prompt,
                "neg_prompt":neg_prompt,
                "cfg":cfg,
                "steps":steps,
                "seed":seed,
                "model":model,
            }
        
    key = generate_api_key()
        
    db.child('uploads').child(key).set(user_data)
    
    print("upload sucessfull")
    
    return jsonify("succesfull")


@app.route("/uploads_profile", methods=["GET"])
def uploads_private():
            
    image = request.args.get("image")

    prompt = request.args.get("prompt")

    neg_prompt = request.args.get("neg_prompt")

    cfg = request.args.get("cfg")

    steps = request.args.get("steps")

    seed = request.args.get("seed")

    username = session["user"]
    
    email = session["email"]

    model = request.args.get("model")
        
    api_key = session["api_key"]

    user_data = {
                "image":image,
                "email": email,
                "user": username,
                "prompt":prompt,
                "neg_prompt":neg_prompt,
                "cfg":cfg,
                "steps":steps,
                "seed":seed,
                "model":model,
            }
        
    key = generate_api_key()
        
    db.child('profile').child(api_key).child(key).set(user_data)
    
    print("upload sucessfull")
    
    return jsonify("succesfull")

@app.route("/gallery")
def gallery_page():
                  
    data = db.child('uploads').get().val()

    return render_template("gallery.html", data=data)

@app.route("/docs")
def docs_page():
    return "Hold Tight We are getting it done"

#Documentation
@app.route("/docs/<user>/<article>")
def docs_route(user, article):
    url = f"https://blog-chipling.onrender.com/{user}/{article}"
    response = requests.get(url)
    data = response.text
    return render_template("docs.html", data=data)

@app.route("/api")
def api_i():
    return redirect("/docs/chipling/api")

@app.route("/about")
def about_page():
    return render_template("extra/about.html")

@app.route("/privacy-policy")
def privacy_page():
    return render_template("extra/privacy.html")

@app.route("/models/<query>")
def expmodels_page(query):
    if query == "image":
        data = Website.image_models
        return render_template("models/base.html", data=data)
    elif query == "text":
        data = Website.text_models
        return render_template("models/base.html", data=data)
    elif query == "video":
        data = Website.video_models
        return render_template("models/base.html", data=data)
    else:
        return "page not found"

@app.route("/playground")
def playground_page():
    return render_template("playground.html")

@app.route("/docs/changelog")
def changelog_page():
    return render_template("extra/changelog.html")

@app.route("/test")
def test():
    return render_template("test.html", image = Website.image_models, text = Website.text_models, video = Website.video_models, new = Website.new_models, trend=Website.trending_models)

@app.route("/sitemap")
def static_from_root():
    response = send_from_directory(app.static_folder, "sitemap.xml")
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route("/ads.txt")
def static_from_ads():
    response = send_from_directory(app.static_folder, "ads.txt")
    return response
