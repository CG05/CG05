class Character{
	_name;
	_level;
	_job;
  _stats;
	_skills;

  constructor(name, level, job, stats, skills) {
    this._name = name;
		this._level = level;
		this._job = job;
    this._stats = stats;
		this._skills = skills;
  }
	
	getCharacterInfo(){
		const characterInfo = {
			name: this._name,
			level: this._level,
			job: this._job,
			stats: this._stats,
		}
		return characterInfo;
	}
	
	set stats(deltaStats){
		for (const key in deltaStats) {
  		if (deltaStats.hasOwnProperty(key)) {
    		this._stats[key] += deltaStats[key];
  		}
		}
	}

	get skills(){
		return this._skills;
	}
	
	addSkill(skill){
		this._skill.push(skill);
	}
	
  attack(target) {
    target.takeDamage(this._stats.attackPoint);
  }

  takeDamage(damage) {
    this._stats.currentHp -= damage;
    if (this._stats.currentHp < 0) {
      this._stats.currentHp = 0;
    }
  }

  isAlive() {
    return this._stats.currentHp > 0;
  }
}

export default Character;
