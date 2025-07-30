# Data Directory

This directory contains three subfolders:

- `aligned/`: Stores the manually aligned versions of the four books of *The Imitation of Christ*. 

- `cleaned/`: Contains the fully cleaned and enriched dataset, prepared and ready for loading into PostgreSQL.

- `raw/`: Contains the original, unprocessed text as extracted from the Latin and English source websites.

- `manual_template.csv` : Template used for manual alignment. Includes one column with Latin text, and a second empty colum for English text. Rows are paragraphs, according to Latin text.