// Player 클래스 정의
class Player {
  constructor(name, level) {
    this.name = name;
    this.level = level;
  }

  getInfo() {
    console.log(`name: ${this.name}, level: ${this.level}`);
  }
	
	toJSON() {
    return {
      name: this.name,
      level: this.level,
      getInfo: this.getInfo // 메소드를 포함시킴
    }
  }
}

// Player 인스턴스 생성
const player = new Player("Sung", 10);
const json = JSON.stringify(player);
console.log(player.toJSON());
const map = new Map();
map.set('sung', {playerData: json, mapData: []});

const data = map.get('sung');
const _json = data.playerData;
let name;
let level;
const _playerData = JSON.parse(_json, (key, value)=>{
	if(key == 'name') name = value;
	if(key == 'level') level = value;

	return new Player(name, level);
});
_playerData.getInfo();
