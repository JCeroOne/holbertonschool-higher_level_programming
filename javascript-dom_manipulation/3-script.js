document.querySelector("#toggle_header").addEventListener("click", e => {
    const header = document.querySelector("header");
    header.classList.toggle("red");
    header.classList.toggle("green");
});