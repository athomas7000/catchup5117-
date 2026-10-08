const button = document.querySelector("#welcome-button");

function showMessage() {
    button.textContent = "Welcome, traveler!";
}

button.addEventListener("click", showMessage);
const nameInput = document.querySelector("#guest-name");
const addGuestButton = document.querySelector("#add-guest");
const guestList = document.querySelector("#guest-list");




function addGuest() {
    const name = nameInput.value.trim();

    if (name === "") {
        return;
    }

    const listItem = document.createElement("li");
    listItem.textContent = name;
    guestList.appendChild(listItem);

    nameInput.value = "";
}

addGuestButton.addEventListener("click", addGuest);