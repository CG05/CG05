// character.js 파일

class Character {
  #name;
	#level;
	#exp;
	#job;
  #maxHp;
  #currentHp;
  #attackPoint;
  #currentPosition;
	#skill;
	#equipment

  constructor(name, level, exp, job, maxHp, attackPoint, currentPosition, skill, equipment) {
    this.#name = name;
		this.#level = level;
		this.#exp = exp;
		this.#job = job;
    this.#maxHp = maxHp;
    this.#currentHp = maxHp;
    this.#attackPoint = attackPoint;
    this.#currentPosition = currentPosition;
		this.#skill = skill;
		this.equipment = equipment;
  }

  get name() {
    return this.#name;
  }
	
	get level(){
		return this.#level;
	}
	
	get exp(){
		return this.#exp;
	}
	
	plusExp(exp){
		this.#exp += exp;
	}
	
	get job(){
		return this.#job;
	}
	
	changeJob(job){
		this.#job = job;
	}

  get maxHp() {
    return this.#maxHp;
  }

  get currentHp() {
    return this.#currentHp;
  }

  get attackPoint() {
    return this.#attackPoint;
  }

  get currentPosition() {
    return this.#currentPosition;
  }

  set currentPosition(position) {
    this.#currentPosition = position;
  }
	
	get skill(){
		return this.#skill;
	}
	
	addSkill(skill){
		this.#skill.push(skill);
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
		this.#level += 1;
		//레벨업으로 올라가는 모든 수치 증가
	}

  attack(target) {
    target.takeDamage(this.#attackPoint);
  }

  takeDamage(damage) {
    this.#currentHp -= damage;
    if (this.#currentHp < 0) {
      this.#currentHp = 0;
    }
  }

  isAlive() {
    return this.#currentHp > 0;
  }
}

export default Character;
