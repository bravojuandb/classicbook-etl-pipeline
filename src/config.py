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
# OUTPUT FILE FOR ENGLISH TEXT
# --------------------------------------------------

ENGLISH_RAW_FILE = RAW_DATA_DIR / "raw_english_kempis.txt"

# --------------------------------------------------
# SOURCE URL FOR ENGLISH TEXT
# --------------------------------------------------

ENGLISH_URL = "https://www.gutenberg.org/cache/epub/1653/pg1653-images.html"