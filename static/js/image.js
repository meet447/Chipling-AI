function runModel() {
    var prompt = document.getElementById("prompt").value;
    if (prompt.trim() === "") {
        alert("Please enter a prompt before running the model.");
        return;
    }

    // Display loading gif
    var loadingGif = "https://cdn.pixabay.com/animation/2022/07/29/03/42/03-42-11-849_512.gif";
    var imageElement = document.getElementById("generated-image");
    imageElement.src = loadingGif;


    var models = document.getElementById("title");
    console.log(models.textContent.toLowerCase());


    // Make the API request
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/api/prediction",
        data: {
            model: models.textContent.toLowerCase(),
            prompt: prompt
        },
        success: function (data) {
            checkForResult(data);
        },
        error: function (error) {
            console.error("Error making API request:", error);
        }
    });
}

function checkForResult(id) {
    var interval = setInterval(function () {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/api/response",
            data: { id: id },
            success: function (result) {
                if (result.status === "succeeded") {
                    clearInterval(interval);
                    displayResult(result.output);
                }
            },
            error: function (error) {
                console.error("Error checking for result:", error);
                clearInterval(interval);
            }
        });
    }, 3000);
}

function displayResult(imageUrl) {
    var imageElement = document.getElementById("generated-image");
    imageElement.src = imageUrl;
}