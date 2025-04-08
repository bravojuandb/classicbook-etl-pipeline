# Classic Book ETL Pipeline — *The Imitation of Christ*
![Status](https://img.shields.io/badge/status-in_progress-yellow)

This is a handcrafted end-to-end data engineering project built around *The Imitation of Christ*, a classical spiritual work by Thomas à Kempis. The goal is to demonstrate a complete Extract–Transform–Load (ETL) pipeline using Python and PostgreSQL, while also honoring the depth of the source text.

## Project Overview

- **Goal**: To build a clean, bilingual paragraph-aligned dataset of *The Imitation of Christ* in Latin and English.
- **Tech Stack**: Python, VS Code, GitHub Codespaces, PostgreSQL, SQL.
- **ETL Structure**: 
  - `extract/`: Web scraping and raw data preparation
  - `processed_data/`: Aligned bilingual data in TSV format
  - `sql/`: SQL table creation and sample queries
  - `logs/`: Daily dev journal (learning in public)
  - `README.md`: You are here.

## Motivation

As someone transitioning into data engineering, I wanted to build a pipeline that was technically real, but also personally meaningful.

Instead of using pre-cleaned datasets, I chose to work with a text that matters to me — spiritually and intellectually — to simulate the messiness of real-world data and to stay motivated throughout the process.

I am manually aligning over 600 Latin paragraphs with their English counterparts to ensure semantic integrity. This slow, careful work reflects the discipline required in data engineering — where structure, clarity, and trustworthiness matter more than volume.

## ETL Breakdown

### 1. Extraction
- Scraped Latin text from The Latin Library
- Scraped English text from Christian Classics Ethereal Library
- Cleaned, stripped, and stored paragraphs in plain text files

### 2. Transformation
- Manual alignment of Latin and English paragraphs
- Converted into a tab-separated values file (`kempis_bilingual.tsv`)
- Ensured consistent paragraph IDs and clean formatting

### 3. Load
- Designed and created PostgreSQL schema
- Loaded data using SQL scripts via pgAdmin
- Ready for complex queries, joins, and NLP tasks

## File Structure

- `classicbook_etl_pipeline/`
  - `extract/`
    - `extract_latin.py`
    - `extract_english.py`
    - `combine_texts.py`
  - `raw_data/`
    - `latin_kempis.txt`
    - `english_kempis.txt`
  - `processed_data/`
    - `kempis_bilingual.tsv`
  - `sql/`
    - `create_tables.sql`
  - `logs/`
    - `Daily-log.md`
  - `requirements.txt`
  - `README.md`


## Reflections

<details>
  <summary>“Scientia est ordinatio rerum in ratione.”</summary>

  “Knowledge is the ordering of things according to reason.”
</details>


- This project is teaching me more than just Python and PostgreSQL. It teaches how much care it takes to bring structure to unstructured information — and how data work, like life itself, often requires quiet discipline and long attention.

## Next Steps, for future projects

- Automate bilingual alignment with basic heuristics
- Load dataset into a cloud-based PostgreSQL instance
- Explore using Airflow or dbt for pipeline orchestration
- Extend to other classic works (e.g., Saint Augustine´s works)

## Author

Juan D. Bravo — aspiring Data Engineer with a background in classical studies,
now building a modern skillset with ancient roots.