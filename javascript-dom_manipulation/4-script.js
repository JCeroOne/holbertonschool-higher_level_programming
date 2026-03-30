document.querySelector("#add_item").addEventListener("click", e => {
    const li = document.createElement("LI");
    li.textContent = "Item";
    document.querySelector("ul").appendChild(li);
});