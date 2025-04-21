# Cleaned Data

This `.tsv` file was generated using the script `scripts/transform/clean_imitation.py`.

It contains the cleaned and enriched bilingual text of *The Imitation of Christ*, aligned at the paragraph level. Each row represents a pair of Latin and English paragraphs with corresponding metadata.

## Columns

- `id`: Unique identifier for each row.
- `book`: The book title (I–IV).
- `book_number`: Numerical representation of the book (1–4).
- `chapter_number`: The chapter number within the book.
- `latin_text`: The original Latin paragraph.
- `english_text`: The aligned English paragraph.
- `chapter_id`: A unique identifier combining book and chapter.
- `latin_word_count`: Word count of the Latin paragraph.
- `english_word_count`: Word count of the English paragraph.