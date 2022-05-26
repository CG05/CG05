import { io } from 'https://cdn.socket.io/4.4.1/socket.io.esm.min.js';
const socket = io();
//connect to the host
const loginForm = document.querySelector('.login-form');
const loginIdInput = document.querySelector('.login-form input.id');
const loginPwInput = document.querySelector('.login-form input.pw');
const loginSubmit = document.querySelector('.login-form button#login');
const signUpButton = document.querySelector('.login-form button#signUp');
const signUpForm = document.querySelector('.signUp-form');
const signUpIdInput = document.querySelector('.signUp-form input.id');
const signUpPwInput = document.querySelector('.signUp-form input.pw');
const signUpCheckInput = document.querySelector('.signUp-form input.check');
const signUpSubmit = document.querySelector('.signUp-form button#signUp');
const chat = document.querySelector('div.chat');

const HIDDEN_CLASSNAME = 'hidden';
const USERID_KEY = 'userId';
const EMPTY_VALUE = '';

function loginEmit(id, pw) {
	const user = {
		id: id,
		pw: pw,
	};
	socket.emit('login', user);
}
socket.on('login', (req) => {
	console.log(req);
	if (!req.auth) return alert('Cannot authorize. Please check again.');

	loginForm.classList.add(HIDDEN_CLASSNAME);
	successLogin(req.id);
});

function signUpEmit(id, pw) {
	const user = {
		id: id,
		pw: pw,
	};

	socket.emit('signUp', user);
}
socket.on('signUp', (unsigned) => {
	if (!unsigned) return alert('This ID already signed up. Please check again.');
	signUpForm.classList.add(HIDDEN_CLASSNAME);
});

function successLogin(userId) {
	console.log(userId);
	signUpForm.classList.add(HIDDEN_CLASSNAME);
	loginForm.classList.add(HIDDEN_CLASSNAME);
	chat.classList.remove(HIDDEN_CLASSNAME);
	loginIdInput.value = EMPTY_VALUE;
	loginPwInput.value = EMPTY_VALUE;
	socket.emit('connecting', userId);
}
socket.on('connecting', (userId) => console.log(userId, ' successed to login'));

function onLoginSubmit(event) {
	event.preventDefault();
	const id = loginIdInput.value;
	const pw = loginPwInput.value;

	loginEmit(id, pw);
}

function onSignUpSubmit(event) {
	event.preventDefault();
	const id = signUpIdInput.value;
	const pw = signUpPwInput.value;
	const check = signUpCheckInput.value;
	if (pw !== check) {
		return alert('Please enter pw & pw-check to be same');
	}

	signUpEmit(id, pw);
}

function showSignUp(event) {
	event.preventDefault();
	signUpForm.classList.remove(HIDDEN_CLASSNAME);
}

function hideSignUp(event) {
	event.preventDefault();
	signUpForm.classList.add(HIDDEN_CLASSNAME);
}

window.onload = function () {
	loginForm.classList.remove(HIDDEN_CLASSNAME);
	loginSubmit.addEventListener('click', onLoginSubmit);
	signUpButton.addEventListener('click', showSignUp);
	signUpSubmit.addEventListener('click', onSignUpSubmit);
};
