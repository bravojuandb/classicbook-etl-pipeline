# Classic Book ETL Pipeline – *The Imitation of Christ*

This project is a hands-on ETL (Extract, Transform, Load) pipeline built around a classic text: *The Imitation of Christ* by Thomas à Kempis.

It demonstrates how to:

- **Extract** both the Latin and English versions from online sources  
- **Transform** the texts into a clean, structured bilingual dataset  
- **Load** the data into a PostgreSQL database for further querying and analysis

The entire pipeline is written in Python, following good data engineering practices:
- Organized folder structure
- Progressive script development
- Clear Git commits and daily logs
- GitHub-hosted, self-contained, and reproducible

Designed as a foundational project to learn core data engineering workflows using meaningful content.
---

## Project Structure

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
    - `2025-04-05.md`
  - `requirements.txt`
  - `README.md`

---

## 🔍 Phase 1 — Extract

### 🧪 Latin Text

> Source: [The Latin Library](https://www.thelatinlibrary.com/kempis.html)

- Fetched index page  
- Found 4 book links (Liber I–IV)  
- Extracted and cleaned Latin paragraphs  
- Saved to `raw_data/latin_kempis.txt`  

📄 Script: `extract_latin.py`  
📦 Output: `latin_kempis.txt`

---

### English Text *(coming up)*

> Source: [Project Gutemberg](https://www.gutenberg.org/cache/epub/1653/pg1653-images.html)

- Write a script to extract English version of the text  
- Make it more portable and sharable using os.getenv()
- Clean and format content  
- Save to `raw_data/english_kempis.txt`  

📄 Script: `extract_english.py`  
📦 Output: `english_kempis.txt`

---

## 🔄 Phase 2 — Transform (Coming Soon)

- [ ] Align Latin and English paragraphs
- [ ] Save aligned text as `kempis_bilingual.tsv`

📄 Script: `combine_texts.py`  
📦 Output: `processed_data/kempis_bilingual.tsv`

---

## Phase 3 — Load (Coming Soon)

- [ ] Design SQL schema for bilingual text
- [ ] Write `create_tables.sql`
- [ ] Load `.tsv` into PostgreSQL via `psql` or Python

---

## Tools Used

- `requests` — HTTP requests
- `BeautifulSoup` — HTML parsing
- `os` — file handling
- `utf-8` encoding — preserve Latin characters
- PostgreSQL — relational database

---

## Requirements

To install dependencies:

```bash
pip install -r requirements.txt