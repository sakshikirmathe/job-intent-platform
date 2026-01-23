import json
from typing import List, Dict
from search import keyword_search

REQUIRED_FIELDS = {"job_id", "title", "skills", "location", "experience"}


def is_valid_job(job: Dict) -> bool:
    return REQUIRED_FIELDS.issubset(job.keys())


def normalize_job(job: Dict) -> Dict:
    """Normalize text fields for consistent searching."""
    return {
        "job_id": job["job_id"],
        "title": job["title"].strip().lower(),
        "skills": sorted({skill.strip().lower() for skill in job["skills"]}),
        "location": job["location"].strip().lower(),
        "experience": job["experience"].strip().lower(),
    }


def load_jobs(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        raw_jobs = json.load(f)

    valid_jobs = []
    for job in raw_jobs:
        if is_valid_job(job):
            valid_jobs.append(normalize_job(job))

    return valid_jobs


def main():
    jobs = load_jobs("data/jobs.json")
    results = keyword_search(jobs, "numbers")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
