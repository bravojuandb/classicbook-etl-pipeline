## Transform Phase Overview

This stage prepares the cleaned and enriched version of The Imitation of Christ, 
ready to be loaded into a database for analysis. 
It includes manual alignment, structured cleaning, and enrichment with metadata.

[← Back to Main README](../../README.md)

### Scripts Overview

#### 1. `create_template.py`
- **Purpose**: Generates a manual alignment template as a CSV file.
- **Usage**: Run this script when you need to manually align Latin and English paragraphs.
- **Output**: A file named `manual_template.csv` containing raw English and Latin paragraphs side-by-side for human alignment.
- **Output location**: `data/manual_template.csv`

#### 2. `clean_kempis.py`
- **Purpose**: Applies structural and textual cleaning to the aligned `.tsv` files.
- **Function**: Exposes a function `clean_aligned_book(book_number)` that:
  - Loads `book{n}_aligned.tsv` from `data/aligned/`
  - Strips whitespace, removes numbering artifacts, and standardizes formatting
  - Returns a cleaned `pandas.DataFrame` with `latin_text` and `english_text` columns.

#### 3. `enrich_kempis.py`
- **Purpose**: Main orchestration script for the transform phase.
- **Workflow**:
  - Calls `clean_aligned_book()` from `clean_kempis.py` for each of the four books.
  - Adds metadata such as:
    ```
    paragraphs_fact (future table name)
        • paragraph_id (PK)
        • chapter_id (FK → chapter_dim)
        • book_id (FK → book_dim)
        • paragraph_number
        • latin_text
        • english_text
    ```
- **Output**: A single tab-separated file:  
  `data/cleaned/imitation_cleaned.tsv`

---

### Execution

To run the full transform phase:
```bash
python -m src.transform.enrich_kempis
```