document.addEventListener("DOMContentLoaded", function() {
    var slider = document.getElementById("myCFG");
    var output = document.getElementById("cfg");
    var steps_slider = document.getElementById("mySteps");
    var steps_output = document.getElementById("steps");
    var seed_element = document.getElementById("seed_value");

    // Setting initial values for the sliders
    if (output !== null){
        output.innerHTML = slider ? slider.value : "";
    }
    if (steps_output !== null){
        steps_output.innerHTML = steps_slider ? steps_slider.value : "";
    }
    // Event listeners to update slider values in real-time
    if (slider !== null) {
        output.innerHTML = slider.value;
        slider.oninput = function() {
            output.innerHTML = this.value;
            console.log(slider.value);
        };
    
    } else {
        output = "Slider is null";
    }

    if (steps_slider !== null){
        steps_output.innerHTML = steps_slider.value
        steps_slider.oninput = function() {
            steps_output.innerHTML = this.value;
            console.log(steps_slider.value);
        };
    }
    else {
        steps_output = "Slider is null";
    }
    
    window.uploadPost = function() {
        // Getting values from input elements

        var prompt_element = document.getElementById("prompt");
        var prompt = prompt_element ? prompt_element.value : "";

        var seed_element = document.getElementById("seed_value");
        var seed = seed_element ? seed_element.value : null;

        var neg_prompt_element = document.getElementById("neg_prompt");
        var neg_prompt = neg_prompt_element ? neg_prompt_element.value : null;

        var steps_element = document.getElementById("mySteps");
        var steps = steps_element ? steps_element.value : null;

        var cfg_element = document.getElementById("myCFG");
        var cfg = cfg_element ? cfg_element.value : null;

        var imageElement = document.getElementById("generated-image");
        var image = imageElement.src

        var models = document.getElementById("title");
        var modelText = models.textContent.toLowerCase();

        
        if (seed != null)
        {
            if (prompt.trim() === "") {
                alert("Please enter a prompt before running the model.");
                return;
            }

            if (seed.trim() === "") {
                alert("Please enter a seed (-1 default) before running the model.");
                return;
            }

            if (image.trim() === "") {
                alert("Please Genrate a Image before uploading.");
                return;
            }
        }


        // Determine the current domain
        var currentDomain = window.location.origin;

        var requestData = {
            model: modelText,
            prompt: prompt,
            neg_prompt: neg_prompt,
            cfg:cfg,
            steps:steps,
            seed:seed,
            image: image
        };
        
        $.ajax({
            type: "GET",
            url: currentDomain + "/uploads",
            data: requestData,
            success: function (data) {
                console.log(data);
                if( document.getElementById("uploadButton"))
                {
                  document.getElementById("uploadButton").style.display = "none";
                }
                
            },
            error: function (error) {
                console.error("Error uploading post :", error);
            }
        });
    }
    window.uploadProfile = function() {
        // Getting values from input elements

        var prompt_element = document.getElementById("prompt");
        var prompt = prompt_element ? prompt_element.value : "";

        var seed_element = document.getElementById("seed_value");
        var seed = seed_element ? seed_element.value : null;

        var neg_prompt_element = document.getElementById("neg_prompt");
        var neg_prompt = neg_prompt_element ? neg_prompt_element.value : null;

        var steps_element = document.getElementById("mySteps");
        var steps = steps_element ? steps_element.value : null;

        var cfg_element = document.getElementById("myCFG");
        var cfg = cfg_element ? cfg_element.value : null;

        var imageElement = document.getElementById("generated-image");
        var image = imageElement.src

        var models = document.getElementById("title");
        var modelText = models.textContent.toLowerCase();

        
        if (seed != null)
        {
            if (prompt.trim() === "") {
                alert("Please enter a prompt before running the model.");
                return;
            }

            if (seed.trim() === "") {
                alert("Please enter a seed (-1 default) before running the model.");
                return;
            }

            if (image.trim() === "") {
                alert("Please Genrate a Image before uploading.");
                return;
            }
        }


        // Determine the current domain
        var currentDomain = window.location.origin;

        var requestData = {
            model: modelText,
            prompt: prompt,
            neg_prompt: neg_prompt,
            cfg:cfg,
            steps:steps,
            seed:seed,
            image: image
        };
        
        $.ajax({
            type: "GET",
            url: currentDomain + "/uploads_profile",
            data: requestData,
            success: function (data) {
                console.log(data);
                if( document.getElementById("uploadprofileButton"))
                {
                  document.getElementById("uploadprofileButton").style.display = "none";
                }
                
            },
            error: function (error) {
                console.error("Error uploading post :", error);
            }
        });
    }



    window.runModel= function() {

        if(document.getElementById("uploadButtom") != null)
        {
          document.getElementById("uploadButton").style.display = "none";
        }
        if(document.getElementById("uploadprofileButton") != null)
        {
          document.getElementById("uploadprofileButton").style.display = "none";
        }            
        var prompt = document.getElementById("prompt").value;
        var seed = seed_element ? seed_element.value : null;

        // Getting user input values
        var prompt_element = document.getElementById("prompt");
        var prompt = prompt_element ? prompt_element.value : "";

        var seed_element = document.getElementById("seed_value");
        var seed = seed_element ? seed_element.value : "none";

        var neg_prompt_element = document.getElementById("neg_prompt");
        var neg_prompt = neg_prompt_element ? neg_prompt_element.value : null;

        var steps_element = document.getElementById("mySteps");
        var steps = steps_element ? steps_element.value : null;

        var cfg_element = document.getElementById("myCFG");
        var cfg = cfg_element ? cfg_element.value : null;

        // Validation for prompt and seed
        if (prompt.trim() === "") {
            alert("Please enter a prompt before running the model.");
            return;
        }
        if(seed != null){
            if (seed.trim() === "") {
                alert("Please enter a seed (-1 default) before running the model.");
                return;
            }
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
                        if( document.getElementById("uploadButton"))
                        {
                        document.getElementById("uploadButton").style.display = "block";
                        }
                        if( document.getElementById("uploadprofileButton"))
                        {
                        document.getElementById("uploadprofileButton").style.display = "block";
                        }
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
        }, 2000);
    }

    function displayResult(imageUrl) {
        var imageElement = document.getElementById("generated-image");
        imageElement.src = imageUrl;
    }

});