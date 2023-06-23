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
			if (this._stats.hasOwnProperty(key)) {
				this._stats[key] += deltaStats[key];
			}
		}
	}

	get skills() {
		return this._skills;
	}
	
	findSkill(skillName){
		for(const skill of this._skills){
			if(skill.name === skillName){
				return skill;
			}
		}
	}
	
	averageSkillLevel(lastSkills){
		let sum = 0;
		for(const skill of lastSkills){
			sum += skill.level;
		}
		return sum / lastSkills.length;
	}

	addSkill(skill, lastSkills) {
		console.log(this.averageSkillLevel(lastSkills));
		const newSkill = {
			name: skill.name,
			level: Math.floor(this.averageSkillLevel(lastSkills)),
			effect: skill.effect,
			defaultDamage: skill.defaultDamage,
			increasePerLevel: skill.increasePerLevel,
			damageFactor: skill.damageFactor,
			attackTimes: skill.attackTimes,
			cooltime: skill.cooltime,
			currentCool: 0
		}
		this._skills.push(newSkill);
	}

	increaseSkillLevel(skillName) {
		const skill = this.findSkill(skillName);

		// 해당 객체가 존재하면 level 속성 값을 1 증가시킵니다.
		if (skill) {
			skill.level += 1;
			console.log(`${skillName}의 레벨이 1 증가했습니다. (현재 레벨: ${skill.level})`);
		} else {
			console.log(`${skillName}을(를) 배우지 않았습니다.`);
		}
	}
	
	skillUsed(skillName){
		const skill = this.findSkill(skillName);
		
		skill.currentCool = skill.cooltime;
	}
	
	skillCooldown(){
		for(const skill of this._skills){
			if(skill.currentCool > 0){
				skill.currentCool -= 1;
			}
		}
	}
	
	skillCooltimeReset(){
		for(const skill of this._skills){
			skill.currentCool = 0;
			
		}
	}
	async defaultAttack(targetInfo) {
		const target = this.targetSetting(targetInfo);
		const damage = await this.defaultAttackDamage(targetInfo);
		target.takeDamage(damage);
		console.log(
			`${targetInfo.name}에게 기본공격으로 ${damage.toFixed(1)}만큼의 피해를 입혔습니다.`
		);
	}

	async defaultAttackDamage(targetInfo) {
		return new Promise((res, rej) => {
			const target = this.targetSetting(targetInfo);
		// const damage = this.criticalProcedure(this._stats.attackPoint * this._stats.damageAmplify);
		const damage = this._stats.attackPoint * this._stats.damageAmplify;
		const targetStats = target.getCharacterInfo().stats;
		const targetDeffense = targetStats.deffense - this._stats.deffensePierce;
		console.log(this.damageReduce(targetDeffense));
		const resultDamage = damage * this.damageReduce(targetDeffense);

		res(resultDamage);
		});
		
	}

	async skillAttack(skill, targetInfo) {
		const target = this.targetSetting(targetInfo);
		const damage = await this.skillAttackDamage(skill, targetInfo);
		target.takeDamage(damage);
		console.log(
			`${targetInfo.name}에게 ${skill.name}(으)로 ${damage.toFixed(1)}만큼의 피해를 입혔습니다.`
		);
	}

	async skillAttackDamage(skill, targetInfo) {
		return new Promise((res, rej) => {
		const target = this.targetSetting(targetInfo);
		const damage1 =
			(skill.defaultDamage + (skill.level - 1) * skill.increasePerLevel + this._stats.attackPoint * skill.damageFactor) * this._stats.damageAmplify;
		// const damage2 = this.criticalProcedure(damage1);
		const targetStats = target.getCharacterInfo().stats;
		const targetDeffense = targetStats.deffense - this._stats.deffensePierce;
		// return damage2 * this.damageReduce(targetDeffense);
		const resultDamage = damage1 * this.damageReduce(targetDeffense);
		res(resultDamage);
		});
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
		const isOverMaxHp = this._stats.currentHp + amount > this._stats.maxHp;
		if(isOverMaxHp){
			this._stats.currentHp = this._stats.maxHp;
		}else{
			this._stats.currentHp += amount;
		}
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