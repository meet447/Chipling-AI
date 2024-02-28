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
    
    sdxl = {"author":"stability-ai", "model":"sdxl", "desc":"sdxl, SDXL is A text-to-image generative AI model that creates beautiful images","github":"https://github.com/replicate/cog-sdxl","runs":"33.4M", "img":"https://learn.thinkdiffusion.com/content/images/2023/07/00000-3097553845B.jpg","type":"image"}
    
    stable_diff = {"author":"stability-ai", "model":"stable-diffusion", "desc":"stable-diffusion is A latent text-to-image diffusion model capable of generating photo-realistic images given any text input","github":"https://github.com/replicate/cog-stable-diffusion","runs":"106.5M", "img":"https://images.squarespace-cdn.com/content/v1/6213c340453c3f502425776e/465cccc6-2a57-48f1-8235-e646b2b39f5b/Stability+AI+Stable+Diffusion+Art.jpg","type":"image"}
    
    kandinsky = {"author":"ai-forever", "model":"kandinsky-2.2", "desc":"kandinsky-2.2 is a multilingual text2image latent diffusion model","github":"https://github.com/chenxwh/Kandinsky-2/tree/v2.2","runs":"7.1M", "img":"https://d7hftxdivxxvm.cloudfront.net/?quality=80&resize_to=width&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FcecmBMX-MBCivPLk7J-Dpg%2Fnormalized.jpg&width=910","type":"image"}
    
    latentConsistency = {"author":"fofr", "model":"latent-consistency-model", "desc":"latent-consistency-model is a Super-fast, 0.6s per image. LCM with img2img, large batching and canny controlnet","github":"https://github.com/fofr/cog-lcm","runs":"357K","img":"https://latent-consistency-models.github.io/static/images/4Step_Image/dreamer_365_sample_1.png","type":"image"}
    
    anythingv5 = {"author":"anything", "model":"anythingv5", "desc":"Anything V5 is a popular choice among users for generating high-quality images from text prompts.","runs":"357K","img":"https://preview.redd.it/anything-v5-is-out-on-civitai-the-real-one-v0-1pawu0cpthqa1.png?width=1216&format=png&auto=webp&s=596f50ed2a102c2bb45a71d82787e63e0e427741", "neg":"True","type":"image"}
    
    dreamshaper8 = {"author":"lykon", "model":"dreamshaper8", "desc":"Dreamshaper is one of the best models trained for image genration.","runs":"357K","img":"https://assets.st-note.com/production/uploads/images/113620660/rectangle_large_type_2_1787502e90ce95b07850bb502cbbffca.png?width=800", "neg":"True","type":"image"}

    absoluteReality = {"author":"lykon", "model":"absolutereality", "desc":"Create Realistic Art with absolute Reality","runs":"-", "img":"https://ts2.pl/wp-content/uploads/2023/07/mfrack_realistic_photo_of_future_AI_10d24595-30f7-4765-af70-d9f9e8068a6a-1024x574.jpeg","neg":"True","type":"image"}
    
    counterfeitv3 = {"author":"rqdwdw", "model":"counterfeitv3", "desc":"Create Anime style Art with counter feit","runs":"-", "img":"https://assets-global.website-files.com/624ac40503a527cf47af4192/64ad98a93748b1dd485f971d_003.jpeg","neg":"True","type":"image"}
    
    am_i_real = {"author":"lostdog", "model":"am-i-real", "desc":"am i real can be used to Create Realistic style Art with am i real model","runs":"-", "img":"https://preview.redd.it/amireal-v1-out-now-v0-o6fvwmczv0wa1.png?width=640&crop=smart&auto=webp&s=56b17186225443a7e8d0cc324f87f0f06394c159","neg":"True","type":"image"}
    
    guofeng3 = {"author":"wrs111", "model":"guofeng3", "desc":"Create Chinese Style Model with guofeng3","runs":"-", "img":"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d3315e02-7c0f-420e-911f-abd53a0ebb28/original=true/tmp9d4z8vav.jpeg","neg":"True","type":"image"}
    
    juggernaut_aftermath = {"author":"kandooai", "model":"juggernaut_aftermath", "desc":"juggernaut_aftermath is one of the best models out there to create realistic images","runs":"-", "img":"https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d4fffe64-3265-4458-9427-0342411319e1/width=450/00072-3633275756.jpeg","neg":"True","type":"image"}
    
    toonyou6 = {"author":"bradcatt", "model":"toonyou6", "desc":"toonyou, toon you by bradcatt is a checkpoint used to create images in toons style","runs":"-", "img":"https://wiki.monai.art/toonyou/(old_man_1.2)_c_8790a.jpg","neg":"True"}
    
    openjourneyv4 = {"author":"prompthero", "model":"openjourneyv4", "desc":"open journey v4, Openjourney  is a  s a custom text-to-image model that generates AI art images in the style of Midjourney. It's a fine-tune of Stable Diffusion","runs":"-", "img":"https://prompthero.s3.amazonaws.com/og/openjourney-og-image.jpg","neg":"True","type":"image"}
    
    pastel_mix= {"author":"pastel", "model":"pastel_mix", "desc":"Pastel mix is a custom text-to-image model that generates AI art images in the style of Patel. It's a fine-tune of Stable Diffusion for anime genration","runs":"-", "img":"https://image.stablediffusionapi.com/?quality=45&Image=https://cdn.stablediffusionapi.com/generations/4c719b17-4325-45c9-b09d-6241ab44e25b-0.png","neg":"True","type":"image"}

    
class Text:
    llama70 = {"author":"meta", "model":"llama-2-70b-chat", "desc":"llama 70 b is A 70 billion parameter language model from Meta, fine tuned for chat completions","github":"https://github.com/a16z-infra/cog-llama-template","runs":"4.3M","img":"https://i0.wp.com/analyticsindiamag.com/wp-content/uploads/2023/07/LlaMA-2-Vs-GPT-4-Vs-Claude-2A-2.jpg?fit=1920%2C1080&ssl=1","type":"text"}
    
    mistral7 = {"author":"mistralai", "model":"mistral-7b-instruct-v0.1", "desc":"mistral is An instruction-tuned 7 billion parameter language model from Mistral","github":"https://github.com/mistralai/mistral-src","runs":"4.3M","img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS72TV5uKAC9XWbLUbfX63UaY6tYqDkxh648w&usqp=CAU","type":"text"}
    
    codellama13b = {"author":"meta", "model":"codellama-13b", "desc":"Code llama is A 13 billion parameter Llama tuned for code completion","github":"https://github.com/facebookresearch/codellama","runs":"93K","img":"https://venturebeat.com/wp-content/uploads/2023/08/cfr0z3n_vector_art_synthwave_llama_typing_on_a_laptop_ee7e1f3d-7509-4cc2-9a46-15841f4da40b.png?fit=1456%2C816&strip=all","type":"text"}

 
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
    
    animateDiff = {"author":"lucataco", "model":"animate-diff", "desc":"Animate Your Personalized Text-to-Image Diffusion Models","github":"https://github.com/lucataco/cog-animatediff","runs":"130.8K","img":"https://s13.gifyu.com/images/SCbiG.gif","type":"video"}
    
    zeroScope = {"author":"anotherjesse", "model":"zeroscope-v2-xl", "desc":"Zeroscope V2 XL & 576w","github":"","runs":"192.5K","img":"https://assets-global.website-files.com/624ac40503a527cf47af4192/64a6ab8e435a254313318bfd_videoexamples.gif","type":"video"}
    
    stablevidDiff = {"author":"stability-ai", "model":"stable-video-diffusion", "desc":"Animate a Image into Video","github":"","runs":"192.5K","img":"https://tjzk.replicate.delivery/models_models_cover_image/923695cb-4735-439c-868b-79620bcacb32/svd.gif", "no_prompt":"True","type":"video"}

    
class Website:
    trending_models = [Image.dreamshaper8, Image.counterfeitv3, Text.mistral7, Video.animateDiff, Text.llama70, Image.pastel_mix]
    
    new_models = [Image.pastel_mix, Image.counterfeitv3,Image.toonyou6]
    
    text_models = [Text.llama70, Text.mistral7, Text.codellama13b]
    
    image_models = [Image.am_i_real, Image.juggernaut_aftermath,  Image.counterfeitv3, Image.absoluteReality, Image.dreamshaper8, Image.guofeng3, Image.anythingv5, Image.kandinsky, Image.sdxl, Image.stable_diff, Image.latentConsistency,Image.toonyou6,Image.openjourneyv4, Image.pastel_mix]
    
    video_models = [Video.animateDiff, Video.zeroScope]
    
    anime_models = [Image.pastel_mix, Image.counterfeitv3, Image.anythingv5]
    
    semi_real_models = [Image.sdxl, Image.kandinsky, Image.toonyou6, Image.latentConsistency]
    
    realistic_models = [Image.absoluteReality, Image.dreamshaper8, Image.guofeng3]
    
    
class leaderboards:
    
    class image:
        fastest_image = []
        
        most_used_images = []
        
        best_image_genration = []
    
    class text:
        fastest_text = []
        
        most_used_text = []
        
        best_text_genration = []
        
    class models:
        fastest_models = []
        
        most_used_models = []
        
        best_model_genration = []

