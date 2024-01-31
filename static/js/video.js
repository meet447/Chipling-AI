function runModel() {
    var prompt = document.getElementById("prompt").value;
    if (prompt.trim() === "") {
        alert("Please enter a prompt before running the model.");
        return;
    }

    var runButtons = document.getElementsByClassName("run-button");
    for (var i = 0; i < runButtons.length; i++) {
        runButtons[i].disabled = false;
    }

    // Display loading gif
    var loadingGif = "https://static.videezy.com/system/resources/previews/000/014/052/original/loading_circle_bars.mp4";

    var errorGif = "https://i.gifer.com/embedded/download/GY9C.gif"

    var imageElement = document.getElementById("generated-video");
    imageElement.src = loadingGif;

    // Disable video player controls and set video to autoloop and play
    imageElement.controls = false;
    imageElement.loop = true;
    imageElement.play();

    var models = document.getElementById("title");
    console.log(models.textContent.toLowerCase());

    // Determine the current domain
    var currentDomain = window.location.origin;

    // Make the API request
    $.ajax({
        type: "GET",
        url: currentDomain + "/api/prediction",
        data: {
            model: models.textContent.toLowerCase(),
            prompt: prompt
        },
        success: function (data) {
            checkForResult(data, runButtons, imageElement);
            console.log(data)
        },
        error: function (error) {
            console.error("Error making API request:", error);
            for (var i = 0; i < runButtons.length; i++) {
                runButtons[i].disabled = false;
            }
            // Enable video player controls again
            imageElement.controls = true;
        }
    });
}

function checkForResult(id, runButtons, imageElement) {
    var interval = setInterval(function () {
        // Determine the current domain
        var currentDomain = window.location.origin;

        var errorGif = "https://i.gifer.com/embedded/download/GY9C.gif"

        $.ajax({
            type: "GET",
            url: currentDomain + "/api/response",
            data: { id: id },
            success: function (result) {
                if (result.status === "succeeded") {
                    clearInterval(interval);
                    displayResult(result.output, runButtons, imageElement);
                }
                else if (result.status === "failed") {
                    clearInterval(interval);
                    displayResult(errorGif, runButtons, imageElement);
                    alert("Something went wrong.");
                    return;
                }
            },
            error: function (error) {
                console.error("Error checking for result:", error);
                clearInterval(interval);

                imageElement.src = errorGif;

                for (var i = 0; i < runButtons.length; i++) {
                    runButtons[i].disabled = false;
                }
                // Enable video player controls again
                imageElement.controls = true;
            }
        });
    }, 3000);
}

function displayResult(imageUrl, runButtons, imageElement) {
    // Enable video player controls again
    imageElement.controls = true;

    for (var i = 0; i < runButtons.length; i++) {
        runButtons[i].disabled = false;
    }

    // Set the result image URL
    imageElement.src = imageUrl;
}
