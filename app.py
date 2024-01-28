from flask import Flask, request, jsonify, render_template
from models.image import sdxl, stablediffusion, kandinsky
from models.text import llama70, mistral7
from models.modelsData import *

app = Flask(__name__)

app.secret_key = "test123"


@app.route("/")
def index_page():
    trend = Website.trending_models
    return render_template("index.html", trending=trend)

@app.route("/api/prediction")
def api_page():
    prompt = request.args.get("prompt")
    model = request.args.get("model")
    
    #image models

    if model == "stability-ai/sdxl":
        data = sdxl.sdxl.create_image(prompt)
        return jsonify(data)

    elif model == "ai-forever/kandinsky-2.2":
        data = kandinsky.kandisky.create_image(prompt)
        return jsonify(data)

    elif model == "stability-ai/stable-diffusion":
        data = stablediffusion.stablediff.create_image(prompt)
        return jsonify(data)
    
    #text models
    
    elif model == "meta/llama-2-70b-chat":
        data  = llama70.llama70.create_req(prompt)
        return jsonify(data)
    
    elif model == "mistralai/mistral-7b-instruct-v0.1":
        data = mistral7.Mistral7b.create_req(prompt)
        return jsonify(data)
    
    else:
        return jsonify({"error": "error occurred"})
    
@app.route("/api/response")
def response_page():
    id = request.args.get("id")
    
    data = sdxl.sdxl.get_image(id)
    
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

    #text models 
     
    elif model == "llama-2-70b-chat" and author == "meta":
       return render_template("text.html", data=Text.llama70)
    elif model == "mistral-7b-instruct-v0.1" and author == "mistralai":
       return render_template("text.html", data=Text.mistral7)
   
    else:
        return "404"
   

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
