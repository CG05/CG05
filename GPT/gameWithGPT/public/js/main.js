const express = require('express');
const http = require('http');
const path = require('path');
const { Server } = require('socket.io');
const mysql = require('mysql');
const Character = require('./character.js');
const { Player } = require('./player.js');
const { Stats } = require('./stats.js');
const { Job, jobs } = require('./jobs.js');

const app = express();
const PORT = 3000;
const server = http.createServer(app);
const io = new Server(server);
const userDb = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: 'Pomcom1123@',
	database: 'Users',
	port: '3306',
});
const AUTHDATA_TABLE = 'auth_data';
const LOGGEDUSERS_TABLE = 'logged_users';
const PLAYER_DATA = 'player_data';

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

// 유저 정보를 찾는 함수
async function userName(socketId) {
	return new Promise((res, rej) => {
		userDb.query(
			`SELECT name FROM ${LOGGEDUSERS_TABLE} WHERE socket_id = '${socketId}';`,
			(error, results) => {
				if (error) {
					console.log(error);
					rej(undefined);
				} else {
					const name = results[0] && results[0].name;
					console.log(`${socketId}: ${name}`);
					res(name);
				}
			}
		);
	});
}

// 유저 정보를 업데이트하는 함수
function updateUser(name, socketId) {
	const user = { name: name, socket_id: socketId };
	userDb.query(
		`INSERT INTO ${LOGGEDUSERS_TABLE} SET ? ON DUPLICATE KEY UPDATE socket_id='${socketId}';`,
		user,
		(error) => {
			if (error) {
				console.log(error);
			} else {
				console.log(`Updated socket ID for user ${name}: ${socketId}`);
			}
		}
	);
}

async function deleteLoggedUser(socketId) {
	const name = await userName(socketId);
	userDb.query(
		`DELETE FROM ${LOGGEDUSERS_TABLE} WHERE socket_id = '${socketId}';`,
		(error, results) => {
			if (error) {
				console.log(error);
			} else {
				console.log(`${name}: ${socketId} has deleted.`);
			}
		}
	);
}
async function isNamedPlayer(name){
	return new Promise((res, rej) => {
		
	});
}

function initPlayerData(name) {
	userDb.query(`INSERT INTO ${PLAYER_DATA} VALUES ('${name}', '{}')`, (error, results) => {
		if (error) {
			console.log(error);
		} else {
			console.log(`Player name ${name}: init completed.`);
		}
	});
}

async function savePlayerData(name) {
	const playerData = player.getCharacterInfo();
	const data = JSON.stringify(playerData);
	userDb.query(
		`UPDATE ${PLAYER_DATA} SET info='${data}' WHERE name='${name}'`,
		(error, results) => {
			if (error) {
				console.log(error);
			} else {
				console.log(`Player name ${name}: save completed.`);
			}
		}
	);
}

async function loadPlayerData(name) {
	let data = {};
	return new Promise((res, rej) => {
		userDb.query(`SELECT info FROM ${PLAYER_DATA} WHERE name='${name}'`, (error, results) => {
			if (error) {
				rej(error);
			} else if(results[0] !== undefined){
				data = JSON.parse(results[0]);
				console.log(`Player name ${name}: load completed.`);
				updatePlayerData(data);
				res(true);
			}
			else{
				console.log(`Load failed.\nNew Player name ${name}: initiating...`);
				res(false);
			}
		});
	});
}

function updatePlayerData(playerData) {
	player.setCharacterData(playerData);
}

async function sendPlayerInfo(socketId){
	const name = await userName(socketId);
			await savePlayerData(name);
			console.log(`${name}: ${socketId} >> ${msg}`);
			const _msg = `
							#Player Status\n
							name: ${player.name}\n
							level: ${player.getCharacterInfo().level}\n
							exp: ${player.getCharacterInfo().expPercent}\n
							hp: ${player.getCharacterInfo().stats.currentHp}/${player.getCharacterInfo().stats.maxHp}\n
							attackPoint: ${player.getCharacterInfo().stats.attackPoint}\n
							What do you wanna do? Need some help, command "/help" will give you some advice.
							`;
			io.emit('chat message', _msg);
}

const initStats = new Stats(50, 50, 5, 0, 0, 1);
const initialJob = new Job(jobs[1]);
const player = new Player(
	'unknown',
	1,
	10,
	0,
	initialJob.name,
	initStats,
	[0, 0],
	initialJob.skills,
	{}
);

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

	socket.on('connecting', async (name) => {
		let newbie = true;
		const data = await loadPlayerData(name);
		if(data){
			newbie = false;
		}else{
			player.name = name;
			initPlayerData(name);
		}

		io.emit('greeting', {
			name: name,
			greeting: `Welcome, ${name}. Wanna start game, Please enter "start".`,
			newbie: newbie
		});
	});

	/**socket.on('nextRequest', (req) =>{
		//데이터베이스에서 현재 상태, 다음 선택지를 respond에 담기
			io.emit('nextRespond', respond);
		}*/

	/**socket.on('choice', (choice) =>{
		//데이터베이스에서 choice에 대한 결과를 result에 담기
			io.emit('result',result);
		}*/

	socket.on('chat message', async (res) => {
		console.log(res);
		const msg = res.msg;
		const socketId = socket.id;
		if (res.msg === 'memorizing user name...') {
			updateUser(res.name, socket.id);
		} else if(res.msg === 'start'){
			await sendPlayerInfo(socketId);
		}else{
			const _msg = 'Wrong input. Please try again.'
			io.emit('chat message', _msg);
			await sendPlayerInfo(socketId);
		}
	});
	
	socket.on('disconnect', async () => {
		const socketId = socket.id;
		const name = await userName(socketId);
		console.log(`${name} disconnected`);
		deleteLoggedUser(socketId);
	});
});