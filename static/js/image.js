document.addEventListener("DOMContentLoaded", function() {
    // Code executed after the DOM has fully loaded

    // Getting references to HTML elements
    var slider = document.getElementById("myCFG");
    var output = document.getElementById("cfg");
    var steps_slider = document.getElementById("mySteps");
    var steps_output = document.getElementById("steps");

    // Setting initial values for the sliders
    output.innerHTML = slider.value;
    steps_output.innerHTML = steps_slider.value;

    // Event listeners to update slider values in real-time
    slider.oninput = function() {
        output.innerHTML = this.value;
        console.log(slider.value);
    };

    steps_slider.oninput = function() {
        steps_output.innerHTML = this.value;
        console.log(steps_slider.value);
    };


    window.runModel= function() {
        // Getting user input values
        var prompt = document.getElementById("prompt").value;
        var seed = document.getElementById("seed_value").value;
        var neg_prompt_element = document.getElementById("neg_prompt");
        var neg_prompt = neg_prompt_element ? neg_prompt_element.value : null;
        var steps_element = document.getElementById("mySteps").value;
        var steps = steps_element ? steps_element : null;
        var cfg_element = document.getElementById("myCFG").value;
        var cfg = cfg_element ? cfg_element : null;

        // Validation for prompt and seed
        if (prompt.trim() === "") {
            alert("Please enter a prompt before running the model.");
            return;
        }

        if (seed.trim() === "") {
            alert("Please enter a seed (-1 default) before running the model.");
            return;
        }

        // Logging user input values
        console.log("This is the negative prompt: " + neg_prompt);
        console.log("This is the cfg value: " + cfg);
        console.log("This is the steps value: " + steps);
        console.log("This is the seed value: " + seed);


        // Display loading gif
        var loadingGif = "https://cdn.pixabay.com/animation/2022/07/29/03/42/03-42-11-849_512.gif";
        
        var imageElement = document.getElementById("generated-image");
        imageElement.src = loadingGif;

        var models = document.getElementById("title");
        var modelText = models.textContent.toLowerCase();

        // Determine the current domain
        var currentDomain = window.location.origin;

        // Prepare the data object for the API request
        var requestData = {
            model: modelText,
            prompt: prompt
        };

        // Add neg_prompt to requestData only if it is not null
        if (neg_prompt !== null) {
            requestData.neg_prompt = neg_prompt;
            requestData.cfg = cfg;
            requestData.steps = steps;
            requestData.seed = seed;
        }

        // Make the API request
        $.ajax({
            type: "GET",
            url: currentDomain + "/api/prediction",
            data: requestData,
            success: function (data) {
                console.log(data);
                checkForResult(id=data);
            },
            error: function (error) {
                console.error("Error making API request:", error);
            }
        });
    }


    function checkForResult(id) {
        var interval = setInterval(function () {
            // Determine the current domain
            var currentDomain = window.location.origin;

            var errorGif = "https://i.gifer.com/embedded/download/GY9C.gif"

            $.ajax({
                type: "GET",
                url: currentDomain + "/api/response",
                data: { id: id },
                success: function (result) {
                    console.log(result)
                    if (result.status === "succeeded") {
                        clearInterval(interval);
                        displayResult(result.output);
                    }
                    else if (result.status === "failed"){
                        clearInterval(interval);
                        displayResult(errorGif);
                    }
                },
                error: function (error) {
                    console.error("Error checking for result:", error);
                    clearInterval(interval);

                    var imageElement = document.getElementById("generated-image");
                    imageElement.src = errorGif;
                }
            });
        }, 3000);
    }

    function displayResult(imageUrl) {
        var imageElement = document.getElementById("generated-image");
        imageElement.src = imageUrl;
    }

});