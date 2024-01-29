from models.image.aiforever import kandinsky
from models.image.stabilityai import sdxl, stablediffusion
from models.image.fofr import latent_consistency_model

from models.video.lucataco import animatediff
from models.video.anotherjesse import zeroscopev2xl

from models.text.mistralai import mistral7
from models.text.meta import llama70

from flask import jsonify

def get_model(prompt, model):
    
    #test model
    
    if model == "test":
        return jsonify({"response":"hello from chipling!"})
    
    #image models
    
    elif model == "stability-ai/sdxl":
        data = sdxl.sdxl.create_image(prompt)
        return jsonify(data)

    elif model == "ai-forever/kandinsky-2.2":
        data = kandinsky.kandisky.create_image(prompt)
        return jsonify(data)

    elif model == "stability-ai/stable-diffusion":
        data = stablediffusion.stablediff.create_image(prompt)
        return jsonify(data)
    
    elif model == "fofr/latent-consistency-model":
        data = latent_consistency_model.latentConsistency.create_image(prompt)
        return jsonify(data)    
    
    #text models
    
    elif model == "meta/llama-2-70b-chat":
        data  = llama70.llama70.create_req(prompt)
        return jsonify(data)
    
    elif model == "mistralai/mistral-7b-instruct-v0.1":
        data = mistral7.Mistral7b.create_req(prompt)
        return jsonify(data)
    
    #video models
    elif model == "lucataco/animate-diff":
        data = animatediff.animateDiff.create_vid(prompt)
        return jsonify(data)
    
    elif model == "anotherjesse/zeroscope-v2-xl":
        data = zeroscopev2xl.zeroScope.create_vid(prompt)
        return jsonify(data)
    
    else:
        return jsonify({"error": "error occurred"})