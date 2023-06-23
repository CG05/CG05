const express = require('express');
const http = require('http');
const path = require('path');
const { Server } = require('socket.io');
const mysql = require('mysql');
const { Character } = require('./character.js');
const playerModule = require('./player.js');
const Player = playerModule.Player;
const { Enemy, enemies } = require('./enemy.js');
const { Stats } = require('./stats.js');
const { Job, jobs } = require('./jobs.js');
const { Node, loadRoute, initRoutes, displayMap } = require('./map.js');
const { Item, Items, BossItems } = require('./item.js');
const { Equips } = require('./equips.js');

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
	console.log('setting player online...');
	return new Promise((res, rej) => {
		onlinePlayers.set(name, {
			playerInfo: player.playerInfo,
			mapData: player.mapData,
			enemyInfo: player.enemyInfo,
			stateData: player.stateData,
		});
		res();
	});
}

async function getPlayerInfo(name) {
	const _playerOnline = () => {
		return new Promise((res, rej) => {
			res(onlinePlayers.get(name));
		});
	};
	return _playerOnline().then((p) => {
		return p.playerInfo;
	});
}

async function getPlayerMap(name) {
	const _playerOnline = () => {
		return new Promise((res, rej) => {
			res(onlinePlayers.get(name));
		});
	};
	return _playerOnline().then((p) => {
		return p.mapData;
	});
}

async function getPlayerEnemy(name) {
	const _playerOnline = () => {
		return new Promise((res, rej) => {
			res(onlinePlayers.get(name));
		});
	};
	return _playerOnline().then((p) => {
		return p.enemyInfo;
	});
}

async function getPlayerState(name) {
	const _playerOnline = () => {
		return new Promise((res, rej) => {
			res(onlinePlayers.get(name));
		});
	};
	return _playerOnline().then((p) => {
		return p.stateData;
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

// // 유저 정보를 찾는 함수
// async function userName(socketId) {
// 	return new Promise((res, rej) => {
// 		userDb.query(
// 			`SELECT name FROM ${LOGGEDUSERS_TABLE} WHERE socket_id = '${socketId}';`,
// 			(error, results) => {
// 				if (error) {
// 					console.log(error);
// 					rej(undefined);
// 				} else {
// 					const name = results[0] && results[0].name;
// 					console.log(`${socketId}: ${name}`);
// 					res(name);
// 				}
// 			}
// 		);
// 	});
// }

// // 유저 정보를 업데이트하는 함수
// function updateUser(name, socketId) {
// 	if (name !== null || name !== undefined) {
// 		return new Promise((res, rej) => {
// 			const user = { name: name, socket_id: socketId };
// 			userDb.query(
// 				`INSERT INTO ${LOGGEDUSERS_TABLE} SET ? ON DUPLICATE KEY UPDATE socket_id='${socketId}';`,
// 				user,
// 				(error) => {
// 					if (error) {
// 						rej(error);
// 					} else {
// 						console.log(`Updated socket ID for user ${name}: ${socketId}`);
// 						res();
// 					}
// 				}
// 			);
// 		});
// 	} else {
// 		const getSocketId = new Promise((res, rej) => {
// 			userDb.query(`SELECT socket_id FROM ${name};`, (error, results) => {
// 				if (error) {
// 					rej(error);
// 				} else {
// 					res(results[0]);
// 				}
// 			});
// 		});
// 		return getSocketId.then((savedSocket_id) => {
// 			if (savedSocket_id !== socketId) {
// 				const user = { name: name, socket_id: socketId };
// 				return new Promise((res, rej) => {
// 					const user = { name: name, socket_id: socketId };
// 					userDb.query(
// 						`INSERT INTO ${LOGGEDUSERS_TABLE} SET ? ON DUPLICATE KEY UPDATE socket_id='${socketId}';`,
// 						user,
// 						(error) => {
// 							if (error) {
// 								rej(error);
// 							} else {
// 								console.log(`Updated socket ID for user ${name}: ${socketId}`);
// 								res();
// 							}
// 						}
// 					);
// 				});
// 			}else{
// 				return;
// 			}
// 		});
// 	}
// }

// async function deleteLoggedUser(socketId) {
// 	const name = await userName(socketId);
// 	userDb.query(
// 		`DELETE FROM ${LOGGEDUSERS_TABLE} WHERE socket_id = '${socketId}';`,
// 		(error, results) => {
// 			if (error) {
// 				console.log(error);
// 			} else {
// 				console.log(`${name}: ${socketId} has deleted.`);
// 			}
// 		}
// 	);
// }

async function playerSetting(info) {
	const equips = new Equips(info.equipments);
	const setting = () => {
		return new Player(
			info.name,
			info.level,
			info.maxExp,
			info.exp,
			info.job,
			info.stats,
			info.skills,
			info.currentPosition,
			info.items,
			equips,
			info.gold,
			info.shopCount,
			info.needMoveOn,
			info.focusItem
		);
	};
	const playerData = setting();
	await playerData.mergeStat();
	return playerData;
}

function enemySetting(info) {
	const enemyData = () => {
		return new Enemy(
			info.name,
			info.level,
			info.type,
			info.rarity,
			info.job,
			info.stats,
			info.skills
		);
	};
	return enemyData();
}

async function initPlayerData(name) {
	const initStats = new Stats(80, 80, 10, 0, 0, 1, 0.01, 1.5);
	const listJobs = await jobs;
	const job = listJobs[0];
	const initialJob = new Job(job.name, job.comment, job.line, job.skills, job.nextJob);
	const equipSetting = new Equips([
		['무기', { name: 'undefined', type: '무기', set: '' }],
		['모자', { name: 'undefined', type: '모자', set: '' }],
		['상의', { name: 'undefined', type: '상의', set: '' }],
		['하의', { name: 'undefined', type: '하의', set: '' }],
		['신발', { name: 'undefined', type: '신발', set: '' }],
	]);
	const playerData = new Player(
		name,
		1,
		10,
		0,
		initialJob,
		initStats,
		initialJob.skills,
		{ floor: 1, route: 'Start', stage: 0 },
		[{ name: 'potion' }],
		equipSetting,
		0,
		1,
		false,
		{}
	);
	await playerData.mergeStat();
	const enemyData = new Enemy(
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined
	);
	const playerInfo = playerData.getCharacterInfo();
	const mapData = await mapping(1);
	const enemyInfo = enemyData.getCharacterInfo();
	const stateData = 'lull';
	await setPlayerOnline(name, {
		playerInfo: playerInfo,
		mapData: mapData,
		enemyInfo: enemyData,
		stateData: stateData,
	});
	const infoJSON = JSON.stringify(playerInfo);
	const mapJSON = JSON.stringify(mapData);
	const enemyJSON = JSON.stringify(enemyInfo);
	const state = stateData;
	await new Promise((res, rej) => {
		userDb.query(
			`INSERT INTO ${PLAYER_DATA}(name, info, map, enemy, state) VALUES('${name}', '${infoJSON}', '${mapJSON}', '${enemyJSON}', '${state}')`,
			(error, results) => {
				if (error) {
					console.log(error);
					rej(error);
				} else {
					console.log(`Player name ${name}: player init completed.`);
					res();
				}
			}
		);
	});
}

async function saveData(name) {
	const info = JSON.stringify(await getPlayerInfo(name));
	const mapData = await getPlayerMap(name);
	const map = JSON.stringify(mapData);
	const enemy = JSON.stringify(await getPlayerEnemy(name));
	const state = await getPlayerState(name);
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
			}
		);
	});
}

async function loadData(name) {
	let data = { info: undefined, enemy: undefined, state: undefined, map: undefined };
	let isLoadedPlayerData;
	let isLoadedEnemyData;
	let isLoadedStateData;
	let isLoadedMapData;
	const loadingPlayerData = new Promise((res, rej) => {
		userDb.query(`SELECT info FROM ${PLAYER_DATA} WHERE name='${name}'`, (error, results) => {
			if (error) {
				rej(error);
			} else if (results[0] !== undefined) {
				const result = results[0];
				const info = JSON.parse(result.info);
				data.info = info;

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
	if (isLoadedPlayerData && isLoadedMapData && isLoadedEnemyData && isLoadedStateData) {
		await setPlayerOnline(name, {
			playerInfo: data.info,
			mapData: data.map,
			enemyInfo: data.enemy,
			stateData: data.state,
		});
		return true;
	} else {
		console.log(`Load failed.\nNew Player name ${name}: player data initiating...`);
		await initPlayerData(name);
		return false;
	}
}

async function mapping(floor) {
	const routeA = await loadRoute(floor);
	const routeB = await loadRoute(floor);
	const routeC = await loadRoute(floor);
	const routes = await initRoutes(routeA, routeB, routeC);

	return routes;
}

function mapRouteToIndex(route) {
	let index;
	switch (route) {
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
function mapIndexToRoute(index) {
	let route;
	switch (index) {
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

function emitText(type, msg) {
	io.emit('text', { msg: msg, type: type });
}
function emitStats(name) {
	const stats = getPlayerInfo(name);
}

async function sendStats(name) {
	const info = await getPlayerInfo(name);
	io.emit('info', { whose: name, info: info });
}

async function sendChoices(name) {
	const playerInfo = await getPlayerInfo(name);
	const playerData = await playerSetting(playerInfo);
	const mapData = await getPlayerMap(name);
	let _msg = '';

	const routeA = mapData[0];
	const routeB = mapData[1];
	const routeC = mapData[2];

	const playerPosition = playerData.currentPosition;
	const playerFloor = playerPosition.floor;
	const playerRoute = playerPosition.route;
	const playerStage = playerPosition.stage;
	let _choices;
	let isBranch = false;
	_msg = `currentPosition: F${playerFloor}-Route${playerRoute}: Stage -${playerStage}-`;
	emitText('text', _msg);
	switch (playerRoute) {
		case 'Start':
			_msg = `다음 행선지: A-1(Enter A), B-1(Enter B), C-1(Enter C)`;
			_choices = [`A`, `B`, `C`];
			break;
		case 'A':
			isBranch = false;
			if (playerStage < 12) {
				isBranch = routeA[playerStage].branch && routeB[playerStage + 1].branch;
				if (isBranch) {
					_msg = `다음 행선지: A-${playerStage + 1}, B-${playerStage + 1}`;
					_choices = [`A`, `B`];
				} else {
					_msg = `다음 행선지: A-${playerStage + 1}`;
					_choices = [`A`];
				}
			} else if (playerStage === 12) {
				_msg = `다음 행선지: A-${playerStage + 1}`;
				_choices = [`A`];
			} else {
				_msg = `다음 행선지: Floor${playerFloor + 1}(Enter F)`;
				_choices = [`F`];
			}

			break;
		case 'B':
			let BAisBranched = false;
			let BCisBranched = false;
			if (playerStage < 12) {
				BAisBranched = routeA[playerStage + 1].branch && routeB[playerStage].branch;
				BCisBranched = routeB[playerStage].branch && routeC[playerStage + 1].branch;
				if (!(BAisBranched && BCisBranched)) {
					_msg = `다음 행선지: B-${playerStage + 1}`;
					_choices = [`B`];
				} else if (BAisBranched) {
					_msg = `다음 행선지: A-${playerStage + 1}, B-${playerStage + 1}`;
					_choices = [`A`, `B`];
				} else if (BCisBranched) {
					_msg = `다음 행선지: B-${playerStage + 1}, C-${playerStage + 1}`;
					_choices = [`B`, `C`];
				} else {
					console.log(`Branch Error Occured: B-${playerStage}`);
				}
			} else if (playerStage === 12) {
				_msg = `다음 행선지: C-${playerStage + 1}`;
				_choices = [`C`];
			} else {
				_msg = `다음 행선지: B-${playerStage + 1}`;
				_choices = [`B`];
			}

			break;
		case 'C':
			isBranch = false;
			if (playerStage < 12) {
				isBranch = routeC[playerStage].branch && routeB[playerStage + 1].branch;
				if (isBranch) {
					_msg = `다음 행선지: B-${playerStage + 1}, C-${playerStage + 1}`;
					_choices = [`B`, `C`];
				} else {
					_msg = `다음 행선지: C-${playerStage + 1}`;
					_choices = [`C`];
				}
			} else if (playerStage === 12) {
				_msg = `다음 행선지: C-${playerStage + 1}`;
				_choices = [`C`];
			} else {
				_msg = `다음 행선지: Floor${playerFloor + 1}(Enter F)`;
				_choices = [`F`];
			}

			break;
		default:
			console.log(`Route Error Occured`);
			break;
	}
	io.emit('choices', { msg: _msg, choices: _choices });
}

async function sendStatsWithChoices(name) {
	emitText(
		'text',
		'=================================================================================='
	);
	await sendStats(name);
	await sendChoices(name);
	await sendLullRespond(name);
}

async function moveOnSequence(name) {
	const playerInfo = await getPlayerInfo(name);
	const playerData = await playerSetting(playerInfo);

	const playerJob = playerInfo.job;
	const listJobs = await jobs;
	const playerNextJob = () => {
		let listNextJob = [];
		for (const listjob of listJobs) {
			for (const jobName of playerJob.nextJob) {
				if (listjob.name === jobName) {
					listNextJob.push(listjob);
				}
			}
		}
		return listNextJob;
	};

	let _msg = `당신은 전직 조건을 충족하여 다음 직업으로 전직할 수 있습니다. 어떤 직업을 선택하시겠습니까?`;
	io.emit('next respond', { msg: _msg, type: 'moveOn' });
	let i = 1;

	for (const job of playerNextJob()) {
		_msg = `${i}. [${job.name}]:`;
		if (job.name === job.line) {
			_msg = _msg + ` ${job.comment} //`;
		} else {
			for (const skill of job.skills) {
				_msg = _msg + ` ${skill.name}-${skill.effect} //`;
			}
		}

		emitText('text', _msg);
		io.emit('move on choices', { num: i, choice: job.name });
		i++;
	}

	emitText(
		'text',
		'=================================================================================='
	);
}

async function moveOn(name, nextJobName) {
	const playerInfo = await getPlayerInfo(name);
	const playerData = await playerSetting(playerInfo);

	const listJobs = await jobs;
	const nextJob = () => {
		for (const job of listJobs) {
			if (job.name === nextJobName) {
				return job;
			}
		}
	};
	playerData.changeJob(nextJob());
	playerData.needMoveOn = false;
	await setPlayerOnline(name, {
		playerInfo: playerData.getCharacterInfo(),
		mapData: await getPlayerMap(name),
		enemyInfo: await getPlayerEnemy(name),
		stateData: await getPlayerState(name),
	});

	emitText('text', `축하합니다, [${nextJobName}](으)로 전직이 완료되었습니다.`);

	emitText(
		'text',
		'=================================================================================='
	);

	await sendStatsWithChoices(name);
}

async function sendLullRespond(name) {
	const playerInfo = await getPlayerInfo(name);
	const playerData = await playerSetting(playerInfo);

	if (playerInfo.needMoveOn) {
		moveOnSequence(name);
	} else {
		const _msg = `다음으로 이동하고 싶다면 행선지의 이니셜을 입력하시오. 입력 가능한 커맨드 => [/help, /stats, /skills, /items, /equips, /shop]`;
		io.emit('next respond', { msg: _msg, type: 'lull' });
		emitText(
			'text',
			'=================================================================================='
		);
	}
	await setPlayerOnline(name, {
		playerInfo: await getPlayerInfo(name),
		mapData: await getPlayerMap(name),
		enemyInfo: await getPlayerEnemy(name),
		stateData: 'lull',
	});
}

async function processCommand(name, command) {
	console.log(command);
	const playerInfo = await getPlayerInfo(name);
	const playerData = await playerSetting(playerInfo);

	const playerStats = playerInfo.stats;
	const playerSkills = playerInfo.skills;
	const playerItems = playerInfo.items;
	const playerEquipments = new Equips(playerInfo.equipments);
	let _msg;
	let i;
	// help, stats, skills, items, equips
	switch (command) {
		case '/help':
			emitText(
				'text',
				'+++++++++++++++++++++++++++++++++++++/ Help /+++++++++++++++++++++++++++++++++++++'
			);
			_msg = 'command list:';
			emitText('text', _msg);
			_msg = '/stats - 플레이어의 상세 스탯을 출력합니다.';
			emitText('text', _msg);
			_msg =
				'/skills - 플레이어의 스킬들을 출력합니다. 번호를 누르면 해당 스킬의 상세 스탯을 출력합니다.';
			emitText('text', _msg);
			_msg =
				'/items - 플레이어가 보유한 아이템들을 출력합니다. 번호를 누르면 판매 또는 장착할 수 있습니다.';
			emitText('text', _msg);
			_msg =
				'/equips - 플레이어가 장착한 아이템들을 출력합니다. 번호를 누르면 해제 및 판매할 수 있습니다.';
			emitText('text', _msg);
			_msg =
				'/shop - 상점에 진입합니다. 번호를 누르면 골드를 소비하여 구매할 수 있습니다. Floor당 1회만 가능합니다.';
			emitText('text', _msg);
			emitText(
				'text',
				'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
			);
			await switchState(name);
			break;
		case '/stats': //maxHp, currentHp, attackPoint, deffense, deffensePierce, damageAmplify
			emitText(
				'text',
				'+++++++++++++++++++++++++++++++++++++/ Stats /++++++++++++++++++++++++++++++++++++'
			);
			_msg = `최대체력: ${playerStats.maxHp}`;
			emitText('text', _msg);
			_msg = `공격력: ${playerStats.attackPoint}`;
			emitText('text', _msg);
			_msg = `방어력: ${playerStats.deffense}`;
			emitText('text', _msg);
			_msg = `방어관통력: ${playerStats.deffensePierce}`;
			emitText('text', _msg);
			_msg = `데미지증폭: ${playerStats.damageAmplify * 100}%`;
			emitText('text', _msg);
			_msg = `치명타확률: ${playerStats.criticalChance * 100}%`;
			emitText('text', _msg);
			_msg = `치명타데미지: ${playerStats.criticalDamage * 100}%`;
			emitText('text', _msg);
			emitText(
				'text',
				'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
			);
			await switchState(name);

			break;
		case '/skills': //name,	level, effect, increasePerLevel, damageFactor, attackTimes, cooltime
			i = 0;
			emitText(
				'text',
				'+++++++++++++++++++++++++++++++++++++/ Skills /+++++++++++++++++++++++++++++++++++'
			);
			io.emit('command choices', { num: i, choice: 'exit' });
			for (const skill of playerSkills) {
				i++;
				_msg = `${i}. [${skill.name}]`;
				emitText('text', _msg);
				io.emit('command choices', { num: i, choice: skill.name });
			}
			emitText('text', '0. exit');
			emitText(
				'text',
				'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
			);

			io.emit('next respond', { msg: undefined, type: 'skills' });
			break;
		case '/items':
			i = 0;
			emitText(
				'text',
				'+++++++++++++++++++++++++++++++++++++/ Items /++++++++++++++++++++++++++++++++++++'
			);
			io.emit('command choices', { num: i, choice: 'exit' });
			for (const item of playerItems) {
				i++;
				if (item.name !== 'potion') {
					_msg = `${i}. <${item.name}(${item.job})>(${item.rarity})-${item.type} {attackPoint: ${item.stats.attackPoint}, maxHp: ${item.stats.maxHp}, deffense: ${item.stats.deffense}}`;
				} else {
					_msg = `${i}. <${item.name}> 30% maxHp 회복`;
				}

				emitText('text', _msg);
				io.emit('command choices', { num: i, choice: item.name });
			}
			if (i === 0) {
				_msg = `보유한 아이템이 없습니다.`;
				emitText('text', _msg);
			}

			emitText('text', '0. exit');
			emitText(
				'text',
				'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
			);

			io.emit('next respond', { msg: undefined, type: 'items' });
			break;
		case '/equips':
			i = 0;
			emitText(
				'text',
				'+++++++++++++++++++++++++++++++++++++/ Equips /+++++++++++++++++++++++++++++++++++'
			);

			io.emit('command choices', { num: i, choice: 'exit' });
			playerEquipments.forEach((equip, key) => {
				if (equip.name !== 'undefined') {
					i++;
					_msg = `${i}. ${key} - <${equip.name}(${equip.job})>(${equip.rarity}) {attackPoint: ${equip.stats.attackPoint}, maxHp: ${equip.stats.maxHp}, deffense: ${equip.stats.deffense}}`;
					emitText('text', _msg);
					io.emit('command choices', { num: i, choice: equip.name });
				}
			});
			if (i === 0) {
				_msg = `장착된 아이템이 없습니다.`;
				emitText('text', _msg);
			}
			emitText('text', '0. exit');
			emitText(
				'text',
				'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
			);

			io.emit('next respond', { msg: undefined, type: 'equips' });
			break;
		case '/shop':
			await renderShop(name);
			emitText(
				'text',
				'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
			);

			io.emit('next respond', { msg: undefined, type: 'shop' });
			break;
		default:
			console.log('command error occured');
			break;
	}
}

async function renderShop(name) {
	const playerInfo = await getPlayerInfo(name);
	const playerData = await playerSetting(playerInfo);
	const playerFloor = playerInfo.currentPosition.floor;
	if (playerInfo.shopCount === 0) {
		io.emit('next respond', { msg: `더이상 상점을 이용할 수 없습니다.`, type: 'lull' });
		sendStatsWithChoices(name);
	} else {
		const itemList = await Items;
		const normal = itemList.filter((e) => e.rarity === '일반');
		const rare = itemList.filter((e) => e.rarity === '희귀');
		const epic = itemList.filter((e) => e.rarity === '영웅');

		let myJobItem = [];
		let option = (length) => {
			return Math.floor(Math.random() * length);
		};
		const setSales = new Promise(async (res, rej) => {
			async function endWhile() {
				let i = 0;
				let _sales = [];
				let pickItem;
				while (i < 5) {
					switch (playerFloor) {
						case 1:
							pickItem = new Promise((response, reject) => {
								let item;
								item = normal[option(normal.length)];
								response(item);
							});
							break;
						case 2:
							pickItem = new Promise((response, reject) => {
								let item;
								myJobItem = normal.filter((e) => e.job === playerInfo.jobline);
								if (Math.random() < 0.3) {
									item = myJobItem[option(myJobItem.length)];
								} else {
									item = rare[option(normal.length)];
								}
								response(item);
							});
							break;
						case 3:
							pickItem = new Promise((response, reject) => {
								let item;
								myJobItem = rare.filter((e) => e.job === playerInfo.jobline);
								if (Math.random() > 0.5) {
									item = myJobItem[option(myJobItem.length)];
								} else {
									item = rare[option(rare.length)];
								}
								response(item);
							});
							break;
						case 4:
							pickItem = new Promise((response, reject) => {
								let item;
								myJobItem = rare.filter((e) => e.job === playerInfo.jobline);
								if (Math.random() < 0.3) {
									item = myJobItem[option(myJobItem.length)];
								} else {
									item = epic[option(epic.length)];
								}
								response(item);
							});
							break;
						case 5:
							pickItem = new Promise((response, reject) => {
								let item;
								myJobItem = epic.filter((e) => e.job === playerInfo.jobline);
								if (Math.random() > 0.5) {
									item = myJobItem[option(myJobItem.length)];
								} else {
									item = epic[option(epic.length)];
								}
								response(item);
							});

							break;
						default:
							break;
					}
					await pickItem.then((item) => {
						if (item === undefined) {
							return;
						} else {
							_sales.push(item);
							i++;
						}
					});
				}
				return _sales;
			}
			res(await endWhile());
		});
		setSales.then((sales) => {
			let j = 1;
			for (const item of sales) {
				let itemCost = 30;
				switch (item.rarity) {
					case '일반':
						break;
					case '희귀':
						itemCost += 50;
						break;
					case '영웅':
						itemCost += 70;
						break;
					default:
						break;
				}
				if (item.type === '무기') {
					itemCost += 30;
				}
				emitText(
					'text',
					`${j}: <${item.name}(${item.job})>(${item.rarity})-${item.type} {attackPoint: ${item.stats.attackPoint}, maxHp: ${item.stats.maxHp}, deffense: ${item.stats.deffense}}`
				);
				emitText('text', `Cost: ${itemCost}Gold`);
				io.emit('shop choices', { num: j, name: item.name, cost: itemCost });
				j++;
			}
			emitText('text', `0: exit`);
		});

		io.emit('shop choices', { num: 0, name: 'exit', cost: 0 });
	}
}

async function processDecision(name, type, decision) {
	const playerInfo = await getPlayerInfo(name);
	const playerData = await playerSetting(playerInfo);

	const playerStats = playerInfo.stats;
	const playerSkills = playerInfo.skills;
	const playerItems = playerInfo.items;
	const playerEquipments = new Equips(playerInfo.equipments);

	if (decision === 'exit') {
		if ((await getPlayerState(name)) === 'lull') {
			await sendStatsWithChoices(name);
		} else {
			await sendStats(name);
			await switchState(name);
		}

		return;
	}
	if (decision === 'back') {
		processCommand(name, `/${type}`);
		return;
	}
	let itemCost;
	let _msg;
	switch (type) {
		case 'skills':
			const skill = playerData.findSkill(decision);
			_msg = `이름: ${skill.name}`;
			emitText('text', _msg);
			_msg = `스킬레벨: ${skill.level}`;
			emitText('text', _msg);
			_msg = `효과: ${skill.effect}`;
			emitText('text', _msg);
			_msg = `기본 데미지: ${skill.defaultDamage}`;
			emitText('text', _msg);
			_msg = `스킬레벨 당 데미지 증가: ${skill.increasePerLevel}`;
			emitText('text', _msg);
			_msg = `데미지 계수: ${skill.damageFactor}`;
			emitText('text', _msg);
			_msg = `공격 횟수: ${skill.attackTimes}`;
			emitText('text', _msg);
			_msg = `쿨타임: ${skill.cooltime}`;
			emitText('text', _msg);
			emitText('text', '1. back');
			io.emit('command choices', { num: 1, choice: 'back' });
			emitText('text', '0. exit');
			io.emit('command choices', { num: 0, choice: 'exit' });
			io.emit('next respond', { msg: undefined, type: 'skills' });
			break;
		case 'items':
			if (decision === 'sell') {
				const sellingItem = playerData.focusItem;
				playerData.pullItem(sellingItem);
				itemCost = 10;
				switch (sellingItem.rarity) {
					case '일반':
						break;
					case '희귀':
						itemCost += 5;
						break;
					case '영웅':
						itemCost += 15;
						break;
					default:
						break;
				}
				if (sellingItem.type === '무기') {
					itemCost += 7;
				}
				playerData.gold += itemCost;
				_msg = `<${sellingItem.name}(${sellingItem.job})>을(를) 팔아 ${itemCost}Gold를 얻었습니다.`;
				emitText('text', _msg);
				await sendStats(name);
				emitText('text', '1. back');
				io.emit('command choices', { num: 1, choice: 'back' });
				emitText('text', '0. exit');
				io.emit('command choices', { num: 0, choice: 'exit' });
				io.emit('next respond', { msg: undefined, type: 'items' });
			} else if (decision === 'setEquip') {
				const equipingItem = playerData.focusItem;

				if (playerData.isMatchJob()) {
					_msg = `<${equipingItem.name}(${equipingItem.job})>(${equipingItem.rarity})이(가) 장착되었습니다.`;
					playerData.pushEquipment(equipingItem);
				} else {
					_msg = `현재 직업군과 맞지 않는 아이템입니다. 장착할 수 없습니다.`;
				}
				emitText('text', _msg);
				await sendStats(name);
				emitText('text', '1. back');
				io.emit('command choices', { num: 1, choice: 'back' });
				emitText('text', '0. exit');
				io.emit('command choices', { num: 0, choice: 'exit' });
				io.emit('next respond', { msg: undefined, type: 'items' });
			} else {
				const item = playerData.findItem(decision);

				if (item.name !== 'potion') {
					playerData.focusItem = item;
					emitText('text', '2. 판매');
					io.emit('command choices', { num: 2, choice: 'sell' });

					emitText('text', '3. 장착: !!겹치는 부위가 팔리지 않고 그대로 삭제됩니다!!');
					io.emit('command choices', { num: 3, choice: 'setEquip' });
				} else {
					playerData.pushEquipment(item);
					playerData.pullItem(item);
					const playerStats = playerInfo.stats;
					const healAmount = Math.floor(playerStats.maxHp * 0.3);
					_msg = `포션을 사용하여 [체력 ${healAmount}](30%)을 회복하였습니다.`;
					await sendStats(name);
				}

				emitText('text', _msg);
				emitText('text', '1. back');
				io.emit('command choices', { num: 1, choice: 'back' });
				emitText('text', '0. exit');
				io.emit('command choices', { num: 0, choice: 'exit' });
				io.emit('next respond', { msg: undefined, type: 'items' });
			}

			break;
		case 'equips':
			const equip = playerEquipments.get(decision);
			playerData.pullEquipment(equip);
			itemCost = 10;
			switch (equip.rarity) {
				case '일반':
					break;
				case '희귀':
					itemCost += 5;
					break;
				case '영웅':
					itemCost += 15;
					break;
				default:
					break;
			}
			if (equip.type === '무기') {
				itemCost += 7;
			}
			_msg = `<${equip.name}(${equip.job})>(${equip.rarity})이(가) 삭제되어 ${itemCost}Gold를 얻었습니다.`;
			emitText('text', _msg);
			await sendStats(name);
			emitText('text', '1. back');
			io.emit('command choices', { num: 1, choice: 'back' });
			emitText('text', '0. exit');
			io.emit('command choices', { num: 0, choice: 'exit' });
			io.emit('next respond', { msg: undefined, type: 'equips' });
			break;
		case 'moveOn':
			moveOn(name, decision);
			break;
		case 'shop':
			if (decision.name !== 'exit') {
				const itemList = await Items;
				const itemArray = itemList.filter((e) => e.name === decision.name);
				const itemPicked = itemArray[0];
				playerData.pushItem(itemPicked);
				_msg = `<${itemPicked.name}(${itemPicked.job})>(${itemPicked.rarity})을(를) 구매하였습니다.`;
				emitText('text', _msg);
				playerData.gold -= decision.cost;
			} else {
				emitText('text', `아무것도 사지 않고 상점을 나갑니다.`);
			}
			playerData.shopCount = 0;
			await switchState(name);
			break;
		default:
			console.log(`Process decision error occured`);
			break;
	}
	await setPlayerOnline(name, {
		playerInfo: playerData.getCharacterInfo(),
		mapData: await getPlayerMap(name),
		enemyInfo: await getPlayerEnemy(name),
		stateData: await getPlayerState(name),
	});
}

async function goAhead(playerData, choice) {
	const _playerData = new Promise((res, rej) => {
		const playerPosition = playerData.currentPosition;
		const currentFloor = playerPosition.floor;
		const currentRoute = choice;
		const currentStage = playerPosition.stage + 1;
		playerData.currentPosition = { floor: currentFloor, route: currentRoute, stage: currentStage };
		res(playerData);
	});

	return _playerData;
}

async function processChoice(name, choice) {
	let playerData = await playerSetting(await getPlayerInfo(name));
	const mapData = await getPlayerMap(name);
	const playerPosition = playerData.currentPosition;
	if (choice.includes('F')) {
		const currentFloor = playerPosition.floor + 1;
		const currentRoute = 'Start';
		const currentStage = 0;
		playerData.currentPosition = {
			floor: currentFloor,
			route: currentRoute,
			stage: currentStage,
		};
		playerData.shopCount = 1;
		const type = 'rest';
		await setPlayerOnline(name, {
			playerInfo: playerData.getCharacterInfo(),
			mapData: await mapping(currentFloor),
			enemyInfo: await getPlayerEnemy(name),
			stateData: type,
		});
		const _msg = `F${currentFloor}-Route ${currentRoute}:-${currentStage}- => ${type} encountered.`;
		io.emit('next respond', { msg: _msg, type: type });
	} else {
		const currentRoute = choice;
		const currentStage = playerPosition.stage + 1;
		playerData = await goAhead(playerData, choice);
		const playerInfo = playerData.getCharacterInfo();
		const type = mapData[mapRouteToIndex(currentRoute)][currentStage - 1].type;
		await setPlayerOnline(name, {
			playerInfo: playerInfo,
			mapData: mapData,
			enemyInfo: await getPlayerEnemy(name),
			stateData: type,
		});
		const _msg = `${currentRoute}-${currentStage} => ${type} encountered.`;
		io.emit('next respond', { msg: _msg, type: type });
	}
}

async function playerAttack(name, controll) {
	const playerData = await playerSetting(await getPlayerInfo(name));
	const playerInfo = playerData.getCharacterInfo();
	const enemyData = enemySetting(await getPlayerEnemy(name));
	const defaultAttackDamage = playerInfo.stats.attackPoint;
	const skills = playerInfo.skills;
	const skillMap = new Map();
	skillMap.set('기본공격', {
		effect: '들고 있는 무기로 아무렇게나 때려봅니다.',
		defaultDamage: defaultAttackDamage,
		increasePerLevel: 0,
		damageFactor: 1,
		attackTimes: 1,
		cooltime: 0,
		currentCool: 0,
	});
	for (const skill of skills) {
		skillMap.set(skill.name, {
			name: skill.name,
			level: skill.level,
			effect: skill.effect,
			defaultDamage: skill.defaultDamage,
			increasePerLevel: skill.increasePerLevel,
			damageFactor: skill.damageFactor,
			attackTimes: skill.attackTimes,
			cooldown: skill.cooldown,
			currentCool: skill.currentCool,
		});
	}
	let damage = 0;
	let isCritical;
	const playerControll = skillMap.get(controll);
	let enemyInfo = enemyData.getCharacterInfo();
	if (controll === '기본공격') {
		await playerData.defaultAttack(enemyInfo);
		const attackResult = await playerData.defaultAttackDamage(enemyInfo);
		damage = attackResult.damage;
		isCritical = attackResult.isCritical;
	} else {
		playerData.skillUsed(playerControll.name);
		for (let t = 0; t < playerControll.attackTimes; t++) {
			await playerData.skillAttack(playerControll, enemyInfo);
			const skillResult = await playerData.skillAttackDamage(playerControll, enemyInfo);
			damage += skillResult.damage;
			isCritical = skillResult.isCritical;
			if (isCritical) {
				emitText('critical effect', playerControll.effect);
			} else {
				emitText('effect', playerControll.effect);
			}
		}
	}

	emitText(
		'player attack',
		`효과는 굉장했다! <${enemyInfo.name}>에게 총 [${damage.toFixed(1)}]의 데미지를 주었다.`
	);
	emitText(
		'text',
		'----------------------------------------------------------------------------------'
	);
	await setPlayerOnline(name, {
		playerInfo: playerData.getCharacterInfo(),
		mapData: await getPlayerMap(name),
		enemyInfo: enemyData.getCharacterInfo(),
		stateData: await getPlayerState(name),
	});
	const isFinished = !enemyData.isAlive();
	if (isFinished) {
		return true;
	} else {
		return false;
	}
}

async function enemyAttack(name) {
	let playerData = await playerSetting(await getPlayerInfo(name));
	const playerInfo = playerData.getCharacterInfo();
	const enemyData = enemySetting(await getPlayerEnemy(name));
	const enemySkills = enemyData.skills;
	let usableSkill = [];
	let type;
	for (const skill of enemySkills) {
		if (skill.currentCool === 0) {
			usableSkill.push(skill);
		}
	}
	let damage = 0;
	if (usableSkill.length > 0) {
		const option = Math.floor(Math.random() * usableSkill.length);
		const skill = usableSkill[option];
		enemyData.skillUsed(skill.name);
		for (let t = 0; t < skill.attackTimes; t++) {
			await enemyData.skillAttack(skill, playerInfo);
			damage += await enemyData.skillAttackDamage(skill, playerInfo);
			emitText('text', skill.effect);
		}
		type = 'skillAttack';
	} else {
		await enemyData.defaultAttack(playerInfo);
		damage = await enemyData.defaultAttackDamage(playerInfo);
		type = 'defaultAttack';
	}

	playerData = await playerSetting(await getPlayerInfo(name));
	enemyData.skillCooldown();
	await setPlayerOnline(name, {
		playerInfo: playerData.getCharacterInfo(),
		mapData: await getPlayerMap(name),
		enemyInfo: enemyData.getCharacterInfo(),
		stateData: await getPlayerState(name),
	});
	const isDead = !playerData.isAlive();
	if (isDead) {
		return { isDead: true, damage: damage, type: type };
	} else {
		return { isDead: false, damage: damage, type: type };
	}
}

async function processCombat(name, controll) {
	const playerData = await playerSetting(await getPlayerInfo(name));
	const playerInfo = playerData.getCharacterInfo();
	const isFinished = await playerAttack(name, controll);
	const enemyData = enemySetting(await getPlayerEnemy(name));
	const enemyInfo = enemyData.getCharacterInfo();

	if (isFinished) {
		if (playerInfo.currentPosition.floor === 5 && playerInfo.currentPosition.stage === 13) {
			return endingSequence(name);
		}
		emitText('text', `방금의 일격으로 <${enemyInfo.name}>이(가) 사망했다. 보상이 들어온다!`);
		const reward = await rewardSetting(name, enemyInfo.level);
		const rewardItem = reward.item;
		const rewardExp = reward.exp;
		const rewardGold = reward.gold;

		const enemyNone = new Enemy(
			undefined,
			undefined,
			undefined,
			undefined,
			undefined,
			undefined,
			undefined
		);

		if (rewardItem === null || rewardItem === undefined) {
			io.emit('result', `경험치 [${rewardExp}]와 [${rewardGold}Gold]를 얻었다!`);
		} else {
			io.emit(
				'result',
				`<${rewardItem.name}(${rewardItem.job})>(${rewardItem.rarity}), 경험치 [${rewardExp}]와 [${rewardGold}Gold]를 얻었다!`
			);
			playerData.pushItem(rewardItem);
		}
		const isLevelUp = playerData.plusExp(rewardExp);
		playerData.gold += rewardGold;
		if (isLevelUp) {
			const info = playerData.getCharacterInfo();
			emitText('text', `##레벨업!! 축하합니다. 레벨${info.level}이 되셨습니다.`);
			if (info.level === 5 || info.level === 10 || info.level === 15) {
				playerData.needMoveOn = true;
			}
		}
		playerData.skillCooltimeReset();
		setPlayerOnline(name, {
			playerInfo: playerData.getCharacterInfo(),
			mapData: await getPlayerMap(name),
			enemyInfo: enemyNone.getCharacterInfo(),
			stateData: 'lull',
		});
	} else {
		const enemyAttackResult = await enemyAttack(name);
		const type = enemyAttackResult.type;
		const damage = enemyAttackResult.damage;
		const isDead = enemyAttackResult.isDead;
		if (isDead) {
			if (type === 'defaultAttack') {
				emitText(
					'enemy attack',
					`당신은 <${enemyInfo.name}>에게 [${damage.toFixed(1)}]의 데미지를 입고 사망하였습니다..`
				);
			} else if (type === 'skillAttack') {
				emitText(
					'enemy skill attack',
					`당신은 <${enemyInfo.name}>에게 [${damage.toFixed(1)}]의 데미지를 입고 사망하였습니다..`
				);
			}

			await deletePlayerData(name);
			emitText('text', `게임을 다시 시작하십시오.`);
		} else {
			let outputDamage;
			if (typeof damage === 'string') {
				outputDamage = stoi(damage).toFixed(1);
			} else if (typeof damage === 'number') {
				outputDamage = damage.toFixed(1);
			} else {
				outputDamage = 'error';
			}
			if (type === 'defaultAttack') {
				emitText(
					'enemy attack',
					`당신은 <${enemyInfo.name}>의 반격으로 [${outputDamage}]의 데미지를 입었습니다..!`
				);
			} else if (type === 'skillAttack') {
				emitText(
					'enemy skill attack',
					`당신은 <${enemyInfo.name}>의 반격으로 [${outputDamage}]의 데미지를 입었습니다..!`
				);
			}
			playerData.skillCooldown();
			setPlayerOnline(name, {
				playerInfo: playerData.getCharacterInfo(),
				mapData: await getPlayerMap(name),
				enemyInfo: enemyData.getCharacterInfo(),
				stateData: 'combat',
			});
			await sendStats(name);
			await sendEnemyStats(name);
			await sendCombatChoices(name);
		}
	}
}

async function rewardSetting(name, level) {
	const playerData = await playerSetting(await getPlayerInfo(name));
	const enemyData = await getPlayerEnemy(name);
	const enemyLevel = enemyData.level;
	const enemyType = enemyData.type;
	const enemyRarity = enemyData.rarity;
	const itemList = await Items;
	const bossItemList = await BossItems;
	let reward;
	let rewardExp;
	let expPerLevel = 5;
	if (enemyType === 'Boss') {
		expPerLevel += 4;
	}
	switch (enemyRarity) {
		case '하위':
			break;
		case '중위':
			expPerLevel += 3;
			break;
		case '상위':
			expPerLevel += 7;
			break;
		case '최상위':
			expPerLevel += 11;
			break;
		default:
			break;
	}
	rewardExp = enemyLevel * expPerLevel;

	const playerInfo = await getPlayerInfo(name);
	const bossWeapon = bossItemList.filter((e) => e.type === '무기');
	const bossGear = bossItemList.filter((e) => e.type !== '무기');
	if (enemyType === 'Boss') {
		if (enemyLevel === 15) {
			for (const item of bossWeapon) {
				if (item.job === playerData.jobline) {
					reward = { item: item, exp: rewardExp, gold: 5 };
					return reward;
				}
			}
		} else {
			const option = (length) => {
				return Math.floor(Math.random() * length);
			};
			while (1) {
				const opt = option(bossGear.length);
				const item = bossGear[opt];
				if (item.job === playerData.jobline) {
					reward = { item: item, exp: rewardExp, gold: 5 };
					return reward;
				}
			}
		}
	} else {
		const normal = itemList.filter((e) => e.rarity === '일반');
		const rare = itemList.filter((e) => e.rarity === '희귀');
		const epic = itemList.filter((e) => e.rarity === '영웅');
		let myJobItem = [];
		let option = (length) => {
			return Math.floor(Math.random() * length);
		};
		if (Math.random() > 0.2) {
			if (enemyLevel < 5) {
				reward = { item: normal[option(normal.length)], exp: rewardExp, gold: 5 };
			} else {
				if (enemyLevel < 10) {
					myJobItem = rare.filter((e) => e.job === playerInfo.jobline);
					if (Math.random() > 0.5) {
						reward = { item: myJobItem[option(myJobItem.length)], exp: rewardExp, gold: 5 };
					} else {
						reward = { item: rare[option(rare.length)], exp: rewardExp, gold: 5 };
					}
				} else {
					myJobItem = epic.filter((e) => e.job === playerInfo.jobline);
					if (Math.random() > 0.5) {
						reward = { item: myJobItem[option(myJobItem.length)], exp: rewardExp, gold: 5 };
					} else {
						reward = { item: epic[option(epic.length)], exp: rewardExp, gold: 5 };
					}
				}
			}
		} else {
			reward = { item: null, exp: rewardExp, gold: 5 };
		}

		return reward;
	}
}

async function findEnemy(enemyName) {
	const enemyList = await enemies;
	for (const enemy of enemyList) {
		if (enemy.name === enemyName) {
			return enemy.getCharacterInfo();
		}
	}
}

function pickEnemy(enemyMeetLevel) {
	const option = Math.floor(Math.random() * enemyMeetLevel.length);
	return enemyMeetLevel[option];
}

async function startCombat(name) {
	const playerInfo = await getPlayerInfo(name);
	const playerData = await playerSetting(playerInfo);
	const playerMap = await getPlayerMap(name);
	const playerRoute = playerInfo.currentPosition.route;
	const playerStage = playerInfo.currentPosition.stage;
	let enemyData;
	const enemy = await getPlayerEnemy(name);

	if (enemy.name === undefined) {
		const routeIndex = mapRouteToIndex(playerRoute);
		const enemyName = playerMap[routeIndex][playerStage - 1].enemy;
		enemyData = enemySetting(await findEnemy(enemyName));
		enemyData.hpReset();
		enemyData.skillCooltimeReset();
	} else {
		enemyData = enemySetting(enemy);
	}

	await setPlayerOnline(name, {
		playerInfo: playerInfo,
		mapData: await getPlayerMap(name),
		enemyInfo: enemyData.getCharacterInfo(),
		stateData: await getPlayerState(name),
	});
	await sendEnemyStats(name);

	await sendCombatChoices(name);
}

async function sendCombatChoices(name) {
	const playerData = await playerSetting(await getPlayerInfo(name));
	const playerInfo = playerData.getCharacterInfo();
	const skills = playerInfo.skills;

	let choices = ['기본공격'];
	for (const skill of skills) {
		if (skill.currentCool === 0) {
			choices.push(skill.name);
		}
	}
	emitText('text', '선택 가능 목록:');
	let i = 1;
	for (const choice of choices) {
		emitText('text', `${i}. ${choice}`);
		io.emit('combat choices', { choice: choice, num: i });
		i++;
	}
	emitText(
		'text',
		'----------------------------------------------------------------------------------'
	);
}

async function sendEnemyStats(name) {
	const enemyData = enemySetting(await getPlayerEnemy(name));
	const enemyInfo = enemyData.getCharacterInfo();
	emitText(
		'text',
		'----------------------------------------------------------------------------------'
	);
	let _msg = `#몬스터 스탯`;
	emitText('text', _msg);
	_msg = `name: ${enemyInfo.name}`;
	emitText('text', _msg);
	_msg = `job: ${enemyInfo.job}`;
	emitText('text', _msg);
	_msg = `level: ${enemyInfo.level}`;
	emitText('text', _msg);
	_msg = `hp: ${enemyInfo.stats.currentHp.toFixed(1)}/${enemyInfo.stats.maxHp.toFixed(1)}`;
	emitText('text', _msg);
	emitText(
		'text',
		'----------------------------------------------------------------------------------'
	);
}

async function rest(name) {
	const playerData = await playerSetting(await getPlayerInfo(name));
	const playerInfo = playerData.getCharacterInfo();
	const playerStats = playerInfo.stats;
	let healPercent;
	if (playerInfo.currentPosition.route === 'Start') {
		healPercent = 0.8;
	} else {
		healPercent = 0.3;
	}
	const healAmount = Math.floor(playerStats.maxHp * healPercent);
	playerData.heal(healAmount);

	const _msg = `플레이어는 휴식을 취하며 [체력 ${healAmount}](${
		healPercent * 100
	}%)을 회복하였습니다.`;
	io.emit('result', _msg);
	await sendStats(name);
	if (playerData.findItem('potion') === null) {
		io.emit('result', `포션을 소지하시지 않아 포션을 1개 획득하셨습니다.`);
		playerData.pushItem({ name: 'potion' });
	}

	await setPlayerOnline(name, {
		playerInfo: playerData.getCharacterInfo(),
		mapData: await getPlayerMap(name),
		enemyInfo: await getPlayerEnemy(name),
		stateData: await getPlayerState(name),
	});
}

function startEvent(name) {
	const choices = ['체력 20% 회복', '공격력 증가', '방어력 증가', '모든 스킬 레벨 1 증가'];
	emitText('text', '선택 가능 목록:');
	let i = 1;
	for (const choice of choices) {
		emitText('text', `${i}. ${choice}`);
		io.emit('event choices', { choice: choice, num: i });
		i++;
	}
	emitText(
		'text',
		'----------------------------------------------------------------------------------'
	);
}

async function processEventChoice(name, choice) {
	const playerData = await playerSetting(await getPlayerInfo(name));
	const playerInfo = playerData.getCharacterInfo();
	const playerFloor = playerInfo.currentPosition.floor;
	const playerStats = playerInfo.stats;
	let _msg;
	let deltaStats;
	switch (choice) {
		case '체력 20% 회복':
			const healAmount = Math.floor(playerStats.maxHp * 0.2);
			playerData.heal(healAmount);
			_msg = `플레이어는 보상으로 [체력 ${healAmount}](20%)을 회복하였습니다.`;

			break;
		case '공격력 증가':
			deltaStats = new Stats(0, 0, playerFloor * 3, 0, 0, 0);

			playerData.setStats(deltaStats);
			_msg = `플레이어는 보상으로 [공격력 ${playerFloor * 3}]을 획득하였습니다.`;
			await sendStats(name);

			break;
		case '방어력 증가':
			deltaStats = new Stats(0, 0, 0, playerFloor * 2, 0, 0);

			playerData.setStats(deltaStats);
			_msg = `플레이어는 보상으로 [방어력 ${playerFloor * 4}]를 획득하였습니다.`;

			break;
		case '모든 스킬 레벨 1 증가':
			const skills = playerInfo.skills;
			for (const skill of skills) {
				playerData.increaseSkillLevel(skill.name);
			}
			_msg = `플레이어는 보상으로 [모든 스킬 레벨 1]을 획득하였습니다.`;

			break;
		default:
			console.log('event error occured');
			break;
	}
	emitText('text', _msg);
	sendLullRespond(name);
	sendStatsWithChoices(name);

	await setPlayerOnline(name, {
		playerInfo: playerData.getCharacterInfo(),
		mapData: await getPlayerMap(name),
		enemyInfo: await getPlayerEnemy(name),
		stateData: await getPlayerState(name),
	});
}

async function switchState(name) {
	const state = await getPlayerState(name);
	switch (state) {
		case 'lull':
			io.emit('type', state);
			await sendStatsWithChoices(name);
			break;
		case 'combat':
			io.emit('type', state);
			await sendStats(name);
			await startCombat(name);
			break;
		case 'event':
			io.emit('type', state);
			await startEvent(name);
			break;
		case 'rest':
			io.emit('type', state);
			await rest(name);
			break;
		default:
			console.log(`switch state error occured`);
			break;
	}
}

async function endingSequence(name) {
	emitText('text', `세계의 의지를 무너뜨리고 당신은 승리하였습니다. 축하합니다!`);
	emitText('text', `새로운 도전을 원하신다면 페이지를 새로고침 해주십시오.`);
	await deletePlayerData(name);
}

function deletePlayerData(name) {
	return new Promise((res, rej) => {
		userDb.query(`DELETE FROM ${PLAYER_DATA} WHERE name='${name}';`, (error, results) => {
			if (error) {
				rej(error);
				console.log(error);
			} else {
				res();
			}
		});
	});
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

let connectionNum = 0;
io.on('connection', (socket) => {
	if(connectionNum > 1) socket.disconnect();
	if(connectionNum === 0) connectionNum ++;
	
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
		await loadData(name);
		io.emit('greeting', {
			name: name,
			greeting: `환영합니다, ${name}. 게임을 시작하고 싶다면 "start"라고 아래 입력창에 입력 후 엔터를 누르세요..`,
		});
	});

	// socket.on('memorizing user name', async (name) => {
	// 	await updateUser(name, socket.id);
	// });

	socket.on('start', async (name) => {
		// await updateUser(name, socket.id);
		console.log(`${name}: ${socket.id} >> start`);
		await processCommand(name, '/help');
		await switchState(name);
	});

	socket.on('command', async (res) => {
		// const socketId = socket.id;
		// const name = await userName(socketId);
		const command = res.command;
		const name = res.name;
		console.log(`command recieved from ${name}: ${command}`);
		//데이터베이스에서 command에 대한 결과를 result에 담기
		await processCommand(name, command);
	});

	socket.on('choice', async (res) => {
		// const socketId = socket.id;
		// const name = await userName(socketId);
		const choice = res.choice;
		const name = res.name;
		console.log(`choice recieved from ${name}: ${choice}`);

		const result = await processChoice(name, choice);
		await saveData(name);
	});

	socket.on('rest encounter', async (name) => {
		// const socketId = socket.id;
		// const name = await userName(socketId);
		console.log(`rest encounter recieved from ${name}`);

		await rest(name);
		await saveData(name);
	});

	socket.on('event encounter', async (name) => {
		// const socketId = socket.id;
		// const name = await userName(socketId);
		console.log(`event encounter recieved from ${name}`);

		await startEvent(name);
		await saveData(name);
	});

	socket.on('combat encounter', async (name) => {
		// const socketId = socket.id;
		// const name = await userName(socketId);
		console.log(`combat encounter recieved from ${name}`);

		await startCombat(name);
		await saveData(name);
	});

	socket.on('event', async (res) => {
		// const socketId = socket.id;
		// const name = await userName(socketId);
		const choice = res.choice;
		const name = res.name;
		console.log(`choice for event recieved from ${name}: ${choice}`);

		await processEventChoice(name, choice);
		await saveData(name);
	});

	socket.on('combat', async (res) => {
		// const socketId = socket.id;
		// const name = await userName(socketId);
		const controll = res.controll;
		const name = res.name;
		console.log(`controll for combat recieved from ${name}: ${controll}`);

		await processCombat(name, controll);
		await saveData(name);
	});

	socket.on('decision', async (res) => {
		const type = res.type;
		const decision = res.decision;
		const name = res.name;
		// const socketId = socket.id;
		// const name = await userName(socketId);
		console.log(`decision for ${type} recieved from ${name}: ${decision}`);

		const result = await processDecision(name, type, decision);
		await saveData(name);
	});

	socket.on('next request', async (name) => {
		//데이터베이스에서 현재 상태, 다음 선택지를 respond에 담기
		// const socketId = socket.id;
		// const name = await userName(socketId);
		await loadData(name);
		await sendStatsWithChoices(name);
	});

	socket.on('disconnect', async (res) => {
		connectionNum --;
		// const socketId = socket.id;
		// const name = await userName(socketId);
		// console.log(`${name} disconnected`);
		// deleteLoggedUser(socketId);
	});
});