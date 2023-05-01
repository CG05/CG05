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

function loadEnemies() {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "../Data/enemies.json", false);
  xhr.send(null);
  const enemiesData = JSON.parse(xhr.responseText);
  const enemies = [];
  for (const enemiesData of enemiesData) {
    const enemy = new Enemy(enemiesData.name, enemiesData.level, enemiesData.type, enemiesData.rarity, enemiesData.job, enemiesData.stats, enemiesData.skills);
    enemies.push(item);
  }
  return enemies;
}

const Enemies = loadEnemies();

export default {Enemy, Enemies};