class Stats {
	constructor(maxHp, currentHp, attackPoint, deffense, deffensePierce, damageAmplify) {
		this.maxHp = maxHp;
		this.currentHp = currentHp;
		this.attackPoint = attackPoint;
		this.deffense = deffense;
		this.deffensePierce = deffensePierce;
		this.damageAmplify = damageAmplify;
	}
}

module.exports = {Stats};