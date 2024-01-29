import requests
from scrapper.headers import prodia_headers

headers = prodia_headers

class prodiaAPI:
    def create_image(neg_prompt, prompt, model):
        
        json_data = {
            'new': 'true',
            'prompt': prompt,
            'model': model,
            'negative_prompt': neg_prompt,
            'steps': '20',
            'cfg': '7',
            'seed': '3605272979',
            'sampler': 'DPM++ 2M Karras',
            'aspect_ratio': 'landscape',
        }

        response = requests.get('https://api.prodia.com/generate', params=json_data, headers=headers)
        
        result = response.json()["job"]
        
        return result
    
    def get_image(id):

        response = requests.get(f'https://api.prodia.com/job/{id}', headers=headers)        
        result = response.json()
        
        return result
        



