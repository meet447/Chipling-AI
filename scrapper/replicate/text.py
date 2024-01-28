import requests
from scrapper.headers import replicate_header

class replicateAPI:
    def create_req(prompt, model, version):
        
        json_data = {
            'model': model,
            'version': version,
            'input': {
                'prompt': prompt,
            },
            'stream': True,
        }

        response = requests.post('https://homepage.replicate.com/api/prediction', headers=replicate_header, json=json_data)
        
        result = response.json()["id"]
        
        return result
    
    def get_res(id):
        
        params = {
            'id': id,
        }

        response = requests.get('https://homepage.replicate.com/api/prediction', params=params, headers=replicate_header)
        
        result = response.json()
        
        return result
        

