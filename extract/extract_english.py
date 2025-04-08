"""
extract_english.py

This script downloads the English version of *The Imitation of Christ* from Project Gutenberg,
extracts the main text content, and saves it as one paragraph per line in:
    raw_data/english_kempis.txt

- Source: https://www.gutenberg.org/cache/epub/1653/pg1653-images.html
- Total extracted paragraphs: 903
- Output format: Plain text, UTF-8 encoded

Usage:
    Run this script from the project root with:
        python extract/extract_english.py
"""

import requests
from bs4 import BeautifulSoup
import os

# Define the URL of the Gutenberg HTML version
URL = "https://www.gutenberg.org/cache/epub/1653/pg1653-images.html"

# Set up project paths (with fallback to default if no environment variable is set)
default_root = os.path.expanduser("~/GitHubRepos/classicbook-etl-pipeline")
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
    print(f"Fetching HTML content from: {url}")
    response = requests.get(url)
    response.encoding = "utf-8"

    if response.status_code != 200:
        raise Exception(f"Failed to fetch page (status {response.status_code})")

    print("HTML successfully fetched.")
    return response.text

# Extract clean paragraphs

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

def save_to_file(paragraphs, output_path):
    """
    Saves a list of text paragraphs to a file, one paragraph per line.
    Ensures UTF-8 encoding for compatibility.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        for paragraph in paragraphs:
            f.write(paragraph + "\n")
    print(f"Saved {len(paragraphs)} paragraphs to {output_path}")

# Main ETL workflow

def main():
    ensure_folder_exists(RAW_DATA_DIR)
    html = fetch_html(URL)
    paragraphs = extract_text_from_html(html)
    save_to_file(paragraphs, OUTPUT_FILE)

# Run the script

if __name__ == "__main__":
    main()

