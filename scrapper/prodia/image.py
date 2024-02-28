import requests
from scrapper.headers import prodia_headers

headers = prodia_headers

class prodiaAPI:
    def create_image(neg_prompt, prompt, model, steps, cfg, seed):
        
        json_data = {
            'new': 'true',
            'prompt': prompt,
            'model': model,
            'negative_prompt': neg_prompt,
            'steps': steps,
            'cfg': cfg,
            'seed': seed,
            'sampler': 'DPM++ 2M Karras',
            "width": '1080',
            "height": '720'
        }

        response = requests.get('https://api.prodia.com/generate', params=json_data, headers=headers)
        
        result = response.json()["job"]
        
        return result
    
    def get_image(id):

        response = requests.get(f'https://api.prodia.com/job/{id}', headers=headers)        
        result = response.json()
        
        return result
        



