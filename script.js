const button = document.querySelector("#welcome-button");

function showMessage() {
    button.textContent = "Welcome, traveler!";
}

button.addEventListener("click", showMessage);