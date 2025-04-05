import requests
from bs4 import BeautifulSoup
import os
import time
import re

# Define the URL of the Gutenberg HTML version
URL = "https://www.gutenberg.org/cache/epub/1653/pg1653-images.html"


# Paths (cross-platform and sharable using os.getenv)
# Set up project paths (with fallback to default if no environment variable is set)
default_root = os.path.expanduser("~/GitHubRepos/classicbook_etl_pipeline")
PROJECT_ROOT = os.getenv("PROJECT_ROOT", default_root)
RAW_DATA_DIR = os.path.join(PROJECT_ROOT, "raw_data")
OUTPUT_FILE = os.path.join(RAW_DATA_DIR, "english_kempis.txt")

# Ensure the raw_data directory exists
os.makedirs(RAW_DATA_DIR, exist_ok=True)

# Notify the user that the script is starting

# Send HTTP GET request to fetch the HTML page

# Raise an error if the download fails

# Parse the HTML using BeautifulSoup

# Find the <body> tag where the book content resides

# Prepare a list to store extracted text parts

# Loop through all relevant HTML tags (<p>, <h1>, <h2>, <h3>)

    # Get and clean the text content of each tag

    # Append non-empty text to the list

# Join the text parts using double line breaks

# Save the cleaned text to the output file

# Notify the user that the book was successfully saved