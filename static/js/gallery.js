// Your existing JavaScript

function showImage(model, src, username, prompt, negPrompt, steps, cfg, seed) {
    var expanded_img_element = document.getElementById("expanded_img");
    var image_element = document.getElementById("image");
    var desc_box_element = document.getElementById("desc_box");

    expanded_img_element.style.display = "block";
    image_element.src = src;
    document.getElementById("model").innerHTML = "Model: " + model;
    document.getElementById("user").innerHTML = "User: " + username;
    document.getElementById("prompt").innerHTML = "Prompt: " + prompt;
    document.getElementById("neg_prompt").innerHTML = "Neg Prompt: " + negPrompt;
    document.getElementById("cfg").innerHTML = "CFG: " + cfg;
    document.getElementById("steps").innerHTML = "steps: " + steps;
    document.getElementById("seed").innerHTML = "seed: " + seed;

}

function closeImage() {
    var expanded_img_element = document.getElementById("expanded_img");
    expanded_img_element.style.display = "none";
}
