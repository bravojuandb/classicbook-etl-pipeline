"""
Script to cran the paralell Latin-English text .tsv file 
for Book II of the Imitation of Christ:

- Read raw aligned text from a TSV file
- Strip whitespace
- Add metadata (book, name, id, paragraph number)
- Save into a final cleaned directory.

"""

# Import pandas to manipulate data
import pandas as pd

# Path class (from pathlib module) to handle file paths in a clean and OS independent way
from pathlib import Path

import re

# Get the base project folder by resolving the parent directory of the script's location
BASE_DIR = Path(__file__).resolve().parent.parent


INPUT_PATH = BASE_DIR / 'processed_data' / 'aligned' / 'book2_aligned.tsv'
OUTPUT_PATH = BASE_DIR / 'processed_data' / 'cleaned' / 'book2_cleaned.tsv'

# For pedagogic use

print(f"\n This is the script's location: {__file__}")
print(f"\n This is the BASE_DIR: {BASE_DIR}")
print(f"\n This is the INPUT_PATH: {INPUT_PATH}")     
print(f"\n This is the OUTPUT_PATH: {OUTPUT_PATH}\n")


# Ensure that folder exists
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_PATH, sep="\t", encoding="utf-8")

df.columns = ['latin_text', 'english_text']

df['latin_text'] = df['latin_text'].str.strip()
df['english_text'] = df['english_text'].str.strip()

# Replace multiple spaces with a single space
df['latin_text'] = df['latin_text'].str.replace(r'\s+', ' ', regex=True)
df['english_text'] = df['english_text'].str.replace(r'\s+', ' ', regex=True)

# Create a new column for id
df.insert(0, "id", range(1, len(df) + 1))

# Add book column
df.insert[1, "Book II", ["Book II"] * len(df)]