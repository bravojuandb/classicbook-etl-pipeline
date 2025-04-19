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
import pandas as pd
import re
from pathlib import Path

# === FILE PATHS ===
BASE_DIR = Path(__file__).resolve().parents[2]
INPUT_DIR = BASE_DIR / 'data' / 'aligned'
OUTPUT_PATH = BASE_DIR / 'data' / 'cleaned' / 'imitation_cleaned.tsv'

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

        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)

        # Remove chapter/section markers (case-insensitive)
        text = re.sub(r'^(cap\.|chapter)\s*\d*\.*\s*', '', text, flags=re.IGNORECASE)

        # Remove number prefixes like "1." or "3.2.1"
        text = re.sub(r'^\d+\.\s*', '', text)

        # Remove dots before letters: ".quod", ".philly" → "quod", "philly"
        text = re.sub(r'^\.\s*', '', text)

        return text.strip()

    return series.astype(str).apply(clean_line)

# === WORD COUNTER ===
def word_count(text):
    return len(re.findall(r'\b\w+\b', str(text)))

# === LOAD AND ENRICH BOOK DATA ===
def clean_and_load_book(book_number: int) -> pd.DataFrame:
    book_label = BOOK_NAMES[book_number]
    input_file = INPUT_DIR / f'book{book_number}_aligned.tsv'

    if not input_file.exists():
        print(f"❌ File not found: {input_file}")
        return None

    # Load TSV with two unnamed columns
    df = pd.read_csv(input_file, sep='\t', names=["latin_text", "english_text"], encoding='utf-8')

    # Clean both text columns
    df["latin_text"] = clean_text_column(df["latin_text"])
    df["english_text"] = clean_text_column(df["english_text"])

    # Add metadata columns
    df.insert(0, "book", book_label)
    df.insert(1, "book_number", book_number)
    df.insert(2, "chapter_number", range(1, len(df) + 1))

    roman = ["I", "II", "III", "IV"][book_number - 1]
    df["chapter_id"] = roman + '.' + df["chapter_number"].astype(str)

    # Add word counts
    df["latin_word_count"] = df["latin_text"].apply(word_count)
    df["english_word_count"] = df["english_text"].apply(word_count)

    return df

# === MAIN PIPELINE ===
if __name__ == "__main__":
    all_books = []

    for book_number in range(1, 5):
        df = clean_and_load_book(book_number)
        if df is not None:
            all_books.append(df)

    # Combine all books
    combined_df = pd.concat(all_books, ignore_index=True)

    # Add global row ID
    combined_df.insert(0, "id", range(1, len(combined_df) + 1))

    # Ensure output directory exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Export to TSV
    combined_df.to_csv(OUTPUT_PATH, sep='\t', index=False, encoding='utf-8')

    print(f"\n✅ Clean enriched file saved to: {OUTPUT_PATH}")