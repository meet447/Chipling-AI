import random
import string

def generate_api_key():
    key_length = 20
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(key_length))

