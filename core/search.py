from typing import List, Dict
from .intent import expand_query
from .analytics import log_search_event

def keyword_search(jobs: List[Dict], query: str) -> List[Dict]:
    """
    Keyword search with relevance scoring, explainability,
    and intent expansion.
    """
    original_query, expanded_query, display_intent = expand_query(query)
    query_terms = expanded_query.split()

    results = []

    for job in jobs:
        score = 0
        reasons = []

        for term in query_terms:
            if term in job["job_title"]:
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
                "reasons": reasons,
                "expanded_query": expanded_query,
                "display_intent": display_intent
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    intent_used = original_query != expanded_query

    log_search_event(
        original_query=original_query,
        expanded_query=expanded_query,
        result_count=len(results),
        intent_used=intent_used
    )
    return results
