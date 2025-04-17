"""
clean_imitation.py

Final unified script to clean all four aligned books of
'The Imitation of Christ' and output a single TSV file.
"""

import pandas as pd
from pathlib import Path

print(__file__)

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / 'data' / 'aligned'
OUTPUT_PATH = BASE_DIR / 'data' / 'cleaned' / 'imitation_cleaned.tsv'

BOOK_NAMES = {
    1: "Book I",
    2: "Book II",
    3: "Book III",
    4: "Book IV"
}
