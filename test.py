import requests

url = "https://discord.com/api/webhooks/1203452921853775962/JvtQvRvNEaji8O4BoftsRxE-lUvYSdxWDw949yMMQh1pxl7RlLuvw6wV63sWOnIZYFWy"

# Your payload with an embedded message
payload = {
    "embeds": [
        {
            "title": "Example Embed",
            "description": "This is a test message with an embedded content.",
            "color": 16711680  # Hex color code (decimal representation)
        }
    ]
}

# Send a POST request to the webhook URL with the payload
response = requests.post(url, json=payload)

# Print the response status code and content
print(response.status_code, response.content)
