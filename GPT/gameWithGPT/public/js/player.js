const { Character } = require('./character.js');
const { Enemy, enemies } = require('./enemy.js');

class Player extends Character {
	#maxExp;
	#exp;
	#currentPosition;
	#items;
	#equipments;

	constructor(name, level, maxExp, exp, job, stats, skills, currentPosition, items, equipments) {
		super(name, level, job, stats, skills);
		this.#maxExp = maxExp;
		this.#exp = exp;
		this.#currentPosition = currentPosition;
		this.#items = items;
		this.#equipments = equipments;
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
			equipments: this.#equipments,
		};
		return characterInfo;
	}

	setCharacterInfo(characterInfo) {
		const info = this.getCharacterInfo();
		for (const key in characterInfo) {
			if (characterInfo.hasOwnProperty(key)) {
				info[key] = characterInfo[key];
			}
		}
		this._name = info.name;
		this._level = info.level;
		this.#maxExp = info.maxExp;
		this.#exp = info.exp;
		this._job = info.job;
		this._stats = info.stats;
		this._skills = info.skills;
		this.#currentPosition = info.currentPosition;
		this.#items = info.items;
		this.#equipments = info.equipments;
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

	pullItem(item) {
		this.#items.pull(item);
	}

	pushItem(item) {
		this.#items.push(item);
	}

	get equipments() {
		return this.#equipments;
	}

	pullEquipment(item) {
		this.#equipments.pull(item);
	}

	pushEquipment(item) {
		if (item !== null) {
			this.#equipments.push(item);
		}
	}

	levelUp() {
		this._level += 1;
		//레벨업으로 올라가는 모든 수치 증가
		this.#maxExp += 8;

		this.setStats({
			maxHp: 7,
			currentHp: 7,
			attackPoint: 3,
			deffense: 0.5,
			deffensePierce: 0,
			damageAmplify: 0,
		});
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
}

exports.Player = Player;