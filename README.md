# Classic Book ETL Pipeline — *The Imitation of Christ*

> A structured, bilingual data pipeline for spiritual and linguistic insight.

![Status](https://img.shields.io/badge/status-in_progress-yellow)

##  Problem Statement

Most classic spiritual texts are available in multiple languages, but rarely are they presented in a format that allows **structured, bidirectional comparison** between the original and its translation. Scholars, students, and spiritually curious readers alike often want to ask:
- “What is the Latin original of this English phrase?”
- “How are certain key spiritual terms rendered across the text?”
- “Is the paragraph structure preserved across languages?”

But without a structured dataset, these questions are hard to answer — especially at scale.

##  Vision and Goals

This project aims to create a **clean, bilingual, paragraph-aligned dataset** of *The Imitation of Christ* in Latin and English — stored in a SQL database and fully queryable — to support:

- **Semantic lookup**: Find the Latin equivalent of an English passage, and vice versa
- **Translation analysis**: Explore how Latin words and themes are rendered in context
- **Concept tracking**: Follow the use of key spiritual terms like *humilitas*, *gratia*, or *imitatio*
- **Structural exploration**: Analyze the organization of the book — books, chapters, paragraphs, and frequency
- **Study tools**: Enable the creation of flashcards, translation exercises, and personal study aids

##  Project Scope and ETL Design

This is a handcrafted ETL (Extract–Transform–Load) pipeline, written in Python and SQL. It demonstrates data engineering principles applied to a real-world, text-centric domain.

### **1. Extract**

- Scraped the Latin text from *The Latin Library*
- Scraped the English text from *Christian Classics Ethereal Library*
- Stored raw texts in plain `.txt` files, preserving natural paragraph breaks

### **2. Transform**

- Aligned each book manually by paragraph (over 600 matches)
- Ensured semantic and structural coherence across languages
- Saved bilingual TSV files per book
- Cleaned aligned data to remove inconsistencies, normalize formatting.
- Split in two TSV files and prepare for loading.

### **3. Load**

- Designed PostgreSQL schema
- Loaded cleaned bilingual TSVs into PostgreSQL using SQL scripts
- Ready for complex queries, joins, NLP tasks, or downstream tools (e.g., flashcard generators)

## 📊 Example Use Cases

Once the data is loaded, it becomes a powerful tool for:

- Searching for Latin equivalents of English passages
- Analyzing how a spiritual concept (e.g., “grace”) is expressed across the text
- Creating datasets for Latin language learners or theology students
- Exploring paragraph frequency, length, and structure across books
- Generating dynamic flashcards and quizzes from the text

## 🧱 Tech Stack

- **Languages**: Python, SQL
- **Tools**: VS Code, Git, GitHub, pgAdmin, PostgreSQL
- **Practices**: Modular design, idempotent scripts, error logging, CLI-ready scripts

## 📁 File Structure

```
classicbook-etl-pipeline/
├── data/
│   ├── aligned/
│   │   ├── book1_aligned.tsv
│   │   ├── book2_aligned.tsv
│   │   ├── book3_aligned.tsv
│   │   └── book4_aligned.tsv
│   ├── cleaned/
│   │   ├── archive/
│   │   ├── imitation_cleaned.tsv
│   │   └── README.md
│   ├── raw/
│   │   ├── english_kempis.txt
│   │   ├── latin_kempis.txt
│   │   └── README.md
│   ├── split/
│   │   └── README.md
│   └── README.md
├── templates/
│   └── latin_alignment_template.csv
├── docs/
├── logs/
│   └── README.md
├── requirements.txt
├── scripts/
│   ├── archive/
│   │   ├── clean_bookI.py
│   │   ├── clean_bookII.py
│   │   ├── clean_bookIII.py
│   │   ├── clean_bookIV.py
│   │   └── README.md
│   ├── extract/
│   │   ├── extract_english.py
│   │   ├── extract_latin.py
│   │   └── README.md
│   ├── transform/
│   │   ├── clean_imitation.py
│   │   └── README.md
│   └── README.md
├── tools/
├── venv/
└── README.md
```


## 🧪 Engineering Principles

- **Idempotency**: Scripts can run multiple times without duplicating or corrupting data
- **Error Handling**: Exceptions are caught and logged to improve robustness
- **Modularity**: Separate scripts for each ETL stage improve clarity and maintainability
- **CLI Execution**: `python run_pipeline.py` runs the pipeline end-to-end

## ✍️ Reflections

> “Scientia est ordinatio rerum in ratione.”  
> *Knowledge is the ordering of things according to reason.*

This project was more than an academic or technical exercise — it was a spiritual and intellectual labor. Manual alignment was slow, but meaningful. It mirrors the discipline of a data engineer: **trust in structure, reverence for clarity, and devotion to detail**.

## 🔮 Future Work

- Automate bilingual alignment using rule-based heuristics
- Migrate the PostgreSQL database to a cloud instance (e.g., AWS RDS)
- Integrate Airflow or dbt for orchestration
- Extend the pipeline to other classical works (e.g., Saint Augustine)

## 👤 Author

**Juan D. Bravo**  
Aspiring Data Engineer with a background in classical languages and philosophy.  
Bridging ancient texts with modern data pipelines.
