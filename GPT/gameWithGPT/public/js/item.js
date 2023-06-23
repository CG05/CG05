const fs = require('fs');

// 전체 아이템 목록을 담을 클래스
class Item {
  constructor(name, type, rarity, job, stats, set) {
    this.name = name;
    this.type = type;
		this.rarity = rarity;
		this.job = job;
    this.stats = stats;
		this.set = set;
  }
}

// 전체 아이템 목록을 담은 배열

async function loadItems() {
  const response = await fs.readFileSync("../../Database/items.json");
  const itemsData = await JSON.parse(response);
  const items = [];
  for (const data of itemsData) {
    const item = new Item(data.name, data.type, data.rarity, data.job, data.stats, data.set);
    items.push(item);
  }
  return items;
}
async function loadBossItems() {
  const response = await fs.readFileSync("../../Database/bossItems.json");
  const itemsData = await JSON.parse(response);
  const items = [];
  for (const data of itemsData) {
    const item = new Item(data.name, data.type, data.rarity, data.job, data.stats, data.set);
    items.push(item);
  }
  return items;
}

const Items = loadItems();

const BossItems = loadBossItems();

module.exports = {Item, Items, BossItems};