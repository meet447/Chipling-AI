from scrapper.prodia import image

class amiReal:
    def create_image(prompt, neg_prompt, seed, cfg, steps):
        return image.prodiaAPI.create_image(prompt=prompt, neg_prompt=neg_prompt, model="amIReal_V41.safetensors [0a8a2e61]",seed=seed, cfg=cfg, steps=steps)
    
    def get_image(id):
        return image.prodiaAPI.get_image(id=id)