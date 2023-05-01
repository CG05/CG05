
class Player extends Character {
	#maxExp;
	#exp;
	#currentPosition;
	#equipment;
	
  constructor(name, level, maxExp, exp, job, stats, currentPosition, skills, equipment){
		super(name, level, job, stats, skills);
		this.#maxExp = maxExp;
		this.#exp = exp;
		this.#currentPosition = currentPosition;
		this.#equipment = equipment;
	}
	
	getCharacterInfo(){
		const characterInfo = {
			name: this._name,
			level: this._level,
			expPercent: this.#exp / this.#maxExp * 100,
			job: this._job,
			stats: this._stats,
		}
		return characterInfo;
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

}

export default Player;
