// script.js
console.log("hello")
const button = document.getElementById('changeColorButton');
const body = document.body;

button.addEventListener('click', () => {
    body.classList.toggle('changed-color');
});
