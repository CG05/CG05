const { Character } = require('./character.js');
const { Enemy, enemies } = require('./enemy.js');
const { Equips } = require('./equips.js');
const {SetEffect, setEffects} = require('./setEffect.js');

class Player extends Character {
	#maxExp;
	#exp;
	#currentPosition;
	#items;
	#equipments;

	constructor(name, level, maxExp, exp, job, stats, skills, currentPosition, items, equipments, gold, shopCount, needMoveOn, focusItem) {
		super(name, level, job, stats, skills);
		this.#maxExp = maxExp;
		this.#exp = exp;
		this.#currentPosition = currentPosition;
		this.#items = items;
		this.#equipments = equipments;
		this.needMoveOn = needMoveOn;
		this.jobline = job.line;
		this.gold = gold;
		this.shopCount = shopCount;
		this.focusItem = focusItem;

	}
	
	async setCheck(){
		const setEffectsList = await setEffects;
		const setMap = this.equipments.checkSetEffect();
		setMap.forEach((value, key) =>{
			for(const setEffect of setEffectsList){
				if(setEffect.set === key && setEffect.num === value){
					setMap.set(key, setEffect);
				}
			}
		});
		return setMap;

	}
	
	async mergeStat(){
		const setMap = await this.setCheck();
		console.log(`before stats:`);
		console.log(this._stats);
		setMap.forEach((value, key) => {
			if(key !== ''){
				console.log(`value.stats:`);
				console.log(value.stats);
				this.setStats(value.stats);
			}
		});
		console.log(`after stats:`);
		console.log(this._stats);
	}

	getCharacterInfo() {
		const characterInfo = {
			name: this._name,
			level: this._level,
			maxExp: this.#maxExp,
			exp: this.#exp,
			job: this._job,
			stats: this._stats,
			skills: this._skills,
			currentPosition: this.#currentPosition,
			items: this.#items,
			equipments: this.#equipments.map,
			gold: this.gold,
			shopCount: this.shopCount,
			needMoveOn: this.needMoveOn,
			focusItem: this.focusItem
		};
		return characterInfo;
	}

	plusExp(exp) {
		this.#exp += exp;
		const diff = this.#exp - this.#maxExp;
		if (diff >= 0) {
			this.levelUp();
			this.#exp = diff;
			return true;
		}
	}

	changeJob(job) {
		this._job = job;
		this.jobline = job.line;
		const lastSkills = this._skills;
		this._skills = [];
		
		for(const skill of job.skills){
			this.addSkill(skill, lastSkills);
		}
	}

	get currentPosition() {
		return this.#currentPosition;
	}

	set currentPosition(position) {
		this.#currentPosition = position;
	}

	get items() {
		return this.#items;
	}
	
	findItem(itemName){
		for(const item of this.#items){
			if(item.name === itemName){
				return item;
			}
		}
		return null;
	}

	pullItem(item) {
		this.#items = this.#items.filter((e) => {
			return e !== item;
		});
	}

	pushItem(item) {
		if(item.name === 'potion'){
			this.#items.unshift(item);
		}else{
			this.#items.push(item);
		}
	}

	get equipments() {
		return this.#equipments;
	}

	pullEquipment(item) {
		this.#equipments.clearType(item.type);
		this.setStats({
			maxHp: (-1) * item.stats.maxHp,
			currentHp: 0,
			attackPoint: (-1) * item.stats.attackPoint,
			deffense: (-1) * item.stats.deffense,
			deffensePierce: 0,
			damageAmplify: 0,
			criticalChance: 0,
			criticalDamage: 0
		});
	}
	isMatchJob(){
		return this.focusItem.job === this.jobline;
	}

	pushEquipment(item) {
		if (item.name !== "potion") {
			this.pullItem(item);
			this.#equipments.set(item);
			this.setStats({
			maxHp: item.stats.maxHp,
			currentHp: item.stats.maxHp,
			attackPoint: item.stats.attackPoint,
			deffense: item.stats.deffense,
			deffensePierce: 0,
			damageAmplify: 0,
			criticalChance: 0,
			criticalDamage: 0
		});
		}else{
			this.pullItem(item);
			this.heal(Math.floor(this._stats.maxHp * 0.3));
		}
	}

	levelUp() {
		this._level += 1;
		//레벨업으로 올라가는 모든 수치 증가
		if(this._level<5){
			this.#maxExp += 8;
		}else if(this._level>=5){
			this.#maxExp += 20;
		}else if(this._level>=10){
			this.#maxExp += 60;
		}else if(this._level>=20){
			this.#maxExp += 100;
		}
		switch(this.jobline){
			case '전사':
				this.setStats({
			maxHp: 50,
			currentHp: 50,
			attackPoint: 2,
			deffense: 3,
			deffensePierce: 0,
			damageAmplify: 0.01,
			criticalChance: 0,
			criticalDamage: 0,
		});
				break;
			case '궁수':
				this.setStats({
			maxHp: 30,
			currentHp: 30,
			attackPoint: 3,
			deffense: 1,
			deffensePierce: 0.3,
			damageAmplify: 0,
			criticalChance: 0.005,
			criticalDamage: 0.015,
		});
				break;
			case '도적':
				this.setStats({
			maxHp: 25,
			currentHp: 25,
			attackPoint: 3,
			deffense: 0.5,
			deffensePierce: 0.5,
			damageAmplify: 0,
			criticalChance: 0.005,
			criticalDamage: 0.01,
		});
				break;
			case '마법사':
				this.setStats({
			maxHp: 25,
			currentHp: 25,
			attackPoint: 2,
			deffense: 0.5,
			deffensePierce: 0.7,
			damageAmplify: 0.02,
			criticalChance: 0,
			criticalDamage: 0,
		});
				break;
			default:
				this.setStats({
			maxHp: 25,
			currentHp: 25,
			attackPoint: 2,
			deffense: 0.5,
			deffensePierce: 0,
			damageAmplify: 0,
			criticalChance: 0,
			criticalDamage: 0,
		});
				break;
		}

		
	}

	targetSetting(info) {
		const targetData = () => {
			return new Enemy(
				info.name,
				info.level,
				info.type,
				info.rarity,
				info.job,
				info.stats,
				info.skills
			);
		};
		return targetData();
	}
	
	async defaultAttack(targetInfo) {
		const target = this.targetSetting(targetInfo);
		const resultDamage = await this.defaultAttackDamage(targetInfo);
		target.takeDamage(resultDamage.damage);
	}
	
	async defaultAttackDamage(targetInfo) {
		return new Promise((res, rej) => {
		const target = this.targetSetting(targetInfo);
		const damage1 = this._stats.attackPoint * this._stats.damageAmplify;
		const criticalResult = this.criticalProcedure(damage1);
		const damage2 = criticalResult.damage;
		const option = criticalResult.isCritical;
		const targetStats = target.getCharacterInfo().stats;
		const targetDeffense = targetStats.deffense - this._stats.deffensePierce;
		console.log(this.damageReduce(targetDeffense));
		const resultDamage = damage2 * this.damageReduce(targetDeffense);

		res({damage: resultDamage, isCritical: option});
		});
		
	}
	
	async skillAttack(skill, targetInfo) {
		const target = this.targetSetting(targetInfo);
		const resultDamage = await this.skillAttackDamage(skill, targetInfo);
		target.takeDamage(resultDamage.damage);
	}
	
	async skillAttackDamage(skill, targetInfo) {
		return new Promise((res, rej) => {
		const target = this.targetSetting(targetInfo);
		const damage1 =
			(skill.defaultDamage + (skill.level - 1) * skill.increasePerLevel + this._stats.attackPoint * skill.damageFactor) * this._stats.damageAmplify;
		const criticalResult = this.criticalProcedure(damage1);
		const damage2 = criticalResult.damage;
		const option = criticalResult.isCritical;
		const targetStats = target.getCharacterInfo().stats;
		const targetDeffense = targetStats.deffense - this._stats.deffensePierce;
		const resultDamage = damage2 * this.damageReduce(targetDeffense);
		res({damage: resultDamage, isCritical: option});
		});
	}

	criticalProcedure(damage) {
		let d;
		let option;
		if (Math.random() * 100 <= this._stats.criticalChance) {
			d = damage * this._stats.criticalDamage;
			option = true;
		} else {
			d = damage;
			option = false;
		}

		return {damage: d, isCritical: option};
	}
}

exports.Player = Player;