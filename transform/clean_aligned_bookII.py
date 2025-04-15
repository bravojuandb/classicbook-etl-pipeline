"""
Script to cran the paralell Latin-English text .tsv file 
for Book II of the Imitation of Christ:

- Read raw aligned text from a TSV file
- Strip whitespace
- Add metadata (book, name, id, paragraph number)
- Save into a final cleaned directory.

"""

# Import pandas to manipulate data
import pandas as pd

# path class (from pathlib module) to handle file paths in a clean and OS independent way
from pathlib import Path


print(Path(__file__))