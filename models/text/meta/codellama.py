import requests
from scrapper.headers import replicate_header
from scrapper.replicate import image, text

class codeLlama13B:
    def create_req(prompt):
        return text.replicateAPI.create_req(prompt=prompt,version="cc618fca92404570b9c10d1a4fb5321f4faff54a514189751ee8d6543db64c8f", model="meta/codellama-13b")
    
    def get_res(id):
        return text.replicateAPI.get_res(id=id)