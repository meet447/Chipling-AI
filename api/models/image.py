from models.image.aiforever.kandinsky import kandisky
from models.image.stabilityai.sdxl import sdxl
from models.image.stabilityai.stablediffusion import stablediff
from models.image.fofr.latent_consistency_model import latentConsistency


class chiplingAPI:
    
    def auth(key):
        if key == "123":
            return True
        else:
            return False
        