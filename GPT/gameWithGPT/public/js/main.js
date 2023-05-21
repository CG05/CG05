const express = require('express');
const http = require('http');
const path = require('path');
const { Server } = require('socket.io');
const mysql = require('mysql');
const Character = require('./character.js');
const { Player } = require('./player.js');
const {Enemy, enemies} = require('./enemy.js');
const { Stats } = require('./stats.js');
const { Job, jobs } = require('./jobs.js');
const { Node, loadRoute, initRoutes, displayMap } = require('./map.js');

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
let onlinePlayers = new Map();

function getUserDb(table) {
	userDb.query(`SELECT * FROM ${table};`, function (error, auth_data) {
		if (error) {
			return console.log(error);
		}
		usersAuthData = auth_data;
	});
}

async function setPlayerOnline(name, player) {
	const _playerData = player.playerData;
	console.log('setting player online...');
	const playerInfo = _playerData.getCharacterInfo();
	const _enemyData = player.enemyData;
	const enemyInfo = _enemyData.getCharacterInfo();
	return new Promise((res, rej)=>{
		onlinePlayers.set(name, { playerData: playerInfo, mapData: player.mapData , enemyData: enemyInfo, stateData: player.stateData});
		res();
	});
}

function getPlayerInfo(name){
	const _playerOnline = onlinePlayers.get(name);
	const playerInfo = _playerOnline.playerData;
	return playerInfo;
}

function getPlayerMap(name){
	const _playerOnline = onlinePlayers.get(name);
	const playerMap = _playerOnline.mapData;
	return playerMap;
}

function getPlayerEnemy(name){
	const _playerOnline = onlinePlayers.get(name);
	const playerEnemy = _playerOnline.enemyData;
	return playerEnemy;
}

function getPlayerState(name){
	const _playerOnline = onlinePlayers.get(name);
	const playerState = _playerOnline.stateData;
	return playerState;
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
function playerSetting(name, info){
	const playerData = new Player(
		name,
		info.level,
		info.maxExp,
		info.exp,
		info.job,
		info.stats,
		info.skills,
		info.currentPosition,
		info.equipment
	);
	return playerData;
}

function enemySetting(info){
	const enemyData = new Enemy(
		info.name,
		info.level,
		info.type,
		info.rarity,
		info.job,
		info.stats,
		info.skills,
	);
	return enemyData;
}

async function initPlayerData(name) {
	const initStats = new Stats(50, 50, 5, 0, 0, 1);
	const listJobs = await jobs;
	const job = listJobs[0];
	const initialJob = new Job(job.name, job.skills, job.nextJob);
	const playerData = new Player(
		name,
		1,
		10,
		0,
		initialJob.name,
		initStats,
		initialJob.skills,
		{ route: 'Start', stage: 0 },
		{}
	);
	const mapData = mapping();
	const enemyData = new Enemy(undefined, undefined, undefined, undefined, undefined, undefined, undefined);
	await setPlayerOnline(name, { playerData: playerData, mapData: mapData , enemyData: enemyData, stateData: 'lull'});
	const info = JSON.stringify(playerData.getCharacterInfo());
	const map = JSON.stringify(mapData);
	const enemy = JSON.stringify(enemyData.getCharacterInfo());
	await new Promise((res, rej) => {
		userDb.query(`INSERT INTO ${PLAYER_DATA}(name, info, map, enemy, state) VALUES('${name}', '${info}', '${map}', '${enemy}', 'lull')`, (error, results) => {
			if (error) {
				console.log(error);
				rej(error);
			} else {
				console.log(`Player name ${name}: player init completed.`);
				res();
			}
		});
	});
	
}

async function saveData(name) {
	const info = JSON.stringify(getPlayerInfo(name));
	const mapData = getPlayerMap(name);
	const map = JSON.stringify(mapData);
	const enemy = JSON.stringify(getPlayerEnemy(name));
	const state = getPlayerState(name);

	const savingPlayerData = new Promise((res, rej) => {
		userDb.query(
			`UPDATE ${PLAYER_DATA} SET info='${info}', enemy='${enemy}', state='${state}', map='${map}' WHERE name='${name}'`,
			(error, results) => {
				if (error) {
					console.log(error);
					rej(error);
				} else {
					console.log(`Player name ${name}: player save completed.`);
					res();
				}
			});
	});
	
}

async function loadData(name) {
	let data = {info: undefined, enemy: undefined, state: undefined, map: undefined};
	let isLoadedPlayerData;
	let isLoadedEnemyData;
	let isLoadedStateData;
	let isLoadedMapData;
	const loadingPlayerData = new Promise((res, rej) => {
		userDb.query(`SELECT info FROM ${PLAYER_DATA} WHERE name='${name}'`, (error, results) => {
			if (error) {
				rej(error);
			} else if (results[0] !== undefined) {
				console.log(results[0].info);
				data.info =	JSON.parse(results[0].info)
				console.log(`Player name ${name}: player load completed.`);
				
				res(true);
			} else {
				res(false);
			}
		});
	});
	const loadingEnemyData = new Promise((res, rej) => {
		userDb.query(`SELECT enemy FROM ${PLAYER_DATA} WHERE name='${name}'`, (error, results) => {
			if (error) {
				rej(error);
			} else if (results[0] !== undefined) {
				data.enemy = JSON.parse(results[0].enemy);
				console.log(`Player name ${name}: enemy load completed.`);
	
				res(true);
			} else {
				res(false);
			}
		});
	});
	const loadingStateData = new Promise((res, rej) => {
		userDb.query(`SELECT state FROM ${PLAYER_DATA} WHERE name='${name}'`, (error, results) => {
			if (error) {
				rej(error);
			} else if (results[0] !== undefined) {
				data.state = results[0].state;
				console.log(`Player name ${name}: state load completed.`);
	
				res(true);
			} else {
				res(false);
			}
		});
	});
	const loadingMapData = new Promise((res, rej) => {
		userDb.query(`SELECT map FROM ${PLAYER_DATA} WHERE name='${name}'`, (error, results) => {
			if (error) {
				rej(error);
			} else if (results[0] !== undefined) {
				data.map = JSON.parse(results[0].map);
				console.log(`Player name ${name}: map load completed.`);
	
				res(true);
			} else {
				res(false);
			}
		});
	});
	isLoadedPlayerData = await loadingPlayerData;
	isLoadedEnemyData = await loadingEnemyData;
	isLoadedStateData = await loadingStateData;
	isLoadedMapData = await loadingMapData;
	if(isLoadedPlayerData && isLoadedMapData && isLoadedEnemyData && isLoadedStateData){
		await setPlayerOnline(name, {playerData: playerSetting(name, data.info), mapData: data.map, enemyData: enemySetting(data.enemy), stateData: data.state});
		return true;
	}else{
		console.log(`Load failed.\nNew Player name ${name}: player data initiating...`);
		await initPlayerData(name);
		return false;
	}
}



function mapping() {
	const routeA = loadRoute();
	const routeB = loadRoute();
	const routeC = loadRoute();
	const routes = initRoutes(routeA, routeB, routeC);

	return routes;
}

function mapRouteToIndex(route){
	let index;
	switch(route){
		case 'A':
			index = 0;
			break;
		case 'B':
			index = 1;
			break;
		case 'C':
			index = 2;
			break;
		default:
			console.log(`Wrong route value input: ${route}`);
			break;
	}
	return index;
}
function mapIndexToRoute(index){
	let route;
	switch(index){
		case 0:
			route = 'A';
			break;
		case 1:
			route = 'B';
			break;
		case 2:
			route = 'C';
			break;
		default:
			console.log(`Wrong index value input: ${index}`);
			break;
	}
	return route;
}


function sendStats(name){
	const playerData = playerSetting(name, getPlayerInfo(name));
	const playerInfo = playerData.getCharacterInfo();
	let _msg = `#Player Status`;
	io.emit('text', _msg);
	_msg = `name: ${name}`;
	io.emit('text', _msg);
	_msg = `level: ${playerInfo.level}`;
	io.emit('text', _msg);
	_msg = `exp: ${playerInfo.exp}/${playerInfo.maxExp}`;
	io.emit('text', _msg);
	_msg = `hp: ${playerInfo.stats.currentHp}/${
		playerInfo.stats.maxHp
	}`;
	io.emit('text', _msg);
	_msg = `attackPoint: ${playerInfo.stats.attackPoint}`;
	io.emit('text', _msg);
	const playerPosition = playerData.currentPosition;
	const playerRoute = playerPosition.route;
	const playerStage = playerPosition.stage;
	_msg = `currentPosition: Route${playerRoute}: Stage -${playerStage}-`;
	io.emit('text', _msg);

}

function sendChoices(name){
	const playerData = playerSetting(name, getPlayerInfo(name));
	const playerInfo = playerData.getCharacterInfo();
	const mapData = getPlayerMap(name);
	let _msg = '';
	
	const routeA = mapData[0];
	const routeB = mapData[1];
	const routeC = mapData[2];
	
	const playerPosition = playerData.currentPosition;
	const playerRoute = playerPosition.route;
	const playerStage = playerPosition.stage;
	let _choices;
	let isBranch = false;
	switch(playerRoute){
		case 'Start':
			_msg = `Next Route: A-1, B-1, C-1`;
			_choices = [`A`, `B`, `C`];
			break;
		case 'A':
			isBranch = routeA[playerStage].branch && routeB[playerStage + 1].branch;
			if(isBranch){
				_msg = `Next Route: A-${playerStage + 1}, B-${playerStage + 1}`;
				_choices = [`A`,`B`];
			}else{
				_msg = `Next Route: A-${playerStage + 1}`;
				_choices = [`A`];
			}
			break;
		case 'B':
			let BAisBranched = routeA[playerStage + 1].branch && routeB[playerStage].branch;
			let BCisBranched = routeB[playerStage].branch && routeC[playerStage + 1].branch;
			if(!(BAisBranched && BCisBranched)){
				_msg = `Next Route: B-${playerStage + 1}`;
				_choices = [`B`];
			}else if(BAisBranched){
				_msg = `Next Route: A-${playerStage + 1}, B-${playerStage + 1}`;
				_choices = [`A`, `B`];
			}else if(BCisBranched){
				_msg = `Next Route: B-${playerStage + 1}, C-${playerStage + 1}`;
				_choices = [`B`, `C`];
			}else{
				console.log(`Branch Error Occured: B-${playerStage}`);
			}
			break;
		case 'C':
			isBranch = false;
			isBranch = routeC[playerStage].branch && routeB[playerStage + 1].branch;
			if(isBranch){
				_msg = `Next Route: B-${playerStage + 1}, C-${playerStage + 1}`;
				_choices = [`B`, `C`];
			}else{
				_msg = `Next Route: C-${playerStage + 1}`;
				_choices = [`C`];
			}
			break;
		default:
			console.log(`Route Error Occured`);
			break;
	}
	io.emit('choices', {msg: _msg, choices: _choices});
}

function sendStatsWithChoices(name) {
	sendStats(name);
	sendChoices(name);
	
	const _msg = `What do you wanna do? Need some help, command "/help" will give you some advice.`;
	io.emit('next respond ', {msg: _msg, type: 'lull'});
}

function processCommand(name, command){
	
}

async function goAhead(playerData, choice){
	const _playerData = new Promise((res, rej)=>{
		const playerPosition = playerData.currentPosition;
		const currentRoute = choice;
		const currentStage = playerPosition.stage + 1;
		playerData.currentPosition = {route: currentRoute, stage: currentStage};
		res(playerData);
	})
	return _playerData;
}

async function processChoice(name, choice){
	let playerData = playerSetting(name, getPlayerInfo(name));
	const mapData = getPlayerMap(name);
	const playerPosition = playerData.currentPosition;
	const currentRoute = choice;
	const currentStage = playerPosition.stage + 1;
	playerData = await goAhead(playerData, choice);
	const playerInfo = playerData.getCharacterInfo();
	playerData.setCharacterInfo(playerInfo);
	const type = mapData[mapRouteToIndex(currentRoute)][currentStage].type;
	await setPlayerOnline(name, {playerData: playerData, mapData: mapData, enemyData: enemySetting(getPlayerEnemy(name)), stateData: type});
	const _msg = `${currentRoute}-${currentStage} => ${type} encountered.`;
	io.emit('next respond', {msg: _msg, type: type});
}

function processCombat(name, controll){
	const playerData = playerSetting(name, getPlayerInfo(name));
	const playerInfo = playerData.getCharacterInfo();
	const skills = playerInfo.skills;
	const result = {finish: false, effects: {}, reward: []};
	if(result.finish){
		io.emit('combat result', result.reward);
	}else{
		sendStats(name);
		sendEnemyStats(name);
		io.emit('combat', result.effects);
	}
}

async function startCombat(name){
	const enemyList = await enemies;
	const enemyData = enemyList[0];
	console.log(enemyData.getCharacterInfo());
	const playerData = playerSetting(name, getPlayerInfo(name));
	await setPlayerOnline(name,{playerData: playerData, mapData: getPlayerMap(name), enemyData: enemyData, stateData: getPlayerState(name)})
	sendEnemyStats(name);
	
	const playerInfo = playerData.getCharacterInfo();
	const skills = playerInfo.skills;

	let choices = ['defaultAttack'];
	for(const skill of skills){
		choices.push(skill.name);
	}
	io.emit('combat', "Player can choice under:");
	let i = 1;
	for(const choice of choices){
		io.emit('combat', `${i}. ${choice}`);
		io.emit('combat choices', {choice: choice, num: i});
		i++;
	}
	
}

function sendEnemyStats(name){
	const enemyData = enemySetting(getPlayerEnemy(name));
	const enemyInfo = enemyData.getCharacterInfo();
	let _msg = `#Enemy Status`;
	io.emit('text', _msg);
	_msg = `name: ${name}`;
	io.emit('text', _msg);
	_msg = `level: ${enemyInfo.level}`;
	io.emit('text', _msg);
	_msg = `hp: ${enemyInfo.stats.currentHp}/${enemyInfo.stats.maxHp}`;
	io.emit('text', _msg);
}

function processDecision(name, type, decision){
	
}


//Socket Server Boundary
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
		console.log(`${name} is connecting to server...`);
		let newbie = true;
		await loadData(name);
	
		io.emit('greeting', {
			name: name,
			greeting: `Welcome, ${name}. Wanna start game, Please enter "start".`,
		});
	});
	
	socket.on('memorizing user name', (name) => {
		const socketId = socket.id;
		updateUser(name, socket.id);
	});

	socket.on('start', async (res) => {
		const socketId = socket.id;
		const name = await userName(socketId);
		console.log(`${name}: ${socketId} >> ${res}`);
		const map = getPlayerMap(name);
		displayMap(map);
			
		await sendStatsWithChoices(name);
	});
	
	socket.on('command', async (command) =>{
		const socketId = socket.id;
		const name = await userName(socketId);
		console.log(`command recieved from ${name}: ${command}`);
		//데이터베이스에서 command에 대한 결과를 result에 담기
		const result = await processCommand(command);
		await saveData(name);
		await sendStatsWithChoices(name);
		io.emit('result', result);
	});
	
	socket.on('choice', async (choice) => {
		const socketId = socket.id;
		const name = await userName(socketId);
		console.log(`choice recieved from ${name}: ${choice}`);
		
		const result = await processChoice(name, choice);
		await saveData(name);
		io.emit('result', result);
	});
	
	socket.on('combat encounter', async (res) => {
		const socketId = socket.id;
		const name = await userName(socketId);
		console.log(`combat encounter recieved from ${name}`);
		
		await startCombat(name);
		await saveData(name);
	});
	
	socket.on('combat', async (controll) => {
		const socketId = socket.id;
		const name = await userName(socketId);
		console.log(`controll for combat recieved from ${name}: ${controll}`);
		
		await processCombat(controll);
		await saveData(name);
	});
	
	socket.on('decision', async (res) => {
		const type = res.type;
		const decision = res.decision;
		const socketId = socket.id;
		const name = await userName(socketId);
		console.log(`decision for ${type} recieved from ${name}: ${decision}`);
		
		const result = await processDecision(type, decision);
		await saveData(name);
		io.emit('result', result);
	});
	
	
	
	socket.on('next request', async (res) =>{
		//데이터베이스에서 현재 상태, 다음 선택지를 respond에 담기
		const socketId = socket.id;
		const name = await userName(socketId);
		await loadData(name);
		await sendStatsWithChoices(name);
	});

	
	socket.on('disconnect', async (res) => {
		const socketId = socket.id;
		const name = await userName(socketId);
		console.log(`${name} disconnected`);
		deleteLoggedUser(socketId);
	});
});