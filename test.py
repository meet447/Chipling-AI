import requests

#IMAGE:
#response.json()["id"]
#response.json()["status"]
#response.json()["output"]



url = "http://127.0.0.1:5000/api/response"

data = {
    "id":"hej7qkjbnetueg6jki57pwsmge"
}

response = requests.get(url, params=data)

print(response.json()["output"])