# Classic Book ETL Pipeline — *The Imitation of Christ*
![Status](https://img.shields.io/badge/status-in_progress-yellow)

This is a handcrafted end-to-end data engineering project built around *The Imitation of Christ*, a classical spiritual work by Thomas à Kempis. The goal is to demonstrate a complete Extract–Transform–Load (ETL) pipeline using Python and PostgreSQL, while also honoring the depth of the source text.

## Project Overview

- **Goal**: To build a clean, bilingual paragraph-aligned dataset of *The Imitation of Christ* in Latin and English.
- **Tech Stack**: Python, VS Code, GitHub Codespaces, PostgreSQL, SQL.
- **ETL Structure**: 
  - `extract/`: Web scraping and raw data preparation for Latin and English raw texts
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
- Aligned each book of The Imitation of Christ manually, treating them as separate units
- Latin and English paragraphs were carefully reviewed and matched to ensure semantic fidelity
- Prepared each book for loading into SQL
- Each book is saved as an individual TSV file (e.g., book1_aligned.tsv)

### 3. Load
- Designed and created PostgreSQL schema
- Loaded data using SQL scripts via pgAdmin
- Ready for complex queries, joins, and NLP tasks

## File Structure

classicbook-etl-pipeline/
   - README.md
   - requirements.txt

   - extract/                  # 1. EXTRACT — raw text scripts
     - extract_latin.py
     - extract_english.py

   - raw_data/                 # Extracted, untouched texts
     - latin_kempis.txt
     - english_kempis.txt
 
   - transform/                # 2. TRANSFORM — cleaning & alignment scripts
     - clean_aligned_books.py
     -  ...
 
   - processed_data/           # Outputs of the transformation phase
     - manual_alignment/          # Hand-aligned, uncleaned TSVs
     - cleaned_alignment/         # Cleaned TSVs (ready for SQL load)
 
   - sql/                      # 3. LOAD — PostgreSQL schema & queries
     - create_tables.sql

   - tools/                    # Helper scripts (e.g., ID generators)
     - generate_latin_alignment_csv.py

   - logs/                     # Learning journal
     - Daily-log.md

   - docs/                     # Optional design notes / schema ideas

## Principles

- Idempotency: 	Running the script twice doesn’t corrupt or duplicate data
- Logging: Print logs to console or file: "Extracted N texts", "Loaded X rows"
- Error handling:	Catch and log errors in extraction and loading
- CLI executable:	python run_pipeline.py runs the full ETL
- Modular design:	Separate extract, transform, load files


## Reflections

<details>
  <summary>“Scientia est ordinatio rerum in ratione.”</summary>

  “Knowledge is the ordering of things according to reason.”
</details>


- “This slow, careful work reflects the discipline required in data engineering — where structure, clarity, and trustworthiness matter more than volume.”

## Next Steps, for future projects

- Automate bilingual alignment with basic heuristics
- Load dataset into a cloud-based PostgreSQL instance
- Explore using Airflow or dbt for pipeline orchestration
- Extend to other classic works (e.g., Saint Augustine´s works)

## Author

Juan D. Bravo — aspiring Data Engineer with a background in classical studies,
now building a modern skillset with ancient roots.
