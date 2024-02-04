from scrapper.prodia import image

class juggernautAftermath:
    def create_image(prompt, neg_prompt, seed, cfg, steps):
        return image.prodiaAPI.create_image(prompt=prompt, neg_prompt=neg_prompt, model="juggernaut_aftermath.safetensors [5e20c455]",seed=seed, cfg=cfg, steps=steps)
    
    def get_image(id):
        return image.prodiaAPI.get_image(id=id)