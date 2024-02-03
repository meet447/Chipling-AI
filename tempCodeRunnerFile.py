import requests

cookies = {
    'covers_ai_email': 'nkdwkwldnw@gmail.com',
    'covers_ai_artist_id': '7adb65b1-755e-4489-9037-c38fb1e4582f',
    'covers_ai_agrees_to_terms': 'true',
}

headers = {
    'authority': 'covers.ai',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ja;q=0.8',
    # 'cookie': 'covers_ai_email=nkdwkwldnw@gmail.com; covers_ai_artist_id=7adb65b1-755e-4489-9037-c38fb1e4582f; covers_ai_agrees_to_terms=true',
    'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22ai-song-generator%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
    'next-url': '/ai-song-generator',
    'referer': 'https://covers.ai/ai-song-generator',
    'rsc': '1',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

params = {
    '_rsc': '3kzeg',
}

response = requests.get('https://covers.ai/covers/puzJ9nnyujwoNuBd96l4', params=params, cookies=cookies, headers=headers)

print(response.text)