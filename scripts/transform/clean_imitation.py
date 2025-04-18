"""
clean_imitation.py

This script performs the data cleaning and combination of four aligned books 
from 'The Imitation of Christ', each stored as a parallel Latin-English .tsv file.

Steps:
1. Define paths and book mapping.
2. Load each aligned book file using a reusable function.
3. Clean text data: strip whitespace and normalize spacing.
4. Add a metadata column: 'book' (Book I, II, III, IV).
5. Concatenate all cleaned books into one DataFrame.
6. Add a global 'id' column to uniquely identify each row.
7. Save the result as 'imitation_cleaned.tsv' for SQL-ready loading.
clean_imitation.py

Final unified script to clean all four aligned books of
'The Imitation of Christ' and output a single TSV file.
"""

import pandas as pd
from pathlib import Path

# Show the script's path (optional, useful for debugging)
print(__file__)

# Define base paths
BASE_DIR = Path(__file__).resolve().parents[2]
INPUT_DIR = BASE_DIR / 'data' / 'aligned'
OUTPUT_PATH = BASE_DIR / 'data' / 'cleaned' / 'imitation_cleaned.tsv'

# Map numeric book ID to full book name
BOOK_NAMES = {
    1: "Book I",
    2: "Book II",
    3: "Book III",
    4: "Book IV"
}

# Function to clean whitespace and normalize spacing in a text column
def clean_text_column(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)

# Function to load, clean, and label a specific book
def clean_and_load_book (book_number: int) -> pd.DataFrame:
    book_label = BOOK_NAMES[book_number]
    input_file = INPUT_DIR / f'book{book_number}_aligned.tsv'
    if not input_file.exists():
        print(f"File not found: {input_file}")
        return None
    
    # Load the TSV file and assign column names
    df = pd.read_csv(input_file, sep='\t', names=["latin_text", "english_text"], encoding='utf-8' )

    # Clean both columns
    df["latin_text"] = clean_text_column(df["latin_text"])
    df["english_text"] = clean_text_column(df["english_text"])

    # Add book label column
    df.insert(0, "book", book_label)

    return df

# Main execution block
if __name__ == "__main__":

    all_books = []

    # Loop through books I–IV, load and clean each
    for book_number in range(1,5):
        df = clean_and_load_book(book_number)
        if df is not None:
            all_books.append(df)

    # Combine all cleaned DataFrames
    combined_df = pd.concat(all_books, ignore_index=True)

    # Add a unique row ID (starts at 1)
    combined_df.insert(0, "id", range(1, len(combined_df) + 1))

    # Make sure output folder exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Save as TSV file (tab-separated, SQL-ready)
    combined_df.to_csv(OUTPUT_PATH, sep="\t", index=False, encoding="utf-8")

    print(f"\n Combined file saved to: {OUTPUT_PATH}")