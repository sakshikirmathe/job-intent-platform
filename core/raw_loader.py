import csv
from pathlib import Path
from typing import List, Dict


def load_raw_jobs(path: Path) -> List[Dict]:
    """
    Load raw job data from a CSV file without any cleaning.
    """
    rows = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    return rows


def inspect_raw_data(rows: List[Dict]):
    """
    Print basic inspection metrics for raw data.
    """
    if not rows:
        print("No data found.")
        return

    print(f"Total rows: {len(rows)}")
    print(f"Columns: {list(rows[0].keys())}")

    print("\nMissing values per column:")
    for column in rows[0].keys():
        missing = sum(1 for row in rows if not row.get(column))
        print(f"  {column}: {missing}")

    print("\nSample rows:")
    for row in rows[:2]:
        print(row)


if __name__ == "__main__":
    data_path = Path("raw/jobs_raw.csv")
    rows = load_raw_jobs(data_path)
    inspect_raw_data(rows)
