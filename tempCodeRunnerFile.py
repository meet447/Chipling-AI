import requests

cookies = {
    'chat-ui': 'f8b0f2bd-d4f8-4497-812a-cb7a8f22234e',
}

headers = {
    'authority': 'huggingfaceh4-zephyr-chat.hf.space',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ja;q=0.8',
    'content-type': 'application/json',
    # 'cookie': 'chat-ui=f8b0f2bd-d4f8-4497-812a-cb7a8f22234e',
    'origin': 'https://huggingfaceh4-zephyr-chat.hf.space',
    'referer': 'https://huggingfaceh4-zephyr-chat.hf.space/conversation/65c370f8e6eb9a66585374b5',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

json_data = {
    'inputs': 'whats nigga ass gay',
    'is_retry': False,
    'is_continue': False,
    'web_search': False,
    'files': [],
}

response = requests.post(
    'https://huggingfaceh4-zephyr-chat.hf.space/conversation/65c370f8e6eb9a66585374b5',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.text)