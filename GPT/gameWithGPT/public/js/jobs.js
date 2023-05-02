const fs = require('fs');

// 전직 정보와 스킬을 담을 클래스
class Job {
  constructor(name, skills, nextJob) {
    this.name = name;
    this.skills = skills;
		this.nextJob = nextJob;
  }
}

// 전직 정보와 스킬을 담은 배열
async function loadJobs() {
  const response = await fs.readFileSync("../../Database/jobs.json");
  const jobsData = await JSON.parse(response);
  const jobs = [];
  for (const data of jobsData) {
    const job = new Job(jobsData.name, jobsData.skills, jobsData.nextJob);
    jobs.push(job);
  }
  return jobs;
}


const jobs = loadJobs();

module.exports = {Job, jobs};
