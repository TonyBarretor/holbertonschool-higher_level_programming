// 8-script.js

document.addEventListener("DOMContentLoaded", function() {
    const helloElement = document.getElementById("hello");
  
    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
      .then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then(data => {
        helloElement.textContent = data.hello;
      })
      .catch(error => {
        console.error("There was a problem fetching the translation:", error);
      });
  });
  