# Transform Scripts

This folder contains transformation scripts used to clean and normalize text data
for the "Classic Book ETL Pipeline".

## `clean_imitation.py`

This script reads the four manually aligned Latin-English `.tsv` files for *The Imitation of Christ*, cleans them, and produces a single output file:  
`data/cleaned/imitation_cleaned.tsv`

Metadata like `book` and `id` columns are added during the process.