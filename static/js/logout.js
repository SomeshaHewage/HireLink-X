// script.js
const logoutModalBtn = document.getElementById("logoutModalBtn");
const logoutmodal = document.getElementById("logoutmyModal");
const logoutcloseBtn = document.querySelector(".logoutclose");
const yesButton = document.getElementById("yesButton");
const noButton = document.getElementById("noButton");

// Open the modal when the button is clicked
logoutModalBtn.addEventListener("click", function() {
    logoutmodal.style.display = "block";
});

// Close the modal when the close button or overlay is clicked
logoutcloseBtn.addEventListener("click", function() {
    logoutmodal.style.display = "none";
});

// Close the modal when the user clicks outside the modal content
window.addEventListener("click", function(event) {
    if (event.target === logoutmodal) {
        logoutmodal.style.display = "none";
    }
});

// Function to handle the "OK" button click
yesButton.addEventListener("click", function() {
    // Add your code here to perform the "OK" action
    // For example, you can display a message or execute a function
    logoutmodal.style.display = "none";
});

// Function to handle the "Cancel" button click
noButton.addEventListener("click", function() {
    // Add your code here to perform the "Cancel" action
    // For example, you can close the modal without any action
    logoutmodal.style.display = "none";
});


