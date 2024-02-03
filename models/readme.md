### 1. **Create Model Module**

- **Location:** `models/image/<yourmodel>/<yourmodel.py>`

- **File Content:**
```python
from scrapper.headers import replicate_header
from scrapper.prodia import image

class YourModel:
    def create_image(prompt, neg_prompt, seed, cfg, steps):
        return image.prodiaAPI.create_image(prompt=prompt, neg_prompt=neg_prompt, model="<model you scraped from prodia>", seed=seed, cfg=cfg, steps=steps)
    
    def get_image(id):
        return image.prodiaAPI.get_image(id=id)
```

### 2. **Setup Route**

- **Location:** `models_route.py`

- **File Content:**
```python
def get_model(prompt, model, neg_prompt=None, seed=None, cfg=None, steps=None):
    
    # Test model
    if model == "test":
        return jsonify({"response": "hello from chipling!"})
    
    # Image models
    elif model == "<author>/<modelname>":
        data = YourModel.create_image(prompt)
        return jsonify(data)
    
    else:
        return jsonify({"error": "error occurred"})
```

### 3. **Setup Model Data**

- **Location:** `modelsData.py`

- **File Content:**
```python
class Image:

    sdxl = {"author": "stability-ai", "model": "sdxl", "desc": "A text-to-image generative AI model that creates beautiful images", "github": "https://github.com/replicate/cog-sdxl", "runs": "33.4M", "img": "https://learn.thinkdiffusion.com/content/images/2023/07/00000-3097553845B.jpg"}
```

### 4. **Update app.py**

- **Location:** `app.py`

- **File Content:**
```python
@app.route("/<author>/<model>")
def generateImage_page(author, model):
    
    # Image models
    if model == "sdxl" and author == "stability-ai":
       return render_template("image.html", data=Image.sdxl, prompt=Image.prompts)
    elif model == "stable-diffusion" and author == "stability-ai":
       return render_template("image.html", data=Image.stable_diff, prompt=Image.prompts)
```

### 5. **Documentation**

- Include a README.md file that explains the purpose of each file and the overall structure.
- Provide instructions on how to add a new model using this template.
- Specify any dependencies or configurations needed.

With these organized steps, developers can easily understand and implement new models into the web application. Remember to update the documentation as needed and provide examples for clarity.


# TO ADD MODELS

| author  | model         | safe tensor                            | Image                                                                                                                                     |   |
|---------|---------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|---|
| wrs111  | guofeng3      | 3Guofeng3_v34.safetensors [50f420de]   | https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d3315e02-7c0f-420e-911f-abd53a0ebb28/original=true/tmp9d4z8vav.jpeg                      |   |
| lostdog | am_i_real     | amIReal_V41.safetensors [0a8a2e61]     | https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/19950811-769f-4e08-b0dc-7440b1c46d6a/width=950/00358-136185449-6fa438a7af-1640x1024.jpeg |   |
| rqdwdw  | counterfeitv3 | Counterfeit_v30.safetensors [9e2a8f19] | https://assets-global.website-files.com/624ac40503a527cf47af4192/64ad98a93748b1dd485f971d_003.jpeg                                        |   |