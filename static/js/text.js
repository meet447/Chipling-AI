function toggleButtonsVisibility(className, isVisible) {
    var buttons = document.getElementsByClassName(className);
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].style.display = isVisible ? "inline-block" : "none";
        console.log("done");
    }
}

function runModel() {
    var prompt = document.getElementById("prompt").value;
    if (prompt.trim() === "") {
        alert("Please enter a prompt before running the model.");
        return;
    }
    var models = document.getElementById("title");
    console.log(models.textContent.toLowerCase());

    var currentDomain = window.location.origin;

    var runButtons = document.getElementsByClassName("run-button");
    
    toggleButtonsVisibility("run-button", true);
    toggleButtonsVisibility("continue-gen-button", false);

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

                var textPlaceholder = document.getElementById("generated-text-placeholder");
                textPlaceholder.textContent = sentence;

                formatGeneratedText()

                if (result.status === "succeeded") {
                    clearInterval(interval);
                    console.log("result complete");
                    for (var i = 0; i < runButtons.length; i++) {
                        runButtons[i].disabled = false;
                    }
                    console.log("Button enabled");

                } else if (result.status === "failed") {
                    clearInterval(interval);
                    console.log("error failed");
                    for (var i = 0; i < runButtons.length; i++) {
                        runButtons[i].disabled = false;
                    }
                }
            },
            error: function (error) {
                console.error("Error checking for result:", error);
                clearInterval(interval);
            }
        });
    }, 2000);
}


function continueModel()
{
    
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
    prompt = textPlaceholder.textContent

    $.ajax({
        type: "GET",
        url: currentDomain + "/api/prediction",
        data: {
            model: models.textContent.toLowerCase(),
            prompt: prompt + "\n continue genrationg this",
        },
        success: function (data) {
            console.log(data);
            var textPlaceholder = document.getElementById("generated-text-placeholder");
            pregen = textPlaceholder.textContent;
            checkForResultGen(data, runButtons, pregen);
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

function formatGeneratedText() {
    var generatedText = document.getElementById('generated-text-placeholder');
    var lines = generatedText.textContent.split('\n');

    generatedText.innerHTML = ''; // Clear the original content

    var container = document.createElement('div');
    var currentList = null;
    var inCodeBlock = false;
    var codeBlock = null;

    lines.forEach(function (line) {
        line = line.trim();

        if (line.startsWith('```')) {
            // Toggle code block
            if (inCodeBlock) {
                container.appendChild(codeBlock);
                codeBlock = null;
            } else {
                inCodeBlock = true;
                codeBlock = document.createElement('code');
            }
        } else if (inCodeBlock) {
            // Inside code block
            var codeLine = document.createElement('div');
            codeLine.textContent = line;
            codeBlock.appendChild(codeLine);
        } else if (line.startsWith('#')) {
            // Heading
            var level = line.indexOf('#') + 1;
            var heading = document.createElement('h' + level);
            heading.textContent = line.substring(level).trim();
            container.appendChild(heading);
        } else if (line.startsWith('*')) {
            // Unordered list
            if (!currentList || currentList.tagName !== 'UL') {
                currentList = document.createElement('ul');
                container.appendChild(currentList);
            }
            var listItem = document.createElement('li');
            listItem.textContent = line.substring(1).trim();
            currentList.appendChild(listItem);
        } else if (line.match(/^\d+\./)) {
            // Ordered list
            if (!currentList || currentList.tagName !== 'OL') {
                currentList = document.createElement('ol');
                container.appendChild(currentList);
            }
            var listItem = document.createElement('li');
            listItem.textContent = line.replace(/^\d+\./, '').trim();
            currentList.appendChild(listItem);
        } else {
            // Paragraph
            if (line !== '') {
                var paragraph = document.createElement('p');
                paragraph.textContent = line;
                container.appendChild(paragraph);
            }
        }
    });

    if (codeBlock) {
        container.appendChild(codeBlock);
    }

    generatedText.appendChild(container);
}


function checkForResultGen(id, runButtons, pregen) {
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

                var textPlaceholder = document.getElementById("generated-text-placeholder");

                textPlaceholder.textContent = pregen + sentence;

                formatGeneratedText();

                console.log("formated")

                if (result.status === "succeeded") {
                    clearInterval(interval);
                    console.log("result complete");
                    for (var i = 0; i < runButtons.length; i++) {
                        runButtons[i].disabled = false;
                    }
                    console.log("Button enabled");

                } else if (result.status === "failed") {
                    clearInterval(interval);
                    console.log("error failed");
                    for (var i = 0; i < runButtons.length; i++) {
                        runButtons[i].disabled = false;
                    }
                }
            },
            error: function (error) {
                console.error("Error checking for result:", error);
                clearInterval(interval);
                for (var i = 0; i < runButtons.length; i++) {
                    runButtons[i].disabled = false;
                }
            }
        });
    }, 2000);
}