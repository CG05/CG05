// 전체 아이템 목록을 담을 클래스
class Item {
  constructor(name, type, rarity, job, stats, chance) {
    this.name = name;
    this.type = type;
		this.rarity = rarity;
		this.job = job;
    this.stats = stats;
		this.chance = chance;
  }
}

// 전체 아이템 목록을 담은 배열

function loadItems() {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "items.json", false);
  xhr.send(null);
  const itemsData = JSON.parse(xhr.responseText);
  const items = [];
  for (const itemData of itemsData) {
    const item = new Item(itemData.name, itemData.type, itemData.rarity, itemData.job, itemData.stats, itemData.chance);
    items.push(item);
  }
  return items;
}

const items = loadItems();

export default {items};