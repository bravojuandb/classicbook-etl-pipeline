# SQL Documentation – ClassicBook ETL

This folder contains all SQL-related components of the **ClassicBook ETL Pipeline**, focused on *The Imitation of Christ*.

## Database Setup

The database was created locally using **pgAdmin 4** and **PostgreSQL**.

- **Database Name**: `Imitation_of_Christ`
- **Schema**: `public`
- **Table Name**: `imitation`
- **Owner/User**: `Christy`

You can find the table creation script in [`schema.md`](./schema.md).

## Table Structure

The table `imitation` contains aligned Latin and English paragraphs, enriched with metadata for book, chapter, and word count analysis.

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

## SQL Queries & Analysis

All executed queries are documented in [`sample_queries.md`](./sample_queries.md). These include:

- Retrieving the Latin title of each book
- Counting verses by book
- Searching for keywords in Latin
- Comparing word counts between Latin and English

Each query is accompanied by a screenshot of the result taken from **pgAdmin**.

## Screenshots

Query result screenshots are stored in the [`screenshots/`](./screenshots) subfolder. These provide visual evidence of the queries and are referenced directly from the sample queries file.

## Tools Used

- [pgAdmin 4](https://www.pgadmin.org/) – GUI for PostgreSQL
- PostgreSQL 14+ – Local database engine

## Purpose

This SQL component serves to:
- Demonstrate data loading into relational databases
- Explore multilingual text alignment and comparison
- Showcase SQL querying as part of a full ETL pipeline

---

> All queries, schemas, and screenshots are created and maintained by **Juan Bravo**, as part of the [ClassicBook ETL Pipeline](https://github.com/juanbravo-dev/classicbook-etl-pipeline) project.
