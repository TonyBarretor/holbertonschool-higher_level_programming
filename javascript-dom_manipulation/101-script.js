// 101-script.js

document.addEventListener("DOMContentLoaded", function() {
    const btnTranslate = document.getElementById("btn_translate");
    const languageCode = document.getElementById("language_code");
    const helloElement = document.getElementById("hello");
  
    btnTranslate.addEventListener("click", function() {
      const selectedLanguage = languageCode.value;
      if (selectedLanguage) {
        fetch(`https://hellosalut.stefanbohacek.dev/?lang=${selectedLanguage}`)
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
      } else {
        console.error("Please choose a language");
      }
    });
  });
  