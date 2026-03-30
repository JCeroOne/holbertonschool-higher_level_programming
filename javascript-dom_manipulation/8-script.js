window.onload = () => {
    fetch("https://hellosalut.stefanbohacek.com/?lang=fr", {method: "GET"})
        .then(res => res.json())
        .then(res => {
            document.querySelector("#hello").textContent = res.hello;
        });
};