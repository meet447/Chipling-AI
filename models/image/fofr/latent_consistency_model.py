import requests
from scrapper.headers import replicate_header
from scrapper.replicate import image

class latentConsistency:
    def create_image(prompt):
        return image.replicateAPI.create_image(prompt=prompt, model="fofr/latent-consistency-model", version="a83d4056c205f4f62ae2d19f73b04881db59ce8b81154d314dd34ab7babaa0f1")
    
    def get_image(id):
        return image.replicateAPI.get_image(id=id)