// 전직 정보와 스킬을 담을 클래스
class Job {
  constructor(name, skill) {
    this.name = name;
    this.skill = skill;
  }
}



// 전직 정보와 스킬을 담은 배열
const jobs = [
  new Job("전사", "강력한 일격"),
  new Job("궁수", "멀리서 화살 공격"),
  new Job("법사", "파괴의 화염구"),
];



export default {jobs};
