"""
extract_latin.py

This script extracts the Latin text of *The Imitation of Christ* from The Latin Library:
    https://www.thelatinlibrary.com/kempis.html

1. Fetches the main index page containing links to the four books.
2. Parses and collects all paragraph texts from each linked subpage.
3. Cleans the extracted content by removing empty lines and boilerplate text.
4. Saves the final result as one paragraph per block to:
       raw_data/raw_latin_kempis.txt

- Total expected paragraphs: ~674
- Output encoding: UTF-8
- Output format: plain text, double newlines between paragraphs

Usage:
         python3 -m src.extract.extract_latin

"""


from src.config import LATIN_RAW_FILE, LATIN_URL, RAW_DATA_DIR, BASE_LATIN_URL
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

def fetch_html(url: str) -> str:
    """
    Fetches the HTML content from the given URL with proper error handling.

    Args:
        url (str): The URL of the index page.

    Returns:
        str: The UTF-8 encoded HTML content.

    Raises:
        Exception: If the request fails or returns a non-200 status code.
    """
    logging.info(f"Fetching HTML content from: {url}")

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )
    }
    try:
        # Waits for 10 secs before raising an error if the server is unresponsive
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        response.encoding = "utf-8" 
        html_content = response.text  # HTML body as string
        return html_content
        
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {url}: {e}", exc_info=True)
        raise Exception(f"Failed to fetch page: {url}") from e

def extract_book_links(index_html: str) -> list[str]:
    """
    Extracts the relative URLs of book subpages from index HTLM
    Parses the HTML of the main index page and filters anchor tags 
    based on the href pattern.

    Args:
        index_html (str): The raw HTML content of the index page.

    Returns:
        list[str]: A list of relative URL strings pointing to the individual book pages.

    """
    soup = BeautifulSoup(index_html, "html.parser")
    book_links = [
        a["href"] for a in soup.find_all("a", href=True)
        if a["href"].startswith("kempis/kempis") and a["href"].endswith(".shtml")
    ]
    logging.info(f"Found {len(book_links)} book links.")
    return book_links

def fetch_book_html(base_url: str, relative_path: str) -> str:
    """
    Fetches the HTML content of an individual book page.

    Constructs the full URL using the base site URL and the relative path to the book.
    Attempts to retrieve the HTML content using the fetch_html function. If the request
    fails, logs a warning and returns an empty string to allow the pipeline to continue.

    Args:
        base_url (str): The root URL of the site (e.g., https://www.thelatinlibrary.com).
        relative_path (str): The relative path to the specific book page.

    Returns:
        str: The HTML content of the book page, or an empty string if fetching failed.

    """
    full_url = f"{base_url}/{relative_path}"
    logging.info(f"Fetching: {full_url}")
    try:
        return fetch_html(full_url)
    except Exception as e:
        logging.warning(f"Failed to fetch {full_url}: {e}")
        return ""  # Return empty string to skip

def parse_book_html(html: str) -> list[str]:
    """
    Parses the HTML content of a book page and extracts clean text paragraphs.

    Filters out boilerplate content such as footers containing "LATIN LIBRARY" and
    skips empty or whitespace-only paragraphs. Returns a list of meaningful Latin
    text paragraphs found inside <p> tags.

    Args:
        html (str): The raw HTML content of the book page.

    Returns:
        list[str]: A list of cleaned paragraph strings extracted from the HTML.
    """
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    paragraphs = []

    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        if "LATIN LIBRARY" in text or not text:
            continue
        paragraphs.append(text)

    return paragraphs

def extract_all_paragraphs(index_html: str, base_url: str) -> list[str]:
    """
    Extracts and aggregates all clean text paragraphs from all book subpages.

    Uses the index HTML to identify links to individual book pages, fetches each book's
    HTML content, parses the content to extract valid <p> tag text, and collects all 
    paragraphs into a single list.

    Args:
        index_html (str): The raw HTML content of the main index page.
        base_url (str): The root URL used to construct full paths to the book pages.

    Returns:
        list[str]: A list of all cleaned text paragraphs extracted from all book pages.
    """
    all_paragraphs = []
    book_links = extract_book_links(index_html)

    for relative_link in book_links:
        book_html = fetch_book_html(base_url, relative_link)
        paragraphs = parse_book_html(book_html)
        all_paragraphs.extend(paragraphs)

    logging.info(f"Total paragraphs collected: {len(all_paragraphs)}")
    return all_paragraphs

def save_to_file(paragraphs: list[str], output_path: Path) -> None:
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
                f.write(paragraph + "\n\n")
        logging.info(f"Saved {len(paragraphs)} paragraphs to {output_path}")
    except Exception as e:
        logging.error(f"Failed to save file to {output_path}: {e}", exc_info=True)
        raise

def main() -> None:

    try:
        logging.info("Starting extraction process...")
        ensure_folder_exists(RAW_DATA_DIR)

        index_html = fetch_html(LATIN_URL)
        paragraphs = extract_all_paragraphs(index_html, base_url=BASE_LATIN_URL)
        save_to_file(paragraphs, LATIN_RAW_FILE)

        logging.info("Extraction completed successfully.")
    
    except Exception as e:
        logging.error(f"An eror occurred during execution: {e}", exc_info=True)


if __name__ == "__main__":
    main()

