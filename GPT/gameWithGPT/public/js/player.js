const Character = require('./character.js');

class Player extends Character {
	#maxExp;
	#exp;
	#currentPosition;
	#equipment;
	
  constructor(name, level, maxExp, exp, job, stats, skills, currentPosition, equipment){
		super(name, level, job, stats, skills);
		this.#maxExp = maxExp;
		this.#exp = exp;
		this.#currentPosition = currentPosition;
		this.#equipment = equipment;
	}
	
	getCharacterInfo(){
		const characterInfo = {
			"level": this._level,
			"maxExp": this.#maxExp,
			"exp": this.#exp,
			"job": this._job,
			"stats": this._stats,
			"skills": this._skills,
			"currentPosition": this.#currentPosition,
			"equipment": this.#equipment
		}
		return characterInfo;
	}
	
	setCharacterInfo(characterInfo){
		const info = this.getCharacterInfo();
		for (const key in characterInfo) {
			if (characterInfo.hasOwnProperty(key)) {
				info[key] = characterInfo[key];
			}
		}
		this._level = info.level;
		this.#maxExp = info.maxExp;
		this.#exp = info.exp;
		this._job = info.job;
		this._stats = info.stats;
		this._skills = info.skills;
		this.#currentPosition = info.currentPosition;
		this.#equipment = info.equipment;
	}
	
	plusExp(exp){
		this.#exp += exp;
	}
	
	changeJob(job){
		this._job = job;
	}
	
	get currentPosition() {
    return this.#currentPosition;
	}

  set currentPosition(position) {
    this.#currentPosition = position;
  }
	
	get equipment(){
		return this.#equipment;
	}
	
	pullEquipment(item){
		this.#equipment.pull(item);
	}
	
	pushEquipment(item){
		this.#equipment.push(item);
	}
	
	levelUp(){
		this._level += 1;
		//레벨업으로 올라가는 모든 수치 증가
	}
	
	clone() {
    return new Player(this._name, this._level, this.#maxExp, this.#exp, this._job, this._stats, this._skills, this.#currentPosition, this.#equipment);
  }

}

module.exports = {Player};
