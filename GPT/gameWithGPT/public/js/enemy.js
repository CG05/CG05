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
	
}

// 전체 몬스터 목록을 담은 배열

async function loadEnemies() {
  const response = await fs.readFileSync("../../Database/enemies.json");
  const enemiesData = await JSON.parse(response);
  const enemies = [];
  for (const data of enemiesData) {
    const enemy = new Enemy(enemiesData.name, enemiesData.skills, enemiesData.nextJob);
    enemies.push(enemy);
  }
  return enemies;
}

const Enemies = loadEnemies();

module.exports = {Enemy, Enemies};