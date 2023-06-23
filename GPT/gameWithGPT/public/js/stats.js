class Stats {
	constructor(maxHp, currentHp, attackPoint, deffense, deffensePierce, damageAmplify, criticalChance, criticalDamage) {
		this.maxHp = maxHp;
		this.currentHp = currentHp;
		this.attackPoint = attackPoint;
		this.deffense = deffense;
		this.deffensePierce = deffensePierce;
		this.damageAmplify = damageAmplify;
		this.criticalChance = criticalChance;
		this.criticalDamage = criticalDamage;
	}
	
}

module.exports = {Stats};