fetch("https://swapi-api.hbtn.io/api/films/?format=json", {method: "GET"})
    .then(res => res.json())
    .then(res => {
        res.results.forEach(r => {
            const li = document.createElement("li");
            li.textContent = r.title;
            document.querySelector("#list_movies").appendChild(li);
        });
    });