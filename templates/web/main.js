// main.js
window.onload = function() {
    fetch('/get_logged_in_user')
        .then(response => {
            if (!response.ok) {
                throw new Error('No logged-in user');
            }
            return response.json();
        })
        .then(data => {
            console.log(data); // handle the logged-in user data
            // You can update the DOM here based on the user data
        })
        .catch(error => console.error('Error:', error));
};
