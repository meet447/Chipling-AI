import requests
from scrapper.headers import replicate_header
from scrapper.replicate import image, text

class Mistral7b:
    def create_req(prompt):
        return text.replicateAPI.create_req(prompt=prompt,version="83b6a56e7c828e667f21fd596c338fd4f0039b46bcfa18d973e8e70e455fda70", model="mistralai/mistral-7b-instruct-v0.1")
    
    def get_res(id):
        return text.replicateAPI.get_res(id=id)