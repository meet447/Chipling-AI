from scrapper.replicate import video

class stablevideoDiff:
    def create_vid(prompt):
        return video.replicateAPI.genrate_video(prompt=prompt, model="stability-ai/stable-video-diffusion", version="3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438")
    
    def get_vid(id):
        return video.replicateAPI.get_video(id=id)
        
