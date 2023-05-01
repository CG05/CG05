// 전체 아이템 목록을 담을 클래스
class Item {
  constructor(name, type, rarity, job, stats, probability) {
    this.name = name;
    this.type = type;
		this.rarity = rarity;
		this.job = job;
    this.stats = stats;
		this.probability = probability;
  }
}

// 전체 아이템 목록을 담은 배열

function loadItems() {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "../Data/items.json", false);
  xhr.send(null);
  const itemsData = JSON.parse(xhr.responseText);
  const items = [];
  for (const itemData of itemsData) {
    const item = new Item(itemData.name, itemData.type, itemData.rarity, itemData.job, itemData.stats, itemData.probability);
    items.push(item);
  }
  return items;
}

const Items = loadItems();

export default {Item, Items};