from typing import List, Dict
from intent import INTENT_MAP


def keyword_search(jobs: List[Dict], query: str) -> List[Dict]:
    """
    Keyword search with relevance scoring and explainability.
    """
    expanded_query = expand_query(query)
    query_terms = expanded_query.split()
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

def expand_query(query: str) -> str:
    """
    Expand vague queries using intent mapping.
    """
    expanded_terms = query.lower().split()

    for term in expanded_terms:
        if term in INTENT_MAP:
            expanded_terms.extend(INTENT_MAP[term])

    # remove duplicates
    return " ".join(sorted(set(expanded_terms)))
