// analytics.js

// Ensure that the script runs after the DOM has fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Your Google Tag Manager script
    var gtmScript = document.createElement("script");
    gtmScript.async = true;
    gtmScript.src = "https://www.googletagmanager.com/gtag/js?id=G-0444GXLW5F";
  
    // Append the script to the document's head
    document.head.appendChild(gtmScript);
  
    // Define a function to initialize Google Tag Manager
    window.dataLayer = window.dataLayer || [];
    function gtag() {
      dataLayer.push(arguments);
    }
    
    gtag('js', new Date());
    gtag('config', 'G-0444GXLW5F');
  });
  