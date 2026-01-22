# Data ingestion logic will live here
import json

with open("data/jobs.json") as f:
    jobs = json.load(f)
print(jobs)
