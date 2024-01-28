import requests
from scrapper.headers import replicate_header
from scrapper.replicate import video

class zeroScope:
    def create_vid(prompt):
        return video.replicateAPI.create_video(prompt=prompt, model="anotherjesse/zeroscope-v2-xl", version="9f747673945c62801b13b84701c783929c0ee784e4748ec062204894dda1a351")
    
    def get_vid(id):
        return video.replicateAPI.get_video(id=id)
        
