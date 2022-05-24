'use strict';
const API_KEY = "8185d5b7811c6407a414d32d7ee31b39"
const weatherContainer = document.querySelector("#weather span:first-child");
const city = document.querySelector("#weather span:last-child");

function onGeoOk(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;
  console.log("You live in ", lat, lon);
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
    //JS will call url with fetch.
  fetch(url)
    .then(Response => Response.json())
    .then(data => {
      city.innerText = data.name;
      weatherContainer.innerText = `Today weather is ${data.weather[0].main} @ ${data.main.temp}˚C`;
    });
}

function onGeoError() {
  alert("Can't find you. No weather for you.");
}

//You can get current coordinate! Just ONE line of code!
navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);