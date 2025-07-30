"""
clean_imitation.py

This script combines four manually aligned books 
from 'The Imitation of Christ', each stored as a parallel Latin-English .tsv file.

The script also removes the prefix clutter (Cap. 5., 3., CHAPTER, )

The script also creates 5 aditional metadata columns. Giving a final structure of 9 colums:

- id 
- book 
- book_number 
- chapter_number 
- chapter_id 
- latin_text 
- english_text 
- latin_word_count 
- english_word_count

Steps:
1. Define paths and book mappings.
2. Load each aligned book file using a function.
3. Clean Latin and English texts (whitespaces, Cap-Chapter, 2. etc)
4. Add a metadata columns, and include word_count columns.
5. Combine all cleaned books into one DataFrame.
6. Add a global 'id' column to uniquely identify each row.
7. Save the result as 'imitation_cleaned.tsv', ready for SQL loading.


"""

from src.config import INPUT_DIR

import pandas as pd
import re
from pathlib import Path

# === BOOK NAMES ===
BOOK_NAMES = {
    1: "Book I",
    2: "Book II",
    3: "Book III",
    4: "Book IV"
}

# === TEXT CLEANER ===
def clean_text_column(series: pd.Series) -> pd.Series:
    def clean_line(text):
        text = str(text).strip()
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'^(cap\.|chapter)\s*\d*\.*\s*', '', text, flags=re.IGNORECASE)
        text = re.sub(r'^\d+\.\s*', '', text)
        text = re.sub(r'^\.\s*', '', text)
        return text.strip()

    return series.astype(str).apply(clean_line)

# === CLEAN SINGLE BOOK ===
def clean_aligned_book(book_number: int) -> pd.DataFrame:
    book_label = BOOK_NAMES[book_number]
    input_file = INPUT_DIR / f'book{book_number}_aligned.tsv'

    if not input_file.exists():
        print(f"❌ File not found: {input_file}")
        return None

    df = pd.read_csv(input_file, sep='\t', names=["latin_text", "english_text"], encoding='utf-8')

    df["latin_text"] = clean_text_column(df["latin_text"])
    df["english_text"] = clean_text_column(df["english_text"])

    return df