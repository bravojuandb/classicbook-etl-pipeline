import requests
from bs4 import BeautifulSoup
import os

# Define the URL of the Gutenberg HTML version
URL = "https://www.gutenberg.org/cache/epub/1653/pg1653-images.html"


# Paths (cross-platform and sharable using os.getenv)

# Set up project paths (with fallback to default if no environment variable is set)
default_root = os.path.expanduser("~/GitHubRepos/classicbook_etl_pipeline")
PROJECT_ROOT = os.getenv("PROJECT_ROOT", default_root)

# Define the raw_data directory and final output file path
RAW_DATA_DIR = os.path.join(PROJECT_ROOT, "raw_data")
OUTPUT_FILE = os.path.join(RAW_DATA_DIR, "english_kempis.txt")

# Ensure the raw_data directory exists
def ensure_folder_exists(path):
    """
    Checks if the specified folder exists. If not, it creates it.
    This ensures we never run into file-saving issues later.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Folder created: {path}")
    else:
        print(f"Folder already exists: {path}")

# Fetch HTML content
def fetch_html(url):
    """
    Sends a GET request to the specified URL and returns the HTML content.
    If the request fails (non-200 status), it raises an exception.
    """
    print(f"Fetching HTML contetnt from: {url}")
    response = requests.get(url)
    response.encoding = "utf-8"

    if response.status_code != 200:
        raise Exception(f"Failed to fetch page (status {response.status_code})")

    print("HTML successfully fetched.")
    return response.text


# Extract clena paragraphs

def extract_text_from_html(html):
    """
    Parses the HTML content using BeautifulSoup, finds the <body> tag,
    and extracts text from <p>, <h1>, <h2>, and <h3> tags.
    Filters out irrelevant lines like Gutenberg boilerplate.
    """
    soup = BeautifulSoup(html, "html.parser")
    body = soup.find("body")

    if not body:
        raise Exception("Body tag not found in HTML.")
    
    print("Extracting meaningful text from HTML...")

    text_parts = []
    for tag in body.find_all(["p","h1","h2","h3"]):
        text = tag.get_text(separator=" ", strip=True)

        if not text or "Gutenberg" in text or "***" in text:
            continue

        text_parts.append(text)

    print(f"Extracted {len(text_parts)} paragraphs.")
    return text_parts

# Save content to .txt file

# Main ETL workflow

# Run the script