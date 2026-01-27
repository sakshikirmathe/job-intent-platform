import re
from typing import Dict, List


TITLE_NORMALIZATION_MAP = {
    "jr": "junior",
    "jr.": "junior",
    "analyst - data": "data analyst",
}


SKILL_KEYWORDS = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
]


def normalize_title(title: str) -> str:
    title = title.lower().strip()

    # remove punctuation
    title = re.sub(r"[^a-z\s]", "", title)

    # normalize common phrases first
    title = re.sub(r"\banalyst\s*-\s*data\b", "data analyst", title)

    # normalize jr variations (word-boundary safe)
    title = re.sub(r"\bjr\b|\bjr\b", "junior", title)

    # remove roman numeral levels safely
    title = re.sub(r"\b(i|ii|iii)\b", "", title)

    # collapse whitespace
    title = re.sub(r"\s+", " ", title)

    return title.strip()


def normalize_location(location: str) -> str:
    if not location:
        return "unknown"

    return location.strip().lower()


def extract_skills(text: str) -> List[str]:
    text = text.lower()
    skills = []

    for skill in SKILL_KEYWORDS:
        if skill in text:
            skills.append(skill)

    return sorted(set(skills))


def clean_rows(staged_rows: List[Dict]) -> List[Dict]:
    """
    Clean and normalize staged rows into canonical format.
    """
    cleaned = []

    for row in staged_rows:
        cleaned.append({
            "job_title": normalize_title(row["job_title"]),
            "company": row["company"].strip(),
            "location": normalize_location(row.get("location", "")),
            "description": row["description"].strip(),
            "skills": extract_skills(row["description"]),
        })

    return cleaned
