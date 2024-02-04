from scrapper.prodia import image

class counterFeitv3:
    def create_image(prompt, neg_prompt, seed, cfg, steps):
        return image.prodiaAPI.create_image(prompt=prompt, neg_prompt=neg_prompt, model="Counterfeit_v30.safetensors [9e2a8f19]",seed=seed, cfg=cfg, steps=steps)
    
    def get_image(id):
        return image.prodiaAPI.get_image(id=id)