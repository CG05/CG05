const fs = require('fs');

class Node {
	
	constructor(num, type, branch) {
		this.num = num;
		this.type = type;
		this.branch = branch;
	}
	
	// get num(){
	// 	return this.#num;
	// }
	// get type(){
	// 	return this.#type;
	// }
	// set type(type){
	// 	this.#type = type;
	// }
	// get branch(){
	// 	return this.#branch;
	// }
	// set branch(branch){
	// 	this.#branch = branch;
	// }
}

function loadRoute() {
	const route = [];
	for (let i = 1; i < 14; i++) {
		const node = new Node(i, "yet", false);
		route.push(node);
	}
	
	return route;
}

function setNodeType(route) {
	let combatCount = 0;
	let minor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
	while (combatCount < 8) {
		const index = Math.floor(Math.random() * 13);
		console.log(`setTypeIndex: ${index}`);
		const num = index + 1;
		if (minor.includes(num)) {
			if(route[index].type !== undefined){
				minor = minor.filter((number) => (number = num));
				route[index].type = "combat";
				combatCount++;
			}else{
				continue;
			}
			
		} else {
			continue;
		}
	}
	let restCount = 0;
	minor.map((e)=>{
		const option = Math.random();
		if(option > 0.5 && restCount < 1){
			route[e - 1].type = "rest";
			restCount++;
		}else if(option > 0.5){
			route[e - 1].type = "event";
		}else{
			route[e - 1].type = "combat";
		}
	})
	return route;
}

function setNodeBranch(routeA, routeB, routeC) {
	let branchCount = 0;
	let minor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
	while (branchCount < 2) {
		const index = Math.floor(Math.random() * 13);
		console.log(`setBranchIndex: ${index}`);
		const num = index + 1;
		if (minor.includes(num)) {
			const option = Math.random();
			console.log(`option: ${option}`);
			if (option > 0.75 && index < 12) {
				if(!routeA[index + 1].branch){
					minor = minor.filter((number) => (number = num));
					routeB[index].branch = true;
					routeA[index + 1].branch = true;
					branchCount++;
				}
			} else if (option > 0.5 && index > 0) {
				if(!routeA[index - 1].branch){
					minor = minor.filter((number) => (number = num));
					routeB[index].branch = true;
					routeA[index - 1].branch = true;
					branchCount++;
				}
			} else if (option > 0.25 && index < 12) {
				if(!routeC[index + 1].branch){
					minor = minor.filter((number) => (number = num));
					routeB[index].branch = true;
					routeC[index + 1].branch = true;
					branchCount++;
				}
				
			} else if (option > 0 && index > 0) {
				if(!routeC[index - 1].branch){
					minor = minor.filter((number) => (number = num));
					routeB[index].branch = true;
					routeC[index - 1].branch = true;
					branchCount++;
				}
				
			}
			
			continue;
			
		} else {
			continue;
		}
	}
	return [routeA, routeB, routeC];
}

function initRoutes(routeA, routeB, routeC) {
	return setNodeBranch(setNodeType(routeA), setNodeType(routeB), setNodeType(routeC));
}

function displayMap(routes) {
	console.log(routes);
}

module.exports = { Node, loadRoute, initRoutes, displayMap };