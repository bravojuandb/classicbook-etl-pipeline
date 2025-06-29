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

# Import necesary libraries
import requests
from bs4 import BeautifulSoup
from pathlib import Path

# Define the URL and Output File
BASE_URL = "https://www.thelatinlibrary.com"  # Used to build sublinks later
INDEX_URL = f"{BASE_URL}/kempis.html"  # Specific subpage to scrape

# Set up dynamic project path (portable)
PROJECT_ROOT = Path.home() / "GitHubRepos" / "classicbook-etl-pipeline"
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
OUTPUT_FILE = RAW_DATA_DIR / "latin_kempis.txt"

# Fetch the index page (request and get the HTML code from the index page)
response = requests.get(INDEX_URL)
response.encoding = "utf-8"   # Decode as UTF-8

# Check the page loaded
if response.status_code != 200:  # 200 means success, page loaded ok
    print("Failed to load index page")
    exit()

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
    full_url = f"{BASE_URL}/{link}"
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


# Make sure the output folder exists
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Save extracted paragraphs into a file
with OUTPUT_FILE.open("w", encoding="utf-8") as f: 
    for paragraph in all_paragraphs:
        f.write(paragraph + "\n\n")

print(f"\n Finished. Saved {len(all_paragraphs)} paragraphs to: {OUTPUT_FILE}")

