import requests
from scrapper.headers import replicate_header
from scrapper.replicate import image

class stablediff:
    def create_image(prompt):
        return image.replicateAPI.create_image(prompt=prompt, model="stability-ai/stable-diffusion", version="ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4")
    
    def get_image(id):
        return image.replicateAPI.get_image(id=id)
        
