"""
genrate_latin_alignment_csv.py

Creates a CSV file with one column of Latin paragraphs and a blank column for manual English alignment.
Output: Desktop/latin_alignment_sheet.csv


"""

import os
import csv

# Define base project directory and output file path
base_dir = os.path.expanduser("~/GitHubRepos/classicbook-etl-pipeline")
output_path = os.path.join(base_dir, "processed_data", "latin_paragraphs.csv")

# Define the input path for the raw Latin text
latin_input = os.path.expanduser("~/GitHubRepos/classicbook-etl-pipeline/raw_data/latin_kempis.txt")

# Step 1: Read the full contents of the Latin text file
with open(latin_input, "r", encoding="utf-8") as f:
    contents = f.read()  # The entire file content is stored in 'contents'

# Step 1: Read the full contents of the Latin text file
paragraphs = contents.split("\n\n")

# Step 3: Clean each paragraph (trim whitespace) and filter out empty entries
paragraphs = [p.strip() for p in paragraphs if p.strip()]

# Step 4: Ensure the output directory exists before attempting to write
os.makedirs("processed_data", exist_ok=True)

# Step 5: Write the cleaned paragraphs to a CSV file for manual English alignment
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)  # Creates a writer object
    writer.writerow(["Latin Paragraph", "English Paragraph (Manual)"])  # Write CSV header
    for paragraph in paragraphs:
        writer.writerow([paragraph, ""]) # Leave English column blank for manual alignment
