# Classic Book ETL Pipeline — *The Imitation of Christ*

HTML extraction, manual alignment of Latin and English texts, transformation, loading to PostgreSQL and analysis.

## CI Status
![Test Pipeline](https://github.com/bravojuandb/classicbook-etl-pipeline/actions/workflows/test-pipeline.yml/badge.svg)


[![Refactoring](https://img.shields.io/badge/Refactoring-in_progress-orange)](#)

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=fff)](#)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker&logoColor=white)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-In_progress%23316192?logo=postgresql&logoColor=white)](#)

---


## Table of Contents
- [Executive Summary](#executive-summary)
- [Problem & Motivation](#problem--motivation)
- [Data Structure & Raw Input](#data-structure--raw-input)
- [Methodology & ETL Architecture](#methodology--etl-architecture)
- [Repository Structure](#repository-structure)
- [Tools & Technologies](#tools--technologies)
- [Setup & Execution](#setup--execution)
- [Results & Sample Insights](#results--sample-insights)
- [Conclusion & Future Improvements](#conclusion--future-improvements)
- [Appendix & Resources](#appendix--resources)

---


## Executive Summary

This ETL project processes The Imitation of Christ (15th c.) by extracting Latin and English texts from HTML sources, cleaning them, and aligning them paragraph by paragraph. The final output is a structured table ready for loading into SQL and analysis. It combines data engineering techniques with classical scholarship.

---


##  Problem & Motivation

Most classic spiritual texts are available in multiple languages, but rarely are they presented in a format that allows **structured, bidirectional comparison** between the original and its translation. Scholars, students, and spiritually curious readers alike often want to ask:

- “What is the Latin original of this English phrase?”
- “How are certain key spiritual terms rendered across the text?”
- “Is the paragraph structure preserved across languages?”

---


## Data Structure & Raw Input

Info bout the book structure. Granearl description of raw books, aspects to be cleaned.

---


##  Methodology & ETL Architecture

This pipeline follows a modular DAG-style architecture consisting of seven sequential tasks (T1–T7), reflecting the canonical **Extract → Transform → Load** pattern, with a final query/reporting stage.

Although currently executed via CLI or manually, the design anticipates automation and orchestration (e.g., using Airflow) by separating concerns and defining task dependencies clearly.

```
               EXTRACT
              =========
T1: extract_english.py   ───┐
                            ├──▶ T3: create_template.py
T2: extract_latin.py     ───┘

              TRANSFORM (Part 1)
              ==================
T3: create_template.py ──▶ T4: MANUAL ALIGNMENT AND SAVING
                                     │
                                     ▼
              TRANSFORM (Part 2)
              ==================
                           T5: clean_book.py
                                     │
                                     ▼
                           T6: enrich_book.py

                   LOAD
                 ========
                           T7: load_book.py
                                     │
                                     ▼
               QUERY (Post-Load)
              ============================
                          Sample SQL Queries
```

**[Extract Phase](src/extract/README.md)**

This stage includes two parallel tasks:

- **T1 – `extract_english.py`**: Scrapes English text from the *Christian Classics Ethereal Library*.
- **T2 – `extract_latin.py`**: Scrapes Latin text from *The Latin Library*.

Each task outputs a raw `.txt` file (one per language).

**Transform**

This stage is divided into two phases:

- **Transform Part 1**:
  - **T3 – `create_template.py`**: Generates a template to assist with bilingual alignment.
  - **T4 – Manual Alignment**: The user manually aligns Latin and English texts side by side using the template, then saves the result.

- **Transform Part 2**:
  - **T5 – `clean_book.py`**: Cleans and formats the aligned text, ensuring consistency and removing noise.
  - **T6 – `enrich_book.py`**: Adds derived fields such as word count and paragraph number.

**Load**

- **T7 – `load_book.py`**: Loads the final, cleaned and enriched bilingual dataset into a PostgreSQL database.

**Query (Post-Load)**

A set of predefined SQL queries runs automatically after loading, generating reports and insights—e.g., most frequent Latin words, alignment integrity checks, etc.

---


## Repository Structure

```
classicbook-etl-pipeline/
├── data/ 
│   ├── raw/                        # Raw text files from Latin and English sources
│   ├── aligned/                    # 4 manually aligned bilingual books (TSV)
│   ├── clean/                      # Final cleaned TSV file for DB loading
│   ├── output/                     #   
│   ├── manual_template.csv         # Template for manual alignment
│   └── README.md
├── src/
│   ├── extract/
│   │   ├── extract_latin.py        # Extracts the Latin text
│   │   ├── extract_english.py      # Extracts the English text
│   │   └── README.md
│   ├── transform/
│   │   ├── create_template.py     # Creates template for manual alignment
│   │   ├── clean_imitation.py      # Cleans and enrich the CSV file
│   │   └── README.md
│   ├── load/
│   │   ├── load_to_sql.py          # Loads final CSV to sql
│   │   └── README.md
    ├── run_pipeline.py             # Main runner: connects E → T → L
│   └── config.py                   # Central configuration module
├── tests/                          # Unit tests (pytest-compatible)
│   ├── test_transform.py
│   └── test_load.py
├── Dockerfile
├── requirements.txt                # Python dependencies
├── .gitignore
├── README.md                       # Project overview and instructions
└── LICENSE
```
---


##  Tools & Technologies

- **Languages**: Python, SQL, Bash
- **Data Tools**: PostgreSQL, pgAdmin
- **Development Tools**: VS Code, Git, GitHub, Docker
- **Python Libraries**: pandas, requests, BeautifulSoup, pathlib, logging
- **Other**: GitHub Codespaces (optional), Markdown, CLI workflows

---


## Setup & Execution

How to Run the Extract Phase.

> Disclaimer:The full pipeline is under active refactoring. However, the Extract Phase is complete and fully Dockerized.

### 1. Clone the Repository

```bash
git clone https://github.com/juan-dbravo/classicbook-etl-pipeline.git
cd classicbook-etl-pipeline
```

### 2. Option A — Run Locally (Python)

#### Requirements

- Python 3.10+
- `venv` (recommended)
- Install dependencies:

```bash
pip install -r requirements.txt
```

#### Run the extract phase:

```bash
python -m src.run_pipeline
```

This will:
- Extract the English version of *The Imitation of Christ* from Project Gutenberg
- Scrape the Latin version from The Latin Library
- Save both as `.txt` files into `data/raw/`

```text
data/raw/
├── raw_english_kempis.txt
└── raw_latin_kempis.txt
```

---

### 3. Option B — Run with Docker

#### Build the image

From the root of the repo:

```bash
docker build -t classicbook-extract .
```

#### Run the container

**For macOS/Linux:**

```bash
docker run --rm \
  -v "$HOME/classicbook_output:/app/data" \
  classicbook-extract
```

**For Windows (PowerShell):**

```powershell
docker run --rm `
  -v "${HOME}\classicbook_output:/app/data" `
  classicbook-extract
```

**For Windows (CMD):**

```cmd
docker run --rm -v %USERPROFILE%\classicbook_output:/app/data classicbook-extract
```

This saves the raw files to your desktop (or wherever you choose):

```text
~/classicbook_output/raw/
├── raw_english_kempis.txt
└── raw_latin_kempis.txt
```

> 💡 You can change the `-v` path to any local directory.

---

## Results & Sample Insights

This project aims to create an improved **clean, bilingual, paragraph-aligned dataset** of *The Imitation of Christ* in Latin and English — stored in a SQL database and fully queryable — to support:

- **Semantic lookup**: Find the Latin equivalent of an English passage, and vice versa
- **Translation analysis**: Explore how Latin words and themes are rendered in context
- **Concept tracking**: Follow the use of key spiritual terms like *humilitas*, *gratia*, or *imitatio*
- **Structural exploration**: Analyze the organization of the book — books, chapters, paragraphs, and words frequency

Once the data is loaded, it becomes a powerful tool for:

- Searching for Latin equivalents of English passages
- Analyzing how a spiritual concept (e.g., “grace”) is expressed across the text
- Creating datasets for Latin language learners or theology students
- Exploring paragraph frequency, length, and structure across books
- Generating dynamic flashcards and quizzes from the text


[`sql/sample_queries.md`](./sql/sample_queries.md)

This includes:

- Retrieving the Latin title of each book
- Counting verses by book
- Searching for keywords in Latin
- Comparing word counts between Latin and English

---

## Conclusion & Future Improvements

> “Scientia est ordinatio rerum in ratione.”  
> *Knowledge is the ordering of things according to reason.*

This project is a spiritual and intellectual labor. Manual alignment was slow, but meaningful.
 It mirrors the discipline of a data carftsman: **trust in structure, reverence for clarity, and attention to detail**.

---

## Appendix & Resources

### Sources:

- **English text**: [Project Gutenberg](https://www.gutenberg.org/cache/epub/1653/pg1653-images.html)  
- **Latin text**: [The Latin Library](https://www.thelatinlibrary.com/kempis.html)

- **[Short article about the Book Itself](https://en.wikipedia.org/wiki/The_Imitation_of_Christ)**
---

**Juan David Bravo** 

Aspiring Data Engineer with a background in classical languages and philosophy.  
Bridging ancient texts with modern data pipelines.

---
