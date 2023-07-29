const fs = require('fs');
const path = require('path');

// 전체 아이템 목록을 담을 클래스
class SetEffect {
  constructor(set, num, stats) {
    this.set = set;
    this.num = num;
    this.stats = stats;

  }
}

// 전체 아이템 목록을 담은 배열

async function loadSetEffects() {
  const response = await fs.readFileSync(path.join(__dirname, "../database/setEffect.json"));
  const setEffectData = await JSON.parse(response);
  
	const setEffects = [];
	return new Promise((res, rej)=>{
		for (const data of setEffectData) {
    	const setEff = new SetEffect(data.set, data.num, data.stats);
    	setEffects.push(setEff);
  	}
		res(setEffects);
	});
}

const setEffects = loadSetEffects();

module.exports = {SetEffect, setEffects};