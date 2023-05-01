class Node {
	constructor(name, edges) {
		this.name = name; // 노드의 이름
		this.edges = edges; // 이 노드와 연결된 다른 노드들의 리스트
	}
}

const nodes = [
	new Node(0, [1, 2, 3]),
	new Node(1, [0, 4, 5]),
	new Node(2, [0, 6, 7]),
	new Node(3, [0, 8, 9]),
	new Node(4, [1]),
	new Node(5, [1]),
	new Node(6, [2]),
	new Node(7, [2]),
	new Node(8, [3]),
	new Node(9, [3]),
	new Node(10, [11]),
	new Node(11, [10, 12]),
	new Node(12, [11, 13, 14]),
	new Node(13, [12]),
	new Node(14, [12, 15]),
	new Node(15, [14]),
];

function drawMap() {
	// 노드들을 초기화합니다.
	const nodes = new vis.DataSet([]);

	// 간선들을 초기화합니다.
	const edges = new vis.DataSet([]);

	// 노드를 추가합니다.
	nodes.add([
		{ id: 1, label: '시작', color: 'lightgreen' },
		{ id: 2, label: '전투 1', color: 'red' },
		{ id: 3, label: 'NPC 이벤트 1', color: 'orange' },
		{ id: 4, label: '전투 2', color: 'red' },
		{ id: 5, label: 'NPC 이벤트 2', color: 'orange' },
		{ id: 6, label: '전투 3', color: 'red' },
		{ id: 7, label: 'NPC 이벤트 3', color: 'orange' },
		{ id: 8, label: '전투 4', color: 'red' },
		{ id: 9, label: 'NPC 이벤트 4', color: 'orange' },
		{ id: 10, label: '전투 5', color: 'red' },
		{ id: 11, label: 'NPC 이벤트 5', color: 'orange' },
		{ id: 12, label: '전투 6', color: 'red' },
		{ id: 13, label: 'NPC 이벤트 6', color: 'orange' },
		{ id: 14, label: '전투 7', color: 'red' },
		{ id: 15, label: 'NPC 이벤트 7', color: 'orange' },
		{ id: 16, label: '휴식', color: 'lightblue' },
	]);

	// 간선을 추가합니다.
	edges.add([
		{ from: 1, to: 2 },
		{ from: 1, to: 3 },
		{ from: 2, to: 4 },
		{ from: 2, to: 5 },
		{ from: 3, to: 6 },
		{ from: 3, to: 7 },
		{ from: 4, to: 8 },
		{ from: 4, to: 9 },
		{ from: 5, to: 10 },
		{ from: 5, to: 11 },
		{ from: 6, to: 12 },
		{ from: 6, to: 13 },
		{ from: 7, to: 14 },
		{ from: 7, to: 15 },
		{ from: 8, to: 16 },
		{ from: 9, to: 16 },
		{ from: 10, to: 16 },
		{ from: 11, to: 16 },
		{ from: 12, to: 16 },
		{ from: 13, to: 16 },
		{ from: 14, to: 16 },
		{ from: 15, to: 16 },
	]);

	// 그래프 옵션을 설정합니다.
	const options = {
		layout: {
			hierarchical: {
				enabled: true,
				direction: 'UD',
				nodeSpacing: 150,
				levelSeparation: 150,
				blockShifting: true,
				edgeMinimization: true,
			},
		},
		edges: {
			arrows: {
				to: { enabled: true, scaleFactor: 1, type: 'arrow' },
			},
		},
		physics: {
			enabled: false,
		},
		nodes: {
			shape: 'box',
			font: {
				size: 24,
			},
		},
	};
}