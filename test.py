import requests

headers = {
    'authority': 'api.prodia.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ja;q=0.8',
    'origin': 'https://app.prodia.com',
    'referer': 'https://app.prodia.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

params = {
    'new': 'true',
    'prompt': 'pokemon',
    'model': 'absolutereality_v181.safetensors [3d9d4d2b]',
    'negative_prompt': '',
    'steps': '20',
    'cfg': '7',
    'seed': '3605272979',
    'sampler': 'DPM++ 2M Karras',
    'aspect_ratio': 'rectangle',
}

response = requests.get('https://api.prodia.com/generate', params=params, headers=headers)

print(response.json())