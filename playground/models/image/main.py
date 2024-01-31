from models.image.aiforever import kandinsky
from models.image.stabilityai import sdxl, stablediffusion
from models.image.fofr import latent_consistency_model
from models.image.anything import anythingv5
from models.image.lykon import dreamshaper8, absolutereality

from models.video.lucataco import animatediff
from models.video.anotherjesse import zeroscopev2xl
from models.video.stabilityai import stable_video_diffusion

from models.text.mistralai import mistral7
from models.text.meta import llama70, codellama

from flask import jsonify

def get_playground(prompt, neg_prompt=None, seed=None, cfg=None, steps=None):
    # Model 1
    model1_name = "stability-ai/sdxl"
    data1 = sdxl.sdxl.create_image(prompt)
    result1 = {"model": model1_name, "data": data1}

    # Model 2
    model2_name = "ai-forever/kandinsky-2.2"
    data2 = kandinsky.kandinsky.create_image(prompt)
    result2 = {"model": model2_name, "data": data2}

    # Model 3
    model3_name = "stability-ai/stable-diffusion"
    data3 = stablediffusion.stablediff.create_image(prompt)
    result3 = {"model": model3_name, "data": data3}

    # Model 4
    model4_name = "fofr/latent-consistency-model"
    data4 = latent_consistency_model.latentConsistency.create_image(prompt)
    result4 = {"model": model4_name, "data": data4}

    # Model 10
    model10_name = "anything/anythingv5"
    data10 = anythingv5.anythingv5.create_image(prompt=prompt, neg_prompt=neg_prompt, seed=seed, cfg=cfg, steps=steps)
    result10 = {"model": model10_name, "data": data10}

    # Model 11
    model11_name = "lykon/dreamshaper8"
    data11 = dreamshaper8.dreamshaper.create_image(prompt=prompt, neg_prompt=neg_prompt, seed=seed, cfg=cfg, steps=steps)
    result11 = {"model": model11_name, "data": data11}

    # Model 12
    model12_name = "lykon/absolutereality"
    data12 = absolutereality.absoluteReality.create_image(prompt=prompt, neg_prompt=neg_prompt, seed=seed, cfg=cfg, steps=steps)
    result12 = {"model": model12_name, "data": data12}


    # Return all results
    all_results = [result1, result2, result3, result4, result10, result11, result12]
    return jsonify(all_results)
 