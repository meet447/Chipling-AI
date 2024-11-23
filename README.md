
[![Website](https://i.ibb.co/C1v2F9q/chipling.png)](https://Chipling.xyz/)



![Screenshot 2024-11-23 145447](https://github.com/user-attachments/assets/85753760-442d-4111-9818-eb8ed6a3ffb3)
![Screenshot 2024-11-23 145413](https://github.com/user-attachments/assets/33041eb2-1780-43f2-b17a-d432a47b2427)
![Screenshot 2024-11-23 145343](https://github.com/user-attachments/assets/636efc15-a77d-424a-9cf5-a269da46d503)
![Screenshot 2024-11-23 145324](https://github.com/user-attachments/assets/5a03bd95-26cf-43bf-be37-028305b28b07)
![Screenshot 2024-11-23 145311](https://github.com/user-attachments/assets/42749d3b-c357-41d7-8f8e-abfd8c7e3e6b)
![Screenshot 2024-11-23 145239](https://github.com/user-attachments/assets/08338aa4-cced-4f24-a47b-67a638703348)

## Run Locally


### Step 1: Create a Firebase Project

1. Go to the [Firebase Console](https://console.firebase.google.com/).
2. Click on "Add Project."
3. Enter a name for your project and choose your preferred country/region.
4. Click "Create Project."

### Step 2: Set up Firebase Authentication

1. In the Firebase Console, go to the "Authentication" section.
2. Enable the "Sign-in method" that you prefer (Email/Password, Google, etc.).
3. Follow the instructions to set up authentication methods.

### Step 3: Get Firebase Configuration

1. In the Firebase Console, click on the gear icon in the left panel to go to "Project Settings."
2. In the "General" tab, scroll down to the "Your apps" section.
3. Click on the "</>" icon to add a web app to your project.
4. Register your app by providing a nickname (e.g., "MyApp").
5. Click "Register App."
6. Copy the generated configuration.

### Step 4: Create a .env file

1. Create a new file in your project root directory and name it `.env`.
2. Open the `.env` file with a text editor.

### Step 5: Add Firebase Configurations to .env

Paste the following lines into your `.env` file and replace the placeholders with the actual values from your Firebase project.

```env
FIREBASE_API_KEY=your_api_key
FIREBASE_AUTH_DOMAIN=your_auth_domain
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_STORAGE_BUCKET=your_storage_bucket
FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
FIREBASE_APP_ID=your_app_id
FIREBASE_MEASUREMENT_ID=your_measurement_id
FIREBASE_DATABASE_URL=your_database_url
```

### Step 6: Save .env File

Save the changes to your `.env` file.

Now, your Firebase project is set up, and your credentials are securely stored in the `.env` file. Make sure to keep your `.env` file private and never expose it to the public.


## Clone the project

```bash
  git clone https://github.com/meet447/Chipling-AI.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install -r requirements.txt 
```

Start the server

```bash
  python wsgi.py
```


# Chipling-AI



## Roadmap

- Create API Routes and Endpoints

- Add more Models

- Add Music Gen models


## Available Models


| Name      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| meta/llama-2-70b-chat | Text |A 70 billion parameter language model from Meta, fine tuned for chat completions
mistralai/mistral-7b-instruct-v0.1|Text|An instruction-tuned 7 billion parameter language model from Mistral
|ai-forever/kandinsky-2.2|Image|multilingual text2image latent diffusion model
|stability-ai/sdxl|Image|A text-to-image generative AI model that creates beautiful images
|stability-ai/stable-diffusion|Image|A latent text-to-image diffusion model capable of generating photo-realistic images given any text input
|lucataco/animate-diff|Video|Animate Your Personalized Text-to-Image Diffusion Models
|anotherjesse/zeroscope-v2-xl|Video|Zeroscope V2 XL & 576w|
|fofr/latent-consistency-model|Image|Super-fast, 0.6s per image. LCM with img2img, large batching and canny controlnet|
|meta/codellama-13b|Text|A 13 billion parameter Llama tuned for code completion|
|anything/anythingv5|Image|Anything V5 is a popular choice among users for generating high-quality images from text prompts.|
|lykon/dreamshaper8|Image|One of the best models|
|lykon/absolutereality|Image|Genrate Realistic Images|
|stability-ai/stable-video-diffusion|Video|Animate your fav images to short vids|



## License

[MIT](https://choosealicense.com/licenses/mit/)


## Tech Stack

**Client:** Html

**Server:** Python, Flask

