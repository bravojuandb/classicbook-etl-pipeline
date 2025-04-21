# Transform Scripts

This folder contains the transformation script used to clean and normalize the aligned text  
for the *Classic Book ETL Pipeline*.

## `clean_imitation.py`

This script processes the four manually aligned Latin-English `.tsv` files for *The Imitation of Christ*,  
applies cleaning operations, and generates a single unified output file:

`data/cleaned/imitation_cleaned.tsv`

The following metadata columns are added during transformation:

- `id`: Unique identifier for each row.
- `book`: The book title (I–IV).
- `book_number`: Numerical representation of the book (1–4).
- `chapter_number`: The chapter number within the book.
- `latin_text`: The original Latin paragraph.
- `english_text`: The aligned English paragraph.
- `chapter_id`: A unique identifier combining book and chapter.
- `latin_word_count`: Word count of the Latin paragraph.
- `english_word_count`: Word count of the English paragraph.