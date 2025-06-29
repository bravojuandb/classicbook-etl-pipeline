# 📊 ClassicBook ETL – SQL Schema

This schema represents the cleaned and enriched version of *The Imitation of Christ*, ready for querying in SQL.

## Table: imitation

| Column Name        | Type     | Description                                                   |
|--------------------|----------|---------------------------------------------------------------|
| id                 | INTEGER  | Unique identifier for each row                                |
| book               | TEXT     | The book title (I, II, III, or IV)                            |
| book_number        | INTEGER  | Numerical representation of the book (1 to 4)                 |
| chapter_number     | INTEGER  | Chapter number within the book                                |
| chapter_id         | TEXT     | A unique identifier combining book and chapter (e.g., I-3)    |
| latin_text         | TEXT     | Original Latin paragraph                                      |
| english_text       | TEXT     | Aligned English paragraph                                     |
| latin_word_count   | INTEGER  | Word count of the Latin paragraph                             |
| english_word_count | INTEGER  | Word count of the English paragraph                           |

---

### 📥 SQL `CREATE TABLE` Script

```sql
CREATE TABLE imitation (
    id INTEGER PRIMARY KEY,
    book TEXT,
    book_number INTEGER,
    chapter_number INTEGER,
    chapter_id TEXT,
    latin_text TEXT,
    english_text TEXT,
    latin_word_count INTEGER,
    english_word_count INTEGER
);