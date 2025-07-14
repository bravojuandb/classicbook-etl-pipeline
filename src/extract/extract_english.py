"""
Downloads the English version of *The Imitation of Christ* from Project Gutenberg,
extracts the main text content, and saves it as one paragraph per line in:
raw_data/raw_english_kempis.txt

- Source: https://www.gutenberg.org/cache/epub/1653/pg1653-images.html
- Total extracted paragraphs: 903
- Output format: Plain text, UTF-8 encoded

Usage:
        python -m src.extract.extract_english

"""


from src.config import ENGLISH_URL, ENGLISH_RAW_FILE, RAW_DATA_DIR

import requests
from bs4 import BeautifulSoup
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Ensure the raw_data directory exists

def ensure_folder_exists(path: Path):
    """
    Checks if the specified folder exists. If not, it creates it.
    """
    try:
        if not path.exists():
            path.mkdir(parents=True)
            logging.info(f"Folder created: {path}")
        else:
            logging.info(f"Folder already exists: {path}")
    except Exception as e:
        logging.error(f"Failed to create folder {path}:{e}", exc_info=True)
        raise

# Fetch HTML content

def fetch_html(url):
    """
    Sends a GET request to the specified URL and returns the HTML content.
    If the request fails, it raises an exception.
    """
    logging.info(f"Fetching HTML content from: {url}")

    try:
        response = requests.get(url, timeout=10)  # Default with SSL verification
        response.raise_for_status()
    except requests.exceptions.SSLError:
        logging.warning("SSL verification failed. Retrying without SSL verification...")
        response = requests.get(url, verify=False, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch page: {e}")

    response.encoding = "utf-8"
    logging.info("HTML successfully fetched.")
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
    
    logging.info("Extracting meaningful text from HTML...")

    text_parts = []
    for tag in body.find_all(["p","h1","h2","h3"]):
        text = tag.get_text(separator=" ", strip=True)

        if not text or "Gutenberg" in text or "***" in text:
            continue

        text_parts.append(text)

    logging.info(f"Extracted {len(text_parts)} paragraphs.")

    return text_parts

# Save content to .txt file

def save_to_file(paragraphs, output_path):
    """
    Saves a list of text paragraphs to a file, one paragraph per line.
    Ensures UTF-8 encoding for compatibility.
    """
    try:
        with output_path.open("w", encoding="utf-8") as f:
            for paragraph in paragraphs:
                f.write(paragraph + "\n")
        logging.info(f"Saved {len(paragraphs)} paragraphs to {output_path}")
    except Exception as e:
        logging.error(f"Failed to save file to {output_path}: {e}", exc_info=True)


# Main workflow

def main():

    try:
        ensure_folder_exists(RAW_DATA_DIR)
        html = fetch_html(ENGLISH_URL)
        paragraphs = extract_text_from_html(html)
        save_to_file(paragraphs, ENGLISH_RAW_FILE)
    
    except Exception as e:
        logging.error(f"An eror occurres during execution: {e}", exc_info=True)

# Run the script

if __name__ == "__main__":
    main()

