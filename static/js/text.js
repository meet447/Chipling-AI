function runModel() {
    var prompt = document.getElementById("prompt").value;
    if (prompt.trim() === "") {
        alert("Please enter a prompt before running the model.");
        return;
    }
    var models = document.getElementById("title");
    console.log(models.textContent.toLowerCase());

    var currentDomain = window.location.origin;

    // Disable the run button
    var runButtons = document.getElementsByClassName("run-button");
    for (var i = 0; i < runButtons.length; i++) {
        runButtons[i].disabled = true;
        console.log("Button disabled");
    }

    var textPlaceholder = document.getElementById("generated-text-placeholder");
    textPlaceholder.textContent = "please wait genrating response might take some time for server to boot up!";

    // Make the API request
    $.ajax({
        type: "GET",
        url: currentDomain + "/api/prediction",
        data: {
            model: models.textContent.toLowerCase(),
            prompt: prompt
        },
        success: function (data) {
            console.log(data);
            checkForResult(data, runButtons);
        },
        error: function (error) {
            console.error("Error making API request:", error);
            // Enable the run button in case of an error
            for (var i = 0; i < runButtons.length; i++) {
                runButtons[i].disabled = false;
            }
            console.log("Button disabled");
        }
    });
}

function checkForResult(id, runButtons) {
    var interval = setInterval(function () {
        // Determine the current domain
        var currentDomain = window.location.origin;

        $.ajax({
            type: "GET",
            url: currentDomain + "/api/response",
            data: { id: id },
            success: function (result) {
                output = result.output
                var sentence = output.join('');
                console.log(sentence);

                // Updated: Display the generated sentence in the text placeholder
                var textPlaceholder = document.getElementById("generated-text-placeholder");
                textPlaceholder.textContent = sentence;

                if (result.status === "succeeded") {
                    clearInterval(interval);
                    console.log("result complete");
                    // Enable the run button once the result is succeeded
                    for (var i = 0; i < runButtons.length; i++) {
                        runButtons[i].disabled = false;
                    }
                    console.log("Button enabled");

                } else if (result.status === "failed") {
                    clearInterval(interval);
                    console.log("error failed");
                    // Enable the run button in case of failure
                    for (var i = 0; i < runButtons.length; i++) {
                        runButtons[i].disabled = false;
                    }
                }
            },
            error: function (error) {
                console.error("Error checking for result:", error);
                clearInterval(interval);

                // Enable the run button in case of an error
                for (var i = 0; i < runButtons.length; i++) {
                    runButtons[i].disabled = false;
                }
                // ... (your existing error handling code) ...
            }
        });
    }, 2000);
}
