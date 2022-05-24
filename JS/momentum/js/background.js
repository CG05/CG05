'use strict';

const images = ["0.jpeg", "1.jpeg", "2.jpeg", ];

const randomImg = Math.floor(Math.random() * images.length);
const chosenImage = images[randomImg];

const bgImg = document.createElement("img");
bgImg.src = `../img/${chosenImage}`;
console.log(bgImg);

document.body.appendChild(bgImg);