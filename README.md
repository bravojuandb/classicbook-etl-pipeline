# 📚 ETL Pipeline Project — *The Imitation of Christ*  (IN PROGRESS)

This is my personal ETL project for April, where I'm building a full **local data pipeline** using Python and PostgreSQL. The source material is the classic text *De Imitatione Christi* (*The Imitation of Christ*) in Latin and English.

---

## 🧠 Project Goals

- Practice the full ETL process from scratch
- Use meaningful data to stay motivated and consistent
- Document everything for learning and portfolio purposes

---

## 🗂️ Project Structure

classicbook_etl_pipeline/
├── extract/
│   ├── extract_latin.py        # Latin text scraper
│   ├── extract_english.py      # English text scraper 
│   └── combine_texts.py        # Merge Latin + English into bilingual TSV
├── raw_data/
│   ├── latin_kempis.txt
│   └── english_kempis.txt
├── processed_data/
│   └── kempis_bilingual.tsv
├── sql/
│   └── create_tables.sql       # DB schema + sample queries
├── logs/
│   └── YYYY-MM-DD.md           # Daily logs and reflections
├── requirements.txt            # Python dependencies
└── README.md                   

---

## 🔍 Phase 1 — Extract

### 🧪 Latin Text

> Source: [The Latin Library](https://www.thelatinlibrary.com/kempis.html)

- ✅ Fetched index page  
- ✅ Found 4 book links (Liber I–IV)  
- ✅ Extracted and cleaned Latin paragraphs  
- ✅ Saved to `raw_data/latin_kempis.txt`  

📄 Script: `extract_latin.py`  
📦 Output: `latin_kempis.txt`

---

### 🧪 English Text *(coming up)*

> Source: [Christian Classics Ethereal Library (CCEL)](https://www.ccel.org/ccel/kempis/imitation)

- [ ] Write a script to extract English version of the text  
- [ ] Clean and format content  
- [ ] Save to `raw_data/english_kempis.txt`  

📄 Script: `extract_english.py`  
📦 Output: `english_kempis.txt`

---

## 🔄 Phase 2 — Transform (Coming Soon)

- [ ] Align Latin and English paragraphs
- [ ] Save aligned text as `kempis_bilingual.tsv`

📄 Script: `combine_texts.py`  
📦 Output: `processed_data/kempis_bilingual.tsv`

---

## 🗄️ Phase 3 — Load (Coming Soon)

- [ ] Design SQL schema for bilingual text
- [ ] Write `create_tables.sql`
- [ ] Load `.tsv` into PostgreSQL via `psql` or Python

---

## 🛠️ Tools Used

- `requests` — HTTP requests
- `BeautifulSoup` — HTML parsing
- `os` — file handling
- `utf-8` encoding — preserve Latin characters
- PostgreSQL — relational database

---

## 🧾 Requirements

To install dependencies:

```bash
pip install -r requirements.txt