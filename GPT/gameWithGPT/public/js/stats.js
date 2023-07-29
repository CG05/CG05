class Stats {
	constructor(stats) {
		this.maxHp = stats.maxHp;
		this.currentHp = stats.currentHp;
		this.attackPoint = stats.attackPoint;
		this.deffense = stats.deffense;
		this.deffensePierce = stats.deffensePierce;
		this.damageAmplify = stats.damageAmplify;
		this.criticalChance = stats.criticalChance;
		this.criticalDamage = stats.criticalDamage;
	}
	
}

module.exports = {Stats};