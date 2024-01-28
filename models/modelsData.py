#title, desc, github, runs, img
class Image:
    
    prompts = {
	 "colors": ['autochrome', 'cinecolour', 'colour', 'colourised', 'colour wheel',
			  'cyanopsia', 'faded', 'faded colours', 'high contrast', 'hue',
			  'low contrast', 'kinemacolour', 'kodachrome', 'monochromatic', 'monochrome',
			  'neon', 'neonpink', 'pigment', 'pure', 'sepia',
			  'spectrum', 'technicolor', 'tone', 'triadic colours', 'variegated',
			  'vibrant'],
	"lighting": ['artificial lighting', 'backlight', 'bright', 'bubble light', 'crepuscular rays',
			   'dark lighting', 'dynamic lighting', 'flickering light', 'floodlight', 'frontlight',
			   'moonlight', 'natural lighting', 'soft lighting', 'spotlight', 'strobe',
			   'strobe light', 'sunlight', 'vivid lighting'],
	"details": ['8k', 'concept art', 'highly detailed', 'hyperrealism',
		'hyperrealistic', 'insanely detailed', 'octane render', 'perfect composition',
		'photorealism', 'photorealistic', 'unreal engine'],
	"artists": ['anne stokes']
    }
    
    sdxl = {"author":"stability-ai", "model":"sdxl", "desc":"A text-to-image generative AI model that creates beautiful images","github":"https://github.com/replicate/cog-sdxl","runs":"33.4M", "img":"https://learn.thinkdiffusion.com/content/images/2023/07/00000-3097553845B.jpg"}
    
    stable_diff = {"author":"stability-ai", "model":"stable-diffusion", "desc":"A latent text-to-image diffusion model capable of generating photo-realistic images given any text input","github":"https://github.com/replicate/cog-stable-diffusion","runs":"106.5M", "img":"https://images.squarespace-cdn.com/content/v1/6213c340453c3f502425776e/465cccc6-2a57-48f1-8235-e646b2b39f5b/Stability+AI+Stable+Diffusion+Art.jpg"}
    
    kandinsky = {"author":"ai-forever", "model":"kandinsky-2.2", "desc":"multilingual text2image latent diffusion model","github":"https://github.com/chenxwh/Kandinsky-2/tree/v2.2","runs":"7.1M", "img":"https://d7hftxdivxxvm.cloudfront.net/?quality=80&resize_to=width&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FcecmBMX-MBCivPLk7J-Dpg%2Fnormalized.jpg&width=910"}
    

class Text:
    llama70 = {"author":"meta", "model":"llama-2-70b-chat", "desc":"A 70 billion parameter language model from Meta, fine tuned for chat completions","github":"https://github.com/a16z-infra/cog-llama-template","runs":"4.3M","img":"https://i0.wp.com/analyticsindiamag.com/wp-content/uploads/2023/07/LlaMA-2-Vs-GPT-4-Vs-Claude-2A-2.jpg?fit=1920%2C1080&ssl=1"}
    
    mistral7 = {"author":"mistralai", "model":"mistral-7b-instruct-v0.1", "desc":"An instruction-tuned 7 billion parameter language model from Mistral","github":"https://github.com/mistralai/mistral-src","runs":"4.3M","img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS72TV5uKAC9XWbLUbfX63UaY6tYqDkxh648w&usqp=CAU"}
    
class Video:
    
    prompts = {
	 "colors": ['autochrome', 'cinecolour', 'colour', 'colourised', 'colour wheel',
			  'cyanopsia', 'faded', 'faded colours', 'high contrast', 'hue',
			  'low contrast', 'kinemacolour', 'kodachrome', 'monochromatic', 'monochrome',
			  'neon', 'neonpink', 'pigment', 'pure', 'sepia',
			  'spectrum', 'technicolor', 'tone', 'triadic colours', 'variegated',
			  'vibrant'],
	"lighting": ['artificial lighting', 'backlight', 'bright', 'bubble light', 'crepuscular rays',
			   'dark lighting', 'dynamic lighting', 'flickering light', 'floodlight', 'frontlight',
			   'moonlight', 'natural lighting', 'soft lighting', 'spotlight', 'strobe',
			   'strobe light', 'sunlight', 'vivid lighting'],
	"details": ["(fractal art:1.3)","(1girl)","extreme detailed","top quality"],
	"artists": ['anne stokes']
    }
    
    animateDiff = {"author":"lucataco", "model":"animate-diff", "desc":"Animate Your Personalized Text-to-Image Diffusion Models","github":"https://github.com/lucataco/cog-animatediff","runs":"130.8K","img":"https://s13.gifyu.com/images/SCbiG.gif"}
    
    zeroScope = {"author":"anotherjesse", "model":"zeroscope-v2-xl", "desc":"Zeroscope V2 XL & 576w","github":"","runs":"192.5K","img":"https://im4.ezgif.com/tmp/ezgif-4-eef349e4fb.gif"}

    
class Website:
    trending_models = [Image.stable_diff, Text.mistral7, Image.kandinsky, Text.llama70]
    
    text_models = [Text.llama70, Text.mistral7]
    
    image_models = [Image.kandinsky, Image.sdxl, Image.stable_diff]
    
    video_models = [Video.animateDiff, Video.zeroScope]
