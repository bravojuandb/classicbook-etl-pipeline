"""
create_template.py

Creates a CSV file with one column of Latin paragraphs and a blank column for manual English alignment.
Output: Desktop/latin_alignment_sheet.csv


"""


import csv
from pathlib import Path
from src.config import LATIN_RAW_FILE, TEMPLATE_OUTPUT_FILE

def read_latin_text(input_path: Path) -> list[str]:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    with input_path.open("r", encoding="utf-8") as f:
        contents = f.read()
    
    paragraphs = [p.strip() for p in contents.split("\n\n") if p.strip()]
    return paragraphs

def write_alignment_template(paragraphs: list[str], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Latin Paragraph", "English Paragraph (Manual)"])
        for paragraph in paragraphs:
            writer.writerow([paragraph, ""])

def main():
    paragraphs = read_latin_text(LATIN_RAW_FILE)
    write_alignment_template(paragraphs, TEMPLATE_OUTPUT_FILE)

if __name__ == "__main__":
    main()