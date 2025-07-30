"""
General configuration file for the ETL pipeline.

By default, paths are rooted in the current working directory (project root),
but you can override this by setting the PROJECT_ROOT environment variable.
"""

from pathlib import Path
import os

# --------------------------------------------------
# PROJECT ROOT
# --------------------------------------------------

PROJECT_ROOT = Path(os.getenv("PROJECT_ROOT", Path.cwd())).resolve()

# --------------------------------------------------
# RAW DATA DIRECTORY
# --------------------------------------------------

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)  # Create if missing

# --------------------------------------------------
# OUTPUT FILE AND SOURCE FOR ENGLISH TEXT EXTRACTION
# --------------------------------------------------

ENGLISH_RAW_FILE = RAW_DATA_DIR / "raw_english_kempis.txt"
ENGLISH_URL = "https://www.gutenberg.org/cache/epub/1653/pg1653-images.html"

# --------------------------------------------------
# OUTPUT FILE AND SOURCE FOR LATIN TEXT EXTRACTION
# --------------------------------------------------

LATIN_RAW_FILE = RAW_DATA_DIR / "raw_latin_kempis.txt"
BASE_LATIN_URL = "https://www.thelatinlibrary.com"
LATIN_URL = f"{BASE_LATIN_URL}/kempis.html"

# --------------------------------------------------
# ALIGNMENT TEMPLATE PATH (for manual Latin-English alignment)
# --------------------------------------------------

TEMPLATE_DIR = PROJECT_ROOT / "data"
TEMPLATE_OUTPUT_FILE = TEMPLATE_DIR / "manual_template.csv"