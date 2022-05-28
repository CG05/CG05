const express = require('express');
const http = require('http');
const path = require('path');
const { Server } = require('socket.io');
const mysql = require('mysql');

const app = express();
const PORT = 8080;
const server = http.createServer(app);
const io = new Server(server);
const userDb = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: 'Pomcom1123@',
	database: 'Users',
});
const AUTHDATA_TABLE = 'auth_data';
const LOGGEDUSERS_TABLE = 'logged_users';

app.set('views', '../../views'); //path 설정
app.set('view engine', 'ejs'); //엔진 정의
app.engine('html', require('ejs').renderFile); //엔진 사용

let usersAuthData = [];
let userId = 'unknown';

function getUserDb(table) {
	userDb.query(`SELECT * FROM ${table};`, function (error, auth_data) {
		if (error) {
			return console.log(error);
		}
		usersAuthData = auth_data;
	});
}
function signUp(id, pw) {
	userDb.query(
		`INSERT INTO ${AUTHDATA_TABLE} (id, pw, authority) VALUES ('${id}', '${pw}', 'user');`,
		function (error, auth_data) {
			if (error) {
				return console.log(error);
			}
		}
	);
	getUserDb(AUTHDATA_TABLE);
}
getUserDb(AUTHDATA_TABLE);

function insertLoggedUser(id, name) {
	userDb.query(
		`INSERT INTO ${LOGGEDUSERS_TABLE} (id, name) VALUES ('${id}', '${name}');`,
		function (error, logged_users) {
			if (error) {
				return console.log(error);
			}
		}
	);
}
function deleteLoggedUser(id) {
	userDb.query(
		`DELETE FROM ${LOGGEDUSERS_TABLE} WHERE id = '${id}';`,
		function (error, logged_users) {
			if (error) {
				return console.log(error);
			}
		}
	);
}
function nameLoggedUser(id) {
	userDb.query(
		`SELECT name FROM ${LOGGEDUSERS_TABLE} where id = '${id}';`,
		function (error, logged_users) {
			if (error) {
				console.log(error);
			}
			console.log(logged_users[0].name, 'name');
			userId = logged_users[0].name;
		}
	);
}

app.use(express.static(path.join('../../public')));

app.get('/', (req, res) => {
	res.render('index.html');
});

server.listen(PORT, () => {
	console.log(`server is running on ${PORT}`);
});

io.emit('some event', {
	someProperty: 'some value',
	otherProperty: 'other value',
});

io.on('connection', (socket) => {
	socket.on('login', (user) => {
		let resId = '';
		let auth = false;
		let i = 0;
		while (i < usersAuthData.length) {
			if (user.id === usersAuthData[i].id && user.pw === usersAuthData[i].pw) {
				resId = user.id;
				insertLoggedUser(socket.id, resId);
				io.emit('saveSocketId', socket.id);
				console.log(socket.id);
				auth = true;
				break;
			}
			i = i + 1;
		}
		const res = { id: resId, auth: auth };
		io.emit('login', res);
	});

	socket.on('signUp', (req) => {
		console.log('signing up');
		var { id, pw } = req;
		let unsigned = true;
		let i = 0;
		while (i < usersAuthData.length) {
			if (id === usersAuthData[i].id) {
				unsigned = false;
				break;
			}
			i = i + 1;
		}
		if (unsigned) {
			signUp(id, pw);
		}
		io.emit('signUp', unsigned);
		console.log('emited');
	});

	socket.on('connecting', (id) => {
		const date = new Date();
		const hours = String(date.getHours()).padStart(2, '0');
		const minutes = String(date.getMinutes()).padStart(2, '0');
		io.emit('greeting', `${id} logged in @[${hours}:${minutes}]`);
	});
	socket.on('resSocketId', (socketId) => {
		console.log(socketId);
		nameLoggedUser(socketId);
	});
	socket.on('chat message', (res) => {
		const msg = res.input;
		const socketId = res.socketId;
		nameLoggedUser(socketId);
		console.log(userId, 'chat message');
		console.log('message: ' + msg);
		const date = new Date();
		const hours = String(date.getHours()).padStart(2, '0');
		const minutes = String(date.getMinutes()).padStart(2, '0');
		const _msg = `#${userId}>> ${msg} @[${hours}:${minutes}]`;
		io.emit('chat message', _msg);
	});

	socket.on('disconnect', () => {
		console.log(`someone disconnected`);
	});
});
