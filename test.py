import requests

# Replace these values with your actual data
api_url = "http://127.0.0.1:5000/api/request"
api_key = "EDS6kNaBIPzLldH6qPmy"
prompt = "hello"
neg_prompt = "Your negative prompt here"
model = "meta/llama-2-70b-chat"
cfg = "7"
seed = "-1"
steps = "20"

# Prepare the request parameters
params = {
    "key": api_key,
    "prompt": prompt,
    "model": model,
}

# Make the POST request
response = requests.post(api_url, params=params)

# Print the response content
print(response.json())


