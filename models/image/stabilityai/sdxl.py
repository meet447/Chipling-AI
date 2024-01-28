import requests
from scrapper.headers import replicate_header
from scrapper.replicate import image

class sdxl:
    def create_image(prompt):
        return image.replicateAPI.create_image(prompt=prompt, model="stability-ai/sdxl", version="39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b")
    
    def get_image(id):
        return image.replicateAPI.get_image(id=id)