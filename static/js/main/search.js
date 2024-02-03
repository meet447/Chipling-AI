// Wait for the document to be ready
$(document).ready(function() {
    // Capture the submit event on the search form
    $('.search-container').submit(function(event) {
        // Prevent the default form submission
        event.preventDefault();
        
        // Get the input value
        var query = $('#searchInput').val().trim();
        
        // Check if the query is not empty
        if (query !== '') {
            // Redirect to the search page with the input value
            window.location.href = '/search/' + query;
        }
    });
});