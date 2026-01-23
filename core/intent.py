INTENT_MAP = {
    "numbers": ["data", "analyst"],
    "analysis": ["data", "analyst"],
    "python": ["data", "engineer"],
    "cloud": ["aws", "data"],
    "excel": ["data", "analyst"],
}


def expand_query(query: str):
    """
    Expand vague queries using intent mapping.

    Returns:
        original_query (str)
        expanded_query (str)   -> used internally for search
        display_intent (str)   -> shown to user
    """
    original_terms = query.lower().strip().split()
    expanded_terms = list(original_terms)
    inferred_terms = []

    for term in original_terms:
        if term in INTENT_MAP:
            inferred_terms.extend(INTENT_MAP[term])
            expanded_terms.extend(INTENT_MAP[term])

    expanded_query = " ".join(sorted(set(expanded_terms)))
    display_intent = " ".join(sorted(set(inferred_terms)))
    original_query = " ".join(original_terms)

    return original_query, expanded_query, display_intent
