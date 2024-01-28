import requests
from scrapper.headers import replicate_header
from scrapper.replicate import video

class animateDiff:
    def create_vid(prompt):
        return video.replicateAPI.create_video(prompt=prompt, model="lucataco/animate-diff", version="beecf59c4aee8d81bf04f0381033dfa10dc16e845b4ae00d281e2fa377e48a9f")
    
    def get_vid(id):
        return video.replicateAPI.get_video(id=id)
        
