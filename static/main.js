// main.js
document.addEventListener('DOMContentLoaded', function() {
    // Your code goes here
    console.log("main.js loaded");
});

// window.onload = function() {
//     fetch('/get_logged_in_user')
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('No logged-in user');
//             }
//             return response.json();
//         })
//         .then(data => {
//             console.log(data); // handle the logged-in user data
//             // You can update the DOM here based on the user data
//         })
//         .catch(error => console.error('Error:', error));
// };

document.getElementById('startButton').addEventListener('click', function() {
    console.log("Start button clicked");
    var time = 10;
    var timerDisplay = document.getElementById('timerDisplay');
    var countdown = time;

    // Update the countdown every 1 second
    var interval = setInterval(function() {
        timerDisplay.innerHTML = countdown;
        countdown--;

        // Check if the countdown is over
        if (countdown < 0) {
            clearInterval(interval);
            timerDisplay.innerHTML = "00:00";
            timerDisplay.classList.add('blinking');
        }
    }, 1000);
});