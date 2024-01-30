import requests
from scrapper.headers import replicate_header
from scrapper.prodia import image

class anythingv5:
    def create_image(prompt, neg_prompt, seed, cfg, steps):
        return image.prodiaAPI.create_image(prompt=prompt, neg_prompt=neg_prompt, model="anythingV5_PrtRE.safetensors [893e49b9]",seed=seed, cfg=cfg, steps=steps)
    
    def get_image(id):
        return image.prodiaAPI.get_image(id=id)