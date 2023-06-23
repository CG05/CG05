class Equips {
	constructor(map) {
		this.map = map;
	}
	indexOfType(type) {
		let i = 0;
		for (const equip of this.map) {
			if (equip[0] === type) {
				return i;
			}
			i++;
		}
		return -1;
	}
	indexOfName(name) {
		let i = 0;
		for (const equip of this.map) {
			if (equip[1].name === name) {
				return i;
			}
			i++;
		}
		return -1;
	}

	get(name) {
		const index = this.indexOfName(name);
		if (index > -1) {
			return this.map[index][1];
		} else {
			console.log(`get equip error occured`);
		}
	}

	set(equip) {
		const index = this.indexOfType(equip.type);
		if (index > -1) {
			this.map[index][1] = equip;
		} else {
			console.log(`set equip error occured`);
		}
	}
	
	clearType(type){
		const index = this.indexOfType(type);
		if (index > -1) {
			this.map[index][1] = {name: 'undefined', type: type , set: ''};
		} else {
			console.log(`clear equip type error occured`);
		}
	}
	
	checkSetEffect(){
		const result = {};
		this.forEach((value) => {
			result[value.set] = (result[value.set] || 0) + 1;
		});
		const setEntry = new Map();
		for(const [setName, num] of Object.entries(result)){
			if(num > 2){
				setEntry.set(setName, num);
			}
		}
		return setEntry;
	}
	
	forEach(callbackFunc){
		for (const equip of this.map) {
			const key = equip[0];
			const value = equip[1];
			callbackFunc(value, key);
		}
	}
}

module.exports = { Equips };