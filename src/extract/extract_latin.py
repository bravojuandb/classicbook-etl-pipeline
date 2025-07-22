"""
extract_latin.py

This script extracts the Latin text of *The Imitation of Christ* from The Latin Library:
    https://www.thelatinlibrary.com/kempis.html

It performs the following steps:
1. Fetches the main index page containing links to the four books.
2. Parses and collects all paragraph texts from each linked subpage.
3. Cleans the extracted content by removing empty lines and boilerplate text.
4. Saves the final result as one paragraph per block to:
       raw_data/latin_kempis.txt

- Total expected paragraphs: ~674
- Output encoding: UTF-8
- Output format: plain text, double newlines between paragraphs

Usage:
    Run this script from the project root directory:
        python extract/extract_latin.py
"""


from src.config import LATIN_RAW_FILE, LATIN_URL, RAW_DATA_DIR
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def ensure_folder_exists(path: Path):
    """
    Ensures that the specified directory exists.

    Creates the directory and any necessary parent directories if they do not already exist.
    Logs the creation event or confirms if the directory already exists.

    Args:
        path (Path): A pathlib.Path object representing the target directory path.

    Returns:
        None

    Raises:
        Exception: If directory creation fails due to permission issues or other I/O errors.
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


# ------------------------------------------------------

def fetch_latin_html(url: str) -> str:
    """
    Fetches the HTML content from the given URL with proper error handling.

    Args:
        url (str): The URL of the Latin index page.

    Returns:
        str: The UTF-8 encoded HTML content.

    Raises:
        Exception: If the request fails or returns a non-200 status code.
    """
    logging.info(f"Fetching HTML content from: {url}")

    try:
        # Waits for 10 secs before raising an error if the server is unresponsive
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = "utf-8" 
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {url}: {e}", exc_info=True)
        raise Exception(f"Failed to fetch page: {url}") from e

# ------------------------------------------------------

def parse_latin_html(html: str) -> list[str]:

    # Parse the HTML of the main page with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # find all the links to the individual books, and store them in a list
    book_links = []

    # Loop through all <a> tags and find the 4 that go to the book

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("kempis/kempis") and href.endswith(".shtml"):
            book_links.append(href)

    # Print the links we found
    print("The book is found here:")
    for link in book_links:
        print("   -", link)            

    # Creates a list to store the text inside the links
    all_paragraphs = [] 

    # Loop through the links (fetchin and parsing each sublink)
    for link in book_links:
        full_url = f"{BASE_LATIN_URL}/{link}"
        print(f"\n ... Fetching: {full_url}")

        book_response = requests.get(full_url) # Fetch each sublink
        book_response.encoding = "utf-8"

        if book_response.status_code != 200:   # Check each sublink
            print("Failed to fetch {full_url}")
            continue     # Skip if failed

        # Parse the book page
        book_soup = BeautifulSoup(book_response.text, "html.parser")
        paragraphs = book_soup.find_all("p")

        for p in paragraphs:
            text = p.get_text(strip=True)
            if "LATIN LIBRARY" in text or not text:
                continue # Skip footers or empty lines
            all_paragraphs.append(text)

    print(f"\n Total paragraphs collected: {len(all_paragraphs)}")

# ------------------------------------------------------


def save_to_file(paragraphs: list, output_path: Path):
    """
    Writes a list of text paragraphs to a file, one paragraph per line.

    Each paragraph is written on a separate line using UTF-8 encoding to ensure
    compatibility across systems and languages.

    Args:
        paragraphs (List[str]): A list of cleaned text paragraphs to write.
        output_path (Path): A pathlib.Path object representing the output file location.

    Raises:
        Exception: If the file cannot be written to the specified path.
    """
    try:
        with output_path.open("w", encoding="utf-8") as f:
            for paragraph in paragraphs:
                f.write(paragraph + "\n")
        logging.info(f"Saved {len(paragraphs)} paragraphs to {output_path}")
    except Exception as e:
        logging.error(f"Failed to save file to {output_path}: {e}", exc_info=True)



# ------------------------------------------------------




# Make sure the output folder exists
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Save extracted paragraphs into a file
with OUTPUT_FILE.open("w", encoding="utf-8") as f: 
    for paragraph in all_paragraphs:
        f.write(paragraph + "\n\n")

print(f"\n Finished. Saved {len(all_paragraphs)} paragraphs to: {OUTPUT_FILE}")

# ------------------------------------------------------



def main():

    try:
        ensure_folder_exists(RAW_DATA_DIR)
        html = fetch_latin_html(LATIN_URL)
        paragraphs = parse_latin_html(html)
        save_to_file(paragraphs, LATIN_RAW_FILE)
    
    except Exception as e:
        logging.error(f"An eror occurres during execution: {e}", exc_info=True)


# Run the script

if __name__ == "__main__":
    logging.info("Starting extraction process...")
    main()

