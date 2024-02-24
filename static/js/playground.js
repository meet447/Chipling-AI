document.addEventListener("DOMContentLoaded", function () {
    const loadingGif = "https://cdn.pixabay.com/animation/2022/07/29/03/42/03-42-11-849_512.gif";
    const errorGif = "https://i.gifer.com/embedded/download/GY9C.gif";

    function displayOutput(element, value) {
        if (element !== null) {
            element.innerHTML = value;
        }
    }

    function validateInput(value, errorMessage) {
        if (value === null || value.trim() === "") {
            alert(errorMessage);
            return false;
        }
        return true;
    }

    const slider = document.getElementById("myCFG");
    const output = document.getElementById("cfg");
    const stepsSlider = document.getElementById("mySteps");
    const stepsOutput = document.getElementById("steps");
    const seedElement = document.getElementById("seed_value");

    displayOutput(output, slider ? slider.value : "");
    displayOutput(stepsOutput, stepsSlider ? stepsSlider.value : "");

    if (slider !== null) {
        slider.addEventListener("input", function () {
            displayOutput(output, this.value);
            console.log(slider.value);
        });
    } else {
        console.error("Slider is null");
    }

    if (stepsSlider !== null) {
        stepsSlider.addEventListener("input", function () {
            displayOutput(stepsOutput, this.value);
            console.log(stepsSlider.value);
        });
    } else {
        console.error("Steps slider is null");
    }

    window.runModel = function () {
        const promptElement = document.getElementById("prompt");
        const prompt = promptElement ? promptElement.value : "";


        let currentModel = "";

        const realisticCheckbox = document.getElementById('realistic');
        const animeCheckbox = document.getElementById('anime');
        const semiRealisticCheckbox = document.getElementById('semi-realistic');
        
        const checkedCheckboxes = [realisticCheckbox, animeCheckbox, semiRealisticCheckbox].filter(checkbox => checkbox.checked);
        if (checkedCheckboxes.length !== 1) {
            alert("Please select exactly one checkbox before running the model.");
            return;
        }
        
        console.log(currentModel);

        if (!validateInput(prompt, "Please enter a prompt before running the model.")) {
            return;
        }

        const seedElement = document.getElementById("seed_value");
        const seed = seedElement ? seedElement.value : "none";

        if (!validateInput(seed, "Please enter a seed (-1 default) before running the model.")) {
            return;
        }

        if(document.getElementById("runButton") != null)
        {
          document.getElementById("runButton").style.display = "none";
        }

        const negPromptElement = document.getElementById("neg_prompt");
        const negPrompt = negPromptElement ? negPromptElement.value : null;

        const stepsElement = document.getElementById("mySteps");
        const steps = stepsElement ? stepsElement.value : null;

        const cfgElement = document.getElementById("myCFG");
        const cfg = cfgElement ? cfgElement.value : null;

        const semi_models = ["bradcatt/toonyou6", "fofr/latent-consistency-model", "stability-ai/sdxl", "ai-forever/kandinsky-2.2"];
        const anime_models = ["rqdwdw/counterfeitv3", "anything/anythingv5", "stability-ai/sdxl", "bradcatt/toonyou6"];
        const real_models = ["kandooai/juggernaut_aftermath", "wrs111/guofeng3", "lykon/dreamshaper8", "lostdog/am-i-real"];

        const imageElements = [
            document.getElementById("generated-image1"),
            document.getElementById("generated-image2"),
            document.getElementById("generated-image3"),
            document.getElementById("generated-image4")
        ];

        const currentDomain = window.location.origin;

        for (let i = 0; i < real_models.length; i++) {
            (function (index) {
                if (realisticCheckbox.checked) {
                    console.log('Realistic checkbox is selected');
                    currentModel = real_models[index];
                } else if (animeCheckbox.checked) {
                    console.log('Anime checkbox is selected');
                    currentModel = anime_models[index];
                } else if (semiRealisticCheckbox.checked) {
                    console.log('Semi-Realistic checkbox is selected');
                    currentModel = semi_models[index];
                }

                const requestData = {
                    model: currentModel,
                    prompt: prompt,
                    neg_prompt: negPrompt,
                    cfg: cfg,
                    steps: steps,
                    seed: seed,
                };

                const requestDataCopy = { ...requestData };
                requestDataCopy.index = index + 1;

                const imageElement = imageElements[index];
                if (imageElement) {
                    imageElement.src = loadingGif;
                }

                $.ajax({
                    type: "GET",
                    url: currentDomain + "/api/prediction",
                    data: requestDataCopy,
                    success: function (data) {
                        checkForResult(data, index + 1);
                    },
                    error: function (xhr, textStatus, errorThrown) {
                        console.error("Error making API requests:", textStatus, errorThrown);
                        displayResult(errorGif, index + 1);
                    }
                });
            })(i);
        }
    };

    function checkForResult(id, index) {
        const interval = setInterval(function () {
            const currentDomain = window.location.origin;

            $.ajax({
                type: "GET",
                url: currentDomain + "/api/response",
                data: { id: id },
                success: function (result) {
                    if (result && result.status) {
                        if (result.status === "succeeded") {
                            clearInterval(interval);
                            displayResult(result.output, index);
                            if(document.getElementById("runButton") != null  && index == 4)
                            {
                             document.getElementById("runButton").style.display = "block";
                             }
                        } else if (result.status === "failed") {
                            clearInterval(interval);
                            displayResult(errorGif, index);
                            if(document.getElementById("runButton") != null)
                            {
                            document.getElementById("runButton").style.display = "block";
                            }
                        }
                    } else {
                        console.error("Unexpected response format:", result);
                        clearInterval(interval);
                        displayResult(errorGif, index);
                    }
                },
                error: function (xhr, textStatus, errorThrown) {
                    console.error("Error checking for result:", textStatus, errorThrown);
                    clearInterval(interval);
                    displayResult(errorGif, index);
                }
            });
        }, 3000);
    }

    function displayResult(imageUrl, index) {
        const imageElement = document.getElementById("generated-image" + index);
        if (imageElement) {
            imageElement.src = imageUrl;
        }
    }
});
