const fs = require('fs');
const { Enemy, enemies } = require('./enemy.js');
const playerModule = require('./player.js');
const Player = playerModule.Player;

class Node {
	constructor(floor, num, type, branch, enemy) {
		this.floor = floor;
		this.num = num;
		this.type = type;
		this.branch = branch;
		this.enemy = enemy
	}
}

async function loadRoute(floor) {
	return new Promise((res, rej) => {
		const route = [];
	for (let i = 1; i < 14; i++) {
		const node = new Node(floor, i, "yet", false, "yet");
		route.push(node);
	}
	res(route);
	})
	
}

function pickEnemy(enemyMeetLevel) {
	const option = Math.floor(Math.random() * enemyMeetLevel.length);
	return enemyMeetLevel[option];
}

async function chosenEnemy(floor, num){
	return new Promise(async (res, rej) => {
		const enemyList = await enemies;
	let enemyMeetLevel = [];
	let enemyRarity;
	let enemyLevelLimitHigh;
	let enemyLevelLimitLow;
	switch(floor){
		case 1:
			enemyRarity = '하위';
			enemyLevelLimitHigh = 5;
			enemyLevelLimitLow = 1;
			break;
		case 2:
			enemyRarity = '중위';
			enemyLevelLimitHigh = 10;
			enemyLevelLimitLow = 5;
			break;
		case 3:
			enemyRarity = '중위';
			enemyLevelLimitHigh = 10;
			enemyLevelLimitLow = 5;
			break;
		case 4:
			enemyRarity = '상위';
			enemyLevelLimitHigh = 15;
			enemyLevelLimitLow = 10
			break;
		case 5:
			enemyRarity = '최상위';
			enemyLevelLimitHigh = 30;
			enemyLevelLimitLow = 15;
			break;
		default:
			break;
	}
	for (const enemy of enemyList) {
		const info = enemy.getCharacterInfo();
		
			if (info.rarity === enemyRarity && info.type === 'nonBoss' && info.level > 1 && info.level < enemyLevelLimitHigh && info.level > enemyLevelLimitLow) {
				enemyMeetLevel.push(enemy);
			}
		
	}
	const pickedEnemy = pickEnemy(enemyMeetLevel);
	res(pickedEnemy.getCharacterInfo().name); 
	});
	
}

async function setNodeType(route) {
	let combatCount = 0;
	let minor;
	switch(route[0].floor){
		case 1:
			minor = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
			route[0].type = "combat";
	route[0].enemy = "하급 고블린";
	route[12].type = "combat";
	route[12].enemy = "대장 고블린";
	route[11].type = "rest";
			break;
		case 2:
		case 3:
			minor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
	route[12].type = "combat";
	route[12].enemy = "어둠의 정령";
			route[11].type = "rest";
			break;
		case 3:
		case 4:
			minor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
	route[12].type = "combat";
	route[12].enemy = "어둠의 대정령";
			route[11].type = "rest";
			break;
		case 5:
			minor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
	route[12].type = "combat";
	route[12].enemy = "세계의 의지";
			route[11].type = "rest";
			break;
		default:
			break;
	}
	
	
	while (combatCount < 7) {
		const index = Math.floor(Math.random() * 12);
		const num = index + 1;
		if (minor.includes(num)) {
			if(route[index].type !== undefined){
				minor = minor.filter((number) => (number = num));
				route[index].type = "combat";
				
				combatCount++;
				route[index].enemy = await chosenEnemy(route[index].floor, num);
			}else{
				continue;
			}
			
		} else {
			continue;
		}
	}
	let eventCount = 0;
	let restCount = 0;
	await minor.map(async (e)=>{
		const option = Math.random();
		if(option > 0.5 && eventCount < 4){
			route[e - 1].type = "event";
			eventCount++;
		}else{
			route[e - 1].type = "combat";
			route[e - 1].enemy = await chosenEnemy(route[e - 1].floor, combatCount);
		}
	})
	return route;
}

function setNodeBranch(routeA, routeB, routeC) {
	console.log(routeA);
	let branchCount = 0;
	let minor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
	while (branchCount < 2) {
		const index = Math.floor(Math.random() * 13);
		const num = index + 1;
		if (minor.includes(num)) {
			const option = Math.random();
			if (option > 0.75 && index < 12) {
				if(!routeA[index + 1].branch){
					minor = minor.filter((number) => (number = num));
					routeB[index].branch = true;
					routeA[index + 1].branch = true;
					branchCount++;
				}
			} else if (option > 0.5 && index > 0) {
				if(!routeA[index - 1].branch){
					minor = minor.filter((number) => (number = num));
					routeB[index].branch = true;
					routeA[index - 1].branch = true;
					branchCount++;
				}
			} else if (option > 0.25 && index < 12) {
				if(!routeC[index + 1].branch){
					minor = minor.filter((number) => (number = num));
					routeB[index].branch = true;
					routeC[index + 1].branch = true;
					branchCount++;
				}
				
			} else if (option > 0 && index > 0) {
				if(!routeC[index - 1].branch){
					minor = minor.filter((number) => (number = num));
					routeB[index].branch = true;
					routeC[index - 1].branch = true;
					branchCount++;
				}
				
			}
			
			continue;
			
		} else {
			continue;
		}
	}
	return [routeA, routeB, routeC];
}

async function initRoutes(routeA, routeB, routeC) {
	return setNodeBranch(await setNodeType(routeA), await setNodeType(routeB), await setNodeType(routeC));
}

function displayMap(routes) {
	console.log(routes);
}

module.exports = { Node, loadRoute, initRoutes, displayMap };