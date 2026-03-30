fetch("https://swapi-api.hbtn.io/api/people/5/?format=json", {method: "GET"})
    .then(res => res.json())
    .then(res => {
        document.querySelector("#character").textContent = res.name;
    });