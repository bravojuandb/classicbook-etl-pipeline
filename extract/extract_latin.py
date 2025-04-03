
# Import necesary libraries
import requests
from bs4 import BeautifulSoup
import os  # Because I want to save the extracted text into a specific folder

# Define the URL and Output File
BASE_URL = "https://www.thelatinlibrary.com"  # Used to build sublinks later
INDEX_URL = f"{BASE_URL}/kempis.html"  # Specific subpage to scrape
PROJECT_ROOT = os.path.expanduser("~/GitHubRepos/classicbook_etl_pipeline")
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "raw_data", "latin_kempis.txt") # So it works in Mac and Windows

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
