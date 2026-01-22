import json
from typing import List, Dict


def load_jobs(path: str) -> List[Dict]:
    """
    Load job data from a JSON file.

    Args:
        path (str): Path to jobs JSON file

    Returns:
        List[Dict]: List of job records
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    jobs = load_jobs("data/jobs.json")
    print(f"Loaded {len(jobs)} job(s)")
    print(jobs)


if __name__ == "__main__":
    main()
