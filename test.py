import requests

def createReq():
    url = "http://127.0.0.1:5000/api/request"

    params = {
        "key":"VuBNqJtRhbu5ot6CgZXh",
        "prompt":"",
        "neg_prompt":"",
        "model":"",
        "cfg":"",
        "seed":"",
        "step":"",  
    }

    response = requests.post(url=url, params=params)

    print(response.json())
    
    
createReq()