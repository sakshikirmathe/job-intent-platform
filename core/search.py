from typing import List, Dict


def keyword_search(jobs: List[Dict], query: str) -> List[Dict]:
    """
    Simple keyword search over job title and skills.
    """
    query = query.lower().strip()
    results = []

    for job in jobs:
        if query in job["title"]:
            results.append(job)
            continue

        if any(query in skill for skill in job["skills"]):
            results.append(job)

    return results
