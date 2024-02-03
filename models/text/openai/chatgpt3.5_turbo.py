import requests

headers = {
    'authority': 'wewordle.org',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ja;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://chat-gpt.com',
    'referer': 'https://chat-gpt.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

json_data = {
    'messages': [
        {
            'content': 'whats 1 + 1 / 2',
            'role': 'assistant',
        }    
    ],
}

response1 = requests.post('https://wewordle.org/gptapi/v1/web/turbo', headers=headers, json=json_data)

print(response1.json()["message"]["content"])