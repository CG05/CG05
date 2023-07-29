const fs = require('fs');
const path = require('path');
const {Character} = require('./character.js');
const playerModule = require('./player.js');
const { Stats } = require('./stats.js');
const { Equips } = require('./equips.js');

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
			name: this._name,
			level: this._level,
			type: this.#type,
			rarity: this.#rarity,
			job: this._job,
			stats: this._stats,
			skills: this._skills
		};
		return characterInfo;
	}
	
	skillCooltimeReset(){
		for(const skill of this._skills){
			skill.currentCool = skill.cooltime;
			
		}
	}

	targetSetting(info) {
		const Player = playerModule.Player;
		const equips = new Equips(info.equipments);
  const stats = new Stats(info.stats);
  const setting = () => {
    return new Player(
      info.name,
      info.level,
      info.maxExp,
      info.exp,
      info.job,
      stats,
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
  const targetData = setting();
		return targetData;
	}
}

// 전체 몬스터 목록을 담은 배열

async function loadEnemies() {
	const response = await fs.readFileSync(path.join(__dirname, "../database/enemies.json"));
	const enemiesData = await JSON.parse(response);

	const _enemies = [];
	return new Promise((res, rej) => {
		for (const data of enemiesData) {
			const dataStats = data.stats;
			const stats = new Stats(dataStats);
			const enemy = new Enemy(
				data.name,
				data.level,
				data.type,
				data.rarity,
				data.job,
				stats,
				data.skills
			);
			_enemies.push(enemy);
		}
		res(_enemies);
	});
}

const enemies = loadEnemies();

module.exports = { Enemy, enemies };