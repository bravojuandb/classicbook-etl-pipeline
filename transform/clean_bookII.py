"""
Script to clean the paralell Latin-English text .tsv file 
for Book II of the Imitation of Christ:

- Read raw aligned text from a TSV file
- Strip whitespace
- Add metadata (book, name, id, paragraph number)
- Save into a final cleaned directory.

"""


import pandas as pd
from pathlib import Path
import re

# Get the base project folder by resolving the parent directory of the script's location
BASE_DIR = Path(__file__).resolve().parent.parent

# Define input/output paths
INPUT_PATH = BASE_DIR / 'processed_data' / 'aligned' / 'book2_aligned.tsv'
OUTPUT_PATH = BASE_DIR / 'processed_data' / 'cleaned' / 'book2_cleaned.tsv'

# Debug paths
print(f"\n This is the script's location: {__file__}")
print(f"\n This is the BASE_DIR: {BASE_DIR}")
print(f"\n This is the INPUT_PATH: {INPUT_PATH}")     
print(f"\n This is the OUTPUT_PATH: {OUTPUT_PATH}\n")


# Ensure that output directory exists
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# Load the aligned TSV file, and assign column names
df = pd.read_csv(INPUT_PATH, sep="\t", encoding="utf-8", names=["latin_text", "english_text"])

# Cleaning the Latin text (ensueres te values are strings, removes whitespaces, normalizes spacing)
df["latin_text"] = df["latin_text"].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)

# Clening trhe English text
df["english_text"] = df["english_text"].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)

# Add the id column, and a unique id number for each row
df.insert(0, "id", range(1, len(df) + 1))

# Add the book column, and assign the same name Book II to each row
df.insert(1, "book", ["Book II"] * len(df))

# Saves the file as TSV
df.to_csv(OUTPUT_PATH, sep="\t", index=False, encoding="utf-8")
print(f"Cleaned file and saved to: {OUTPUT_PATH}\n")