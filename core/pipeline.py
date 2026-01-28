import json
from pathlib import Path

from .raw_loader import load_raw_jobs, inspect_raw_data
from .staging import stage_rows
from .cleaning import clean_rows


OUTPUT_PATH = Path("data/clean_jobs.json")


def run_pipeline():
    """
    Run the data pipeline from raw ingestion to cleaned output.
    """
    print("\n=== PIPELINE STARTED ===")

    # Stage 1: Raw ingestion
    raw_path = Path("raw/jobs_raw.csv")
    print("\n[Stage 1] Loading raw job data...")
    raw_rows = load_raw_jobs(raw_path)

    # Stage 2: Raw inspection
    print("\n[Stage 2] Inspecting raw data...")
    inspect_raw_data(raw_rows)

    # Stage 3: Staging validation
    print("\n[Stage 3] Validating rows (staging)...")
    staged_rows, rejected_rows = stage_rows(raw_rows)

    print(f"Staged rows: {len(staged_rows)}")
    print(f"Rejected rows: {len(rejected_rows)}")

    # Stage 4: Cleaning & normalization
    print("\n[Stage 4] Cleaning staged data...")
    cleaned_rows = clean_rows(staged_rows)

    print(f"Cleaned rows: {len(cleaned_rows)}")

    # Stage 5: Persist cleaned output
    print("\n[Stage 5] Writing cleaned data to disk...")
    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(cleaned_rows, f, indent=2)

    print(f"Cleaned data written to {OUTPUT_PATH}")

    print("\n=== PIPELINE FINISHED ===")


if __name__ == "__main__":
    run_pipeline()
