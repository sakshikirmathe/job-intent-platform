from typing import Dict, List, Tuple


REQUIRED_FIELDS = ["job_title", "company", "description"]


def stage_rows(
    raw_rows: List[Dict]
) -> Tuple[List[Dict], List[Dict]]:
    """
    Validate raw rows against a minimal staging schema.

    Returns:
        staged_rows: rows that passed validation
        rejected_rows: rows that failed, with reasons
    """
    staged_rows = []
    rejected_rows = []

    for idx, row in enumerate(raw_rows):
        errors = []

        # Check required fields
        for field in REQUIRED_FIELDS:
            if not row.get(field) or not row[field].strip():
                errors.append(f"missing_required_field:{field}")

        if errors:
            rejected_rows.append({
                "row_index": idx,
                "row": row,
                "errors": errors,
            })
        else:
            staged_rows.append(row)

    return staged_rows, rejected_rows
