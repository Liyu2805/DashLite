const form = document.querySelector(".txt");
const inputs = document.querySelectorAll(".inputbox");

form.addEventListener("submit", function (event) {
  let isValid = true;

  inputs.forEach(function (input) {
    if (input.name === "name" && input.value.trim().length < 3) {
      isValid = false;
    }
    if (input.name === "email" && !input.value.includes("@")) {
      isValid = false;
    }
    if (input.name === "message" && input.value.trim().length < 10) {
      isValid = false;
    }
  });

  if (!isValid) {
    event.preventDefault();
    alert("There is something wrong");
  }
});