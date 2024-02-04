import requests

cookies = {
    'pll_language': 'en',
}

headers = {
    'authority': 'chatgptdemo.ai',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ja;q=0.8',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryaAnWB9hBvpTGfnY6',
    'cookie': 'pll_language=en',
    'origin': 'https://chatgptdemo.ai',
    'referer': 'https://chatgptdemo.ai/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
}

files = {
    '_wpnonce': (None, '4c60c0a734'),
    'post_id': (None, '2943'),
    'url': (None, 'https://chatgptdemo.ai'),
    'action': (None, 'wpaicg_chat_shortcode_message'),
    'message': (None, 'whaaa really?\n'),
    'bot_id': (None, '0'),
    'chatbot_identity': (None, 'shortcode'),
    'wpaicg_chat_client_id': (None, 'PisLboWku9'),
    'wpaicg_chat_history': (None, '["Human: who are you?","AI: I am an AI assistant designed to help answer questions and provide information. How can I assist you today?","Human: when were u made?","AI: I am an AI language model developed by OpenAI. The specific version you are interacting with, GPT-3, was released in June 2020.","Human: whaaa really?"]'),
}

response = requests.post('https://chatgptdemo.ai/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, files=files)

print(response)