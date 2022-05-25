'use strict';

const loginForm = document.querySelector(".login-form");
const loginIdInput = document.querySelector(".login-form input.id");
const loginPwInput = document.querySelector(".login-form input.pw");
const loginSubmit = document.querySelector(".login-form button#login");
const signUpButton = document.querySelector(".login-form button#signUp");
const signUpForm = document.querySelector(".signUp-form");
const signUpIdInput = document.querySelector(".signUp-form input.id");
const signUpPwInput = document.querySelector(".signUp-form input.pw");
const signUpCheckInput = document.querySelector(".signUp-form input.check");
const signUpSubmit = document.querySelector(".signUp-form button#signUp");
const chat = document.querySelector("div.chat");

const HIDDEN_CLASSNAME = "hidden";
const USERID_KEY = "userId";
const USERDB_KEY = "userDb";
const EMPTY_VALUE = "";

let userDb = [
  { id: "admin", pw: "1234" },
  { id: "user0", pw: "5678" },
];
writeDb();

function writeDb() {
  localStorage.setItem(USERDB_KEY, JSON.stringify(userDb));

}

function readDb() {
  const _userDb = JSON.parse(localStorage.getItem(USERDB_KEY));
  return _userDb;
}


function signUp(id, pw) {
  userDb.push({ id: id, pw: pw });
  writeDb();
}

function paintGreetings(userId) {
  console.log(userId);
  signUpForm.classList.add(HIDDEN_CLASSNAME);
  loginForm.classList.add(HIDDEN_CLASSNAME);
  chat.classList.remove(HIDDEN_CLASSNAME);
}

function saveUserId(userId) {
  loginForm.classList.add(HIDDEN_CLASSNAME);
  localStorage.setItem(USERID_KEY, userId);
}

function authorizeUser(id, pw) {
  let result = EMPTY_VALUE;
  const _userDb = readDb();
  for (let i = 0; i < userDb.length; i++) {
    if (id === _userDb[i].id && pw === _userDb[i].pw) return result = id;

  }
}

function onLoginSubmit(event) {
  event.preventDefault();
  const id = loginIdInput.value;
  const pw = loginPwInput.value;
  if (authorizeUser(id, pw) === EMPTY_VALUE) {
    return alert("Please check your id or pw.");
  }
  saveUserId(id);
  paintGreetings(id);
  loginIdInput.value = EMPTY_VALUE;
  loginPwInput.value = EMPTY_VALUE;
}

function onSignUpSubmit(event) {
  event.preventDefault();
  const id = signUpIdInput.value;
  const pw = signUpPwInput.value;
  const check = signUpCheckInput.value;
  if (pw !== check) {
    return alert("Please enter pw & pw-check to be same");
  }
  signUp(id, pw);
  signUpForm.classList.add(HIDDEN_CLASSNAME);
  loginIdInput.value = id;
}

function showSignUp(event) {
  event.preventDefault();
  signUpForm.classList.remove(HIDDEN_CLASSNAME);
}

function hideSignUp(event) {
  event.preventDefault();
  signUpForm.classList.add(HIDDEN_CLASSNAME);
}

const savedUserId = localStorage.getItem(USERID_KEY);

window.onload = function() {
  if (savedUserId === null) {
    loginForm.classList.remove(HIDDEN_CLASSNAME);
    loginSubmit.addEventListener("click", onLoginSubmit);
    signUpButton.addEventListener("click", showSignUp);
    signUpSubmit.addEventListener("click", onSignUpSubmit);

  } else {
    paintGreetings(savedUserId);
  }

}