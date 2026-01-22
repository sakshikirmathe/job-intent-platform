from typing import List, Dict


def keyword_search(jobs: List[Dict], query: str) -> List[Dict]:
    """
    Multi-word, partial keyword search over job title and skills.
    """
    query_terms = query.lower().strip().split()
    results = []

    for job in jobs:
        searchable_text = " ".join(
            [job["title"]] + job["skills"]
        )

        for term in query_terms:
            if term in searchable_text:
                results.append(job)
                break

    return results
