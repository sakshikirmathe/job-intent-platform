# Job Intent Platform

An end-to-end data engineering and NLP system for intent-aware job search, built on a production-style data pipeline.  
It focuses on **how intelligent systems are built**: raw ingestion, validation, cleaning, canonical datasets, analytics, and explainable intent handling — with ML added only when justified.

---

## 🔍 Architecture Overview

# Job Intent Platform

An end-to-end data engineering and NLP system for intent-aware job search, built on a production-style data pipeline.  
It focuses on **how intelligent systems are built**: raw ingestion, validation, cleaning, canonical datasets, analytics, and explainable intent handling — with ML added only when justified.

---

## 🔍 Architecture Overview

RAW DATA (CSV)
↓
RAW INGESTION
↓
STAGING & SCHEMA VALIDATION
↓
CLEANING & NORMALIZATION
↓
CANONICAL DATASET (JSON)
↓
INTENT-AWARE SEARCH
↓
SEARCH ANALYTICS & OBSERVABILITY


This separation ensures reliability, extensibility, and clean evolution of NLP and ML layers.

---

## 🚀 Features

### Data Engineering
- Raw data ingestion and inspection
- Staging layer with schema validation
- Cleaning & normalization pipeline
- Canonical dataset as a strict data contract

### NLP & Search
- Intent expansion for vague queries
- Phrase-aware and keyword-based matching
- Explainable search scoring and reasoning

### Analytics
- Persistent logging of search events
- Aggregated metrics (intent usage, zero-result rate)
- Top-query analysis for system evaluation

---

## 📦 Project Structure

core/
pipeline.py # Orchestrates the data pipeline
raw_loader.py # Raw CSV ingestion
staging.py # Schema validation
cleaning.py # Normalization & feature extraction
search.py # Intent-aware search logic
intent.py # Query intent expansion
analytics.py # Search analytics & metrics
ingest.py # Application entry point

raw/
jobs_raw.csv # Raw job data (intentionally messy)

data/
clean_jobs.json # Canonical dataset produced by pipeline

storage/
search_logs.json # Persistent analytics logs


---

## ▶️ How to Run

### 1. Run the data pipeline

python core/pipeline.py

This will:

load raw data

validate and clean it

write data/clean_jobs.json

---
### 2. Run the search application

python core/ingest.py

## Design Philosophy

This project is intentionally pipeline-first.  
Instead of jumping straight to ML, it focuses on clean data contracts,
explainable NLP, and analytics-driven system evolution.

## Roadmap

- Advanced NLP (phrases, synonyms)
- Semantic search with embeddings (hybrid ranking)
- Larger real-world datasets (Kaggle / scraping)
- API layer (FastAPI) and UI




