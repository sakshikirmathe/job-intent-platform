from typing import List, Dict


def keyword_search(jobs: List[Dict], query: str) -> List[Dict]:
    """
    Keyword search with simple relevance scoring.
    """
    query_terms = query.lower().strip().split()
    scored_results = []

    for job in jobs:
        score = 0

        for term in query_terms:
            if term in job["title"]:
                score += 3  # title is important

            if any(term in skill for skill in job["skills"]):
                score += 1  # skills are secondary

        if score > 0:
            scored_results.append((score, job))

    # sort by score (highest first)
    scored_results.sort(key=lambda x: x[0], reverse=True)

    # return only jobs
    return [job for score, job in scored_results]
