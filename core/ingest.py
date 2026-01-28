import json
from .search import keyword_search
from .analytics import get_analytics_summary, get_top_queries



def load_jobs(path: str):
    """
    Load already-cleaned job data produced by the pipeline.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    jobs = load_jobs("data/clean_jobs.json")

    query = "Data Engineer"
    results = keyword_search(jobs, query)

    if not results:
        print("No results found.")
        return

    display_intent = results[0].get("display_intent", "")

    if display_intent and display_intent != query:
        print("No direct matches found.")
        print(f"Showing results based on inferred intent: {display_intent}")

    for result in results:
        print(result)

    print("\n--- SEARCH ANALYTICS SUMMARY ---")
    summary = get_analytics_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\n--- TOP QUERIES ---")
    for query, count in get_top_queries():
        print(f"{query}: {count}")


if __name__ == "__main__":
    main()
