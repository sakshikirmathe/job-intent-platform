import json
from datetime import datetime
from typing import Dict, List
from pathlib import Path

STORAGE_PATH = Path("storage/search_logs.json")


def _load_logs() -> List[Dict]:
    if not STORAGE_PATH.exists():
        return []

    with open(STORAGE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_logs(logs: List[Dict]):
    with open(STORAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)


def log_search_event(
    original_query: str,
    expanded_query: str,
    result_count: int,
    intent_used: bool
):
    logs = _load_logs()

    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "original_query": original_query,
        "expanded_query": expanded_query,
        "result_count": result_count,
        "intent_used": intent_used,
    }

    logs.append(event)
    _save_logs(logs)


def get_search_logs() -> List[Dict]:
    return _load_logs()


def get_analytics_summary() -> Dict:
    logs = _load_logs()
    total_searches = len(logs)

    if total_searches == 0:
        return {
            "total_searches": 0,
            "intent_expansion_rate": 0.0,
            "zero_result_rate": 0.0,
        }

    intent_used_count = sum(1 for log in logs if log["intent_used"])
    zero_result_count = sum(1 for log in logs if log["result_count"] == 0)

    return {
        "total_searches": total_searches,
        "intent_expansion_rate": intent_used_count / total_searches,
        "zero_result_rate": zero_result_count / total_searches,
    }


def get_top_queries(limit: int = 5):
    logs = _load_logs()
    frequency = {}

    for log in logs:
        query = log["original_query"]
        frequency[query] = frequency.get(query, 0) + 1

    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:limit]
