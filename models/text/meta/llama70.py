import requests
from scrapper.headers import replicate_header
from scrapper.replicate import image, text

class llama70:
    def create_req(prompt):
        return text.replicateAPI.create_req(prompt=prompt,version="02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3", model="meta/llama-2-70b-chat")
    
    def get_res(id):
        return text.replicateAPI.get_res(id=id)