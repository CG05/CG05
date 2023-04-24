// 전직 정보와 스킬을 담을 클래스
class Job {
  constructor(name, skills, nextJob) {
    this.name = name;
    this.skills = skills;
		this.nextJob = nextJob;
  }
	
	
}

// 전직 정보와 스킬을 담은 배열
function loadJobs() {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "../Data/jobs.json", false);
  xhr.send(null);
  const jobsData = JSON.parse(xhr.responseText);
  const jobs = [];
  for (const jobsData of jobsData) {
    const job = new Enemy(jobsData.name, jobsData.skills, jobsData.nextJob);
    jobs.push(job);
  }
  return jobs;
}

const jobs = loadJobs();

export default {jobs};
