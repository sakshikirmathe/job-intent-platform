from typing import List, Dict


def keyword_search(jobs: List[Dict], query: str) -> List[Dict]:
    """
    Keyword search with relevance scoring and explainability.
    """
    query_terms = query.lower().strip().split()
    results = []

    for job in jobs:
        score = 0
        reasons = []

        for term in query_terms:
            if term in job["title"]:
                score += 3
                reasons.append(f"title match: {term}")

            for skill in job["skills"]:
                if term in skill:
                    score += 1
                    reasons.append(f"skill match: {skill}")

        if score > 0:
            results.append({
                "job": job,
                "score": score,
                "reasons": reasons
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results
