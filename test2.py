import requests
import time

def create_request(prompt):
    url = "http://127.0.0.1:5000/api/prediction"

    data = {
        "model": "stability-ai/sdxl",
        "prompt": prompt
    }

    response = requests.get(url, params=data)

    id = response.json()
    
    while True:
        result = get_response(id)

        if result["status"] == "succeeded":
            print(get_response(id)["output"])
            return get_response(id)["output"]

        time.sleep(3)

def get_response(id):
    url = "http://127.0.0.1:5000/api/response"
    
    data = {
        "id": id,
    }
    
    response = requests.get(url, params=data)
    
    return response.json()

