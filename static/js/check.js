// script.js
const showPopupBtn = document.getElementById("showPopupBtn");
const popupOverlay = document.querySelector(".popup-overlay");
const popup = document.getElementById("popup");
const nextButton = document.getElementById("nextButton");
const scoreElement = document.getElementById("score");
var jobname =""

function loaderror() {
  const Errors = document.getElementById("Errors");
  var Errorsvalue = sessionStorage.getItem("pageView");
  console.log(Errorsvalue.split("\n\n"))
  const data = Errorsvalue.split("\n\n")
  for(let i=0;i<data.length;i++){
    Errors.innerHTML += data[i]+"<br><br>";
  }
  
  console.log("Errorsvalue");
}

showPopupBtn.addEventListener("click", function () {
  document.getElementById('showPopupBtn').style.backgroundColor = 'red';
  document.getElementById('showPopupBtn').innerHTML = 'Checked';
  var fileInput = document.getElementById("resume");
  var file = fileInput.files[0];

  var formData = new FormData();
  formData.append("file", file);

  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((message) => {
      // alert(message.jobname);

      // Example: Updating the score
      jobname = message.jobname
      let score = message.score;
      scoreElement.textContent = score + "%";
      // Errors.textContent = message.all_error_type
      console.log(message.all_error_type)
      sessionStorage.setItem("pageView", message.all_error_type);
      var pageView = sessionStorage.getItem("pageView");
      console.log(pageView)

      popupOverlay.style.display = "block"; // Show the overlay
      popup.style.display = "block"; // Show the popup
      // You can perform additional actions after the file is uploaded
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});

nextButton.addEventListener("click", function () {
  popupOverlay.style.display = "none"; // Hide the overlay
  popup.style.display = "none"; // Hide the popup
  console.log(parseInt(scoreElement.textContent.split("%")[0]));

  if (parseInt(scoreElement.textContent.split("%")[0]) > 80) {
    

    var formData = new FormData();
    formData.append("jobname", jobname);

    fetch("/goVacancy", {
        method: "POST",
        body: formData,
    })
    .then(response => {
        if (response.ok) {
            return response.text(); // Assuming your server returns HTML
        }
        throw new Error('Network response was not ok.');
    })
    .then(html => {
        // Assuming you want to replace the current document content with the response
        document.open();
        document.write(html);
        document.close();
    })
    .catch(error => {
        console.error("Error:", error);
    });


  } else {
    window.location.href = "/error";
  }
});

// Function to update the score (you can modify this function as needed)
function updateScore() {
  score++;
  scoreElement.textContent = score;
}
