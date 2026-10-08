const button = document.querySelector("#welcome-button");

function showMessage() {
    button.textContent = "Welcome, traveler!";
}

button.addEventListener("click", showMessage);


const guestForm = document.querySelector("#guest-form");
const guestNameInput = document.querySelector("#guest-name");
const guestList = document.querySelector("#guest-list");

guestForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(guestForm);

    const response = await fetch("/guestbook", {
        method: "POST",
        body: formData
    });

    const guest = await response.json();

    const listItem = document.createElement("li");
    listItem.textContent = guest.name;
    guestList.appendChild(listItem);

    guestNameInput.value = "";
});