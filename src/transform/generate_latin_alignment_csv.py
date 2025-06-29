"""
genrate_latin_alignment_csv.py

Creates a CSV file with one column of Latin paragraphs and a blank column for manual English alignment.
Output: Desktop/latin_alignment_sheet.csv


"""


import csv
from pathlib import Path

# Define base project directory and output file path
base_dir = Path(__file__).resolve().parent.parent

# Define the input path for the raw Latin text
latin_input = base_dir / "data" / "raw" / "latin_kempis.txt"

# Output file (CSV for manual alignment)
output_path = base_dir / "templates" / "latin_alignment_template.csv"

# Ensure input file exists
if not latin_input.exists():
    raise FileNotFoundError(f"Input file not found: {latin_input}")

# Read the full contents of the Latin text file
with latin_input.open("r", encoding="utf-8") as f:
    contents = f.read()  # The entire file content is stored in 'contents'

# Split into paragraphs, strip whitespace, and remove empties
paragraphs = [p.strip() for p in contents.split("\n\n") if p.strip()]

# Ensure the output directory exists before attempting to write
output_path.parent.mkdir(parents=True, exist_ok=True)

# Write the cleaned paragraphs to a CSV file for manual English alignment
with output_path.open("w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)  # Creates a writer object
    writer.writerow(["Latin Paragraph", "English Paragraph (Manual)"])  # Write CSV header
    for paragraph in paragraphs:
        writer.writerow([paragraph, ""]) # Leave English column blank for manual alignment
