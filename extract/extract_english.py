import requests
from bs4 import BeautifulSoup
import os

# URLs

BASE_URL = "https://www.ccel.org" # Used to build full links later
INDEX_URL = f"{BASE_URL}/ccel/kempis/imitation"  # Main page for english version

# Paths (cross-platform and sharable using os.getenv )

# To run in custom path:
# Run in Bash: export PROJECT_ROOT=/home/your_folder
#              python extract_latin.py

default_root = os.path.expanduser("~/GitHubRepos/classicbook_etl_pipeline")
PROJECT_ROOT = os.getenv("PROJECT_ROOT", default_root)
RAW_DATA_DIR = os.path.join(PROJECT_ROOT, "raw_data")
OUTPUT_FILE = os.path.join(RAW_DATA_DIR, "english_kempis.txt")

# Ensures data folder exists
os.makedirs(RAW_DATA_DIR, exist_ok=True)