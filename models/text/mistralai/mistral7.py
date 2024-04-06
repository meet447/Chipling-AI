import requests
from scrapper.headers import replicate_header
from scrapper.replicate import image, text

class Mistral7b:
    def create_req(prompt):
        return text.replicateAPI.create_req(prompt=prompt,version="dp-79052a3adbba8116ebc6697dcba67ad0d58feff23e7aeb2f103fc9aa545f9269", model="mistralai/mistral-7b-instruct-v0.2")
    
    def get_res(id):
        return text.replicateAPI.get_res(id=id)