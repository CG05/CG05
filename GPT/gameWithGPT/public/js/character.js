class Character {
	_name;
	_level;
	_job;
	_stats;
	_skills;

	constructor(name, level, job, stats, skills) {
		console.log(stats);
		this._name = name;
		this._level = level;
		this._job = job;
		this._stats = stats;
		this._skills = skills;
	}

	get name(){
		return this._name;
	}
	
	set name(name){
		this._name = name;
	}
	
	getCharacterInfo() {
		const characterInfo = {
			level: this._level,
			job: this._job,
			stats: this._stats,
		};
		return characterInfo;
	}
	
	setCharacterInfo(characterInfo){
		const info = this.getCharacterInfo();
		for (const key in characterInfo) {
			if (characterInfo.hasOwnProperty(key)) {
				info[key] += characterInfo[key];
			}
		}
		this._level = info.level;
		this._job = info.job;
		this._stats = info.stats;
		this._skills = info.skills;
	}

	setStats(deltaStats) {
		for (const key in deltaStats) {
			if (deltaStats.hasOwnProperty(key)) {
				this._stats[key] += deltaStats[key];
			}
		}
	}

	get skills() {
		return this._skills;
	}

	addSkill(skill) {
		const {
			name: name,
			effect: effect,
			defaultDamage: defaultDamage,
			increasePerLevel: increasePerLevel,
			damageFactor: damageFactor,
			cooldown: cooldown,
		} = skill.getSkillInfo();
		const newSkill = {
			name: name,
			level: 1,
			effect: effect,
			defaultDamage: defaultDamage,
			increasePerLevel: increasePerLevel,
			damageFactor: damageFactor,
			cooldown: cooldown,
		}
		this._skill.push(newSkill);
	}

	increaseSkillLevel(skillName) {
		const skill = this._skill.find((s) => s.name === skillName);

		// 해당 객체가 존재하면 level 속성 값을 1 증가시킵니다.
		if (skill) {
			skill.level += 1;
			console.log(`${skillName}의 레벨이 1 증가했습니다. (현재 레벨: ${skill.level})`);
		} else {
			console.log(`${skillName}을(를) 배우지 않았습니다.`);
		}
	}

	defaultAttack(targetInfo) {
		const target = this.targetSetting(targetInfo);
		const damage = this.defaultAttackDamage(targetInfo);
		target.takeDamage(damage);
		console.log(
			`${targetInfo.name}에게 기본공격으로 ${damage}만큼의 피해를 입혔습니다.`
		);
	}

	defaultAttackDamage(targetInfo) {
		const target = this.targetSetting(targetInfo);
		// const damage = this.criticalProcedure(this._stats.attackPoint * this._stats.damageAmplify);
		const damage = this._stats.attackPoint * this._stats.damageAmplify;
		const targetStats = target.getCharacterInfo().stats;
		const targetDeffense = targetStats.deffense - this._stats.deffensePierce;
		console.log(this.damageReduce(targetDeffense));
		const resultDamage = damage * this.damageReduce(targetDeffense);

		return resultDamage.toFixed(1);
	}

	skillAttack(skill, targetInfo) {
		const target = this.targetSetting(targetInfo);
		const damage = this.skillAttackDamage(skill, targetInfo);
		target.takeDamage(damage);
		console.log(
			`${targetInfo.name}에게 ${skill.name}(으)로 ${damage}만큼의 피해를 입혔습니다.`
		);
	}

	skillAttackDamage(skill, targetInfo) {
		const target = this.targetSetting(targetInfo);
		const damage1 =
			skill.defaultDamage + this._stats.attackPoint * skill.damageFactor * this._stats.damageAmplify;
		// const damage2 = this.criticalProcedure(damage1);
		const targetStats = target.getCharacterInfo().stats;
		const targetDeffense = targetStats.deffense - this._stats.deffensePierce;
		// return damage2 * this.damageReduce(targetDeffense);
		const resultDamage = damage1 * this.damageReduce(targetDeffense);
		return resultDamage.toFixed(1);
	}

	// criticalProcedure(damage) {
	// 	let d;

	// 	if (Math.random() * 100 <= this._stats.criticalChance) {
	// 		d = damage * this._stats.criticalDamage;
	// 	} else {
	// 		d = damage * this._stats.damageAmplify;
	// 	}

	// 	return d;
	// }

	damageReduce(deffense) {
		return 100 / (100 + deffense);
	}
	
	targetSetting(){
		
	}
	
	heal(amount){
		this._stats.currentHp += amount;
	}
	
	hpReset(){
		this._stats.currentHp = this._stats.maxHp;
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

module.exports = {Character};