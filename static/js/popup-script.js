// script.js
const openModalBtn = document.getElementById("openModalBtn");
const modal = document.getElementById("myModal");
const closeBtn = document.querySelector(".close");
const okButton = document.getElementById("okButton");
const cancelButton = document.getElementById("cancelButton");

// Open the modal when the button is clicked
openModalBtn.addEventListener("click", function() {
    modal.style.display = "block";
});

// Close the modal when the close button or overlay is clicked
closeBtn.addEventListener("click", function() {
    modal.style.display = "none";
});

// Close the modal when the user clicks outside the modal content
window.addEventListener("click", function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});

// Function to handle the "OK" button click
okButton.addEventListener("click", function() {
    // Add your code here to perform the "OK" action
    // For example, you can display a message or execute a function
    modal.style.display = "none";
});

// Function to handle the "Cancel" button click
cancelButton.addEventListener("click", function() {
    // Add your code here to perform the "Cancel" action
    // For example, you can close the modal without any action
    modal.style.display = "none";
});


