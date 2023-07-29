const fs = require('fs');
const path = require('path');

// 전직 정보와 스킬을 담을 클래스
class Job {
  constructor(name, comment, line, skills, nextJob) {
    this.name = name;
		this.comment = comment;
		this.line = line;
    this.skills = skills;
		this.nextJob = nextJob;
  }
}

// 전직 정보와 스킬을 담은 배열
async function loadJobs() {
  const response = await fs.readFileSync(path.join(__dirname, "../database/jobs.json"));
  const jobsData = await JSON.parse(response);
  
	const _jobs = [];
	return new Promise((res, rej)=>{
		for (const data of jobsData) {
    	const job = new Job(data.name, data.comment, data.line, data.skills, data.nextJob);
    	_jobs.push(job);
  	}
		res(_jobs);
	});
}


const jobs = loadJobs();


module.exports = {Job, jobs};
