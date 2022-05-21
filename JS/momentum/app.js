//get stuff from HTML by more ways
//First-id : that you used last time

//Second-className
const hellos = document.getElementsByClassName("hello");
console.log(hellos); //=> you can get all stuffs whom class named "hello"

//Third-tagName
const h1s = document.getElementsByTagName("h1");
console.log(h1s); //=>you can get all stuffs tag is "h1"

//Bestseller Way > querySelector
const title = document.querySelector(".hello h1");
//.hello: .'className', h1: 'tagName'
console.log(title); //=>you get first one of them

//if you want all 3 of them, use querySelectorAll
const titleA = document.querySelectorAll(".hello h1");
console.log(titleA); //you can get all of them by type of array

//How To Use querySelector
//.'className'
//#'id'
//'tagName'.'className' #'id' 'tagName'.'className' #'id' 'tagName'...
const tagName = document.querySelectorAll("div");
const className = document.querySelector("div.class");
const id = document.querySelector("div.class #id");
const _tagName = document.querySelector("div.class #id h2");
console.log(tagName);
//=>[div.class, div#id, div.hello, div.hello, div.hello]
console.log(className);
console.log(id);
console.log(_tagName);
console.log(_tagName.textContent);