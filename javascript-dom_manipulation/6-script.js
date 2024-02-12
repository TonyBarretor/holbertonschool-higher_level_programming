document.addEventListener("DOMContentLoaded", function() {
    const characterTag = document.getElementById("character");
  
    fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
      .then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then(data => {
        characterTag.textContent = data.name;
      })
      .catch(error => {
        console.error("There was a problem fetching the character:", error);
      });
  });
  