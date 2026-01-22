import json
from typing import List, Dict

REQUIRED_FIELDS = {"job_id", "title", "skills", "location", "experience"}


def is_valid_job(job: Dict) -> bool:
    """Check if a job record contains required fields."""
    return REQUIRED_FIELDS.issubset(job.keys())


def load_jobs(path: str) -> List[Dict]:
    """
    Load and validate job data from a JSON file.
    Invalid records are skipped.
    """
    with open(path, "r", encoding="utf-8") as f:
        raw_jobs = json.load(f)

    valid_jobs = [job for job in raw_jobs if is_valid_job(job)]
    return valid_jobs


def main():
    jobs = load_jobs("data/jobs.json")
    print(f"Loaded {len(jobs)} valid job(s)")
    print(jobs)


if __name__ == "__main__":
    main()
