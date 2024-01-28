import requests
from scrapper.headers import replicate_header
from scrapper.replicate import image

class kandisky:
    def create_image(prompt):
        return image.replicateAPI.create_image(prompt=prompt, model="ai-forever/kandinsky-2.2", version="ea1addaab376f4dc227f5368bbd8eff901820fd1cc14ed8cad63b29249e9d463")
    
    def get_image(id):
        return image.replicateAPI.get_image(id=id)
        
