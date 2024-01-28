document.addEventListener('DOMContentLoaded', function () {
    // Function to handle button click
    function handleButtonClick(event) {
      const promptTextarea = document.getElementById('prompt');
      const buttonText = event.target.innerText;

      // Append the button text to the textarea
      promptTextarea.value += `${buttonText}, `;
    }

    // Attach click event listeners to all buttons with the class 'prompt'
    const promptButtons = document.querySelectorAll('.prompt');
    promptButtons.forEach(function (button) {
      button.addEventListener('click', handleButtonClick);
    });

    // Function to handle form submission (optional)
    function handleFormSubmit(event) {
      event.preventDefault();
      // Add additional logic for form submission if needed
    }

    // Attach submit event listener to the form
    const form = document.querySelector('.form');
    form.addEventListener('submit', handleFormSubmit);
  });




