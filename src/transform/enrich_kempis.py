"""

"""

from src.config import OUTPUT_PATH

import pandas as pd
from pathlib import Path
from src.transform.clean_kempis import clean_aligned_book

# === BOOK METADATA ===
BOOK_NAMES = {
    1: "Book I",
    2: "Book II",
    3: "Book III",
    4: "Book IV"
}

# === WORD COUNTER ===
def word_count(text):
    return len(str(text).split())

# === ENRICHMENT FUNCTION ===
def enrich_book(df: pd.DataFrame, book_number: int) -> pd.DataFrame:
    book_label = BOOK_NAMES[book_number]
    df.insert(0, "book", book_label)
    df.insert(1, "book_number", book_number)
    df.insert(2, "chapter_number", range(1, len(df) + 1))

    roman = ["I", "II", "III", "IV"][book_number - 1]
    df["chapter_id"] = roman + '.' + df["chapter_number"].astype(str)

    df["latin_word_count"] = df["latin_text"].apply(word_count)
    df["english_word_count"] = df["english_text"].apply(word_count)

    return df

# === MAIN ===
if __name__ == "__main__":
    all_books = []

    for book_number in range(1, 5):
        df = clean_aligned_book(book_number)
        if df is not None:
            enriched = enrich_book(df, book_number)
            all_books.append(enriched)

    combined_df = pd.concat(all_books, ignore_index=True)
    combined_df.insert(0, "id", range(1, len(combined_df) + 1))

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    combined_df.to_csv(OUTPUT_PATH, sep='\t', index=False, encoding='utf-8')

    print(f"\n✅ Clean enriched file saved to: {OUTPUT_PATH}")