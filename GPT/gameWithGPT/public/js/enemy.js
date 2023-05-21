const fs = require('fs');
const Character = require('./character.js');

// 전체 몬스터 목록을 담을 클래스
class Enemy extends Character {
	#type;
	#rarity;
  constructor(name, level, type, rarity, job, stats, skills) {
		super(name, level, job, stats, skills);
    this.#type = type;
		this.#rarity = rarity;
  }
	
	getCharacterInfo() {
		const characterInfo = {
			"name": this._name, 
			"level": this._level, 
			"type": this.#type, 
			"rarity": this.#rarity, 
			"job": this._job, 
			"stats": this._stats, 
			"skills": this._skills
		};
		return characterInfo;
	}
}

// 전체 몬스터 목록을 담은 배열

async function loadEnemies() {
  const response = await fs.readFileSync("../../Database/enemies.json");
  const enemiesData = await JSON.parse(response);
  
	const _enemies = [];
	return new Promise((res, rej)=>{
		for (const data of enemiesData) {
    	const enemy = new Enemy(data.name, data.level, data.type, data.rarity, data.job, data.stats, data.skills);
    	_enemies.push(enemy);
  	}
		res(_enemies);
	});
}

const enemies = loadEnemies();

module.exports = {Enemy, enemies};