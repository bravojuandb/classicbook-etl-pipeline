# Scraping Dictionary (Extract Phase Cheat Sheet)

Created during the *Classic Book ETL Pipeline*  
This cheat sheet documents essential concepts, tools, and commands used in the extract phase of a real ETL project.

---

##  1. GENERAL SCRAPING CONCEPTS

| Term         | Definition |
|--------------|------------|
| **Scraping** | The process of extracting structured data from web pages. |
| **Fetching** | Downloading the raw HTML content from a webpage. |
| **Parsing**  | Converting HTML into a structured format that Python can work with. |
| **HTML**     | The markup language used to structure content on web pages. |
| **DOM**      | Document Object Model — the tree-like structure of HTML elements. |
| **404 / 200**| HTTP status codes. 200 = OK. 404 = Not Found. |

---

##  2. `requests` — Fetching Web Content

| Term / Command            | Explanation |
|---------------------------|-------------|
| `requests.get(url)`       | Sends an HTTP GET request to retrieve a web page. |
| `response.status_code`    | Returns the HTTP status code (e.g. 200 = OK, 404 = Not Found). |
| `response.text`           | Returns the HTML content of the response as a string. |
| `response.content`        | Returns binary content (e.g., for images or files). |
| `headers = {...}`         | Custom headers like `User-Agent` to simulate a browser. |
| `requests.get(url, headers=headers)` | Sends a request with headers. |
| `try/except`              | Handles request errors such as timeouts or invalid URLs. |
| `time.sleep(1)`           | Adds a delay between requests to avoid overloading the server. |

---

##  3. `BeautifulSoup` — Parsing HTML

| Term / Command                     | Explanation |
|------------------------------------|-------------|
| `BeautifulSoup(html, "html.parser")` | Parses the HTML string into a navigable tree structure. |
| `soup.find("tag")`               | Finds the **first** occurrence of a tag. |
| `soup.find_all("tag")`           | Finds **all** matching tags. |
| `soup.find("tag", class_="...")` | Finds a tag by its CSS class. |
| `tag.get_text(strip=True)`        | Gets only the visible text, removes whitespace. |
| `tag["href"]`                    | Accesses an attribute of the tag (e.g., the `href` link). |
| `tag.find_parent("tag")`         | Moves up the DOM tree to the tag’s parent. |

---

##  4. FILE I/O and TEXT HANDLING

| Term / Command             | Explanation |
|----------------------------|-------------|
| `open("file.txt", "w")`     | Opens a file for writing (overwrites if it exists). |
| `with open(...) as f:`      | Safely opens a file (auto-closes when done). |
| `f.write("text")`           | Writes text to a file. |
| `.txt`                      | Plain text format. |
| `.tsv`                      | Tab-separated values format. Ideal for structured data. |
| `os.path.exists("file")`   | Checks if a file already exists. |
| `re.sub(r"\s+", " ", text)` | Replaces multiple spaces/newlines using regex. |

---

###  Created during:
- The *Classic Book ETL Pipeline* project.
- Juan’s study of `requests`, `BeautifulSoup`, and web scraping.
- April 2025 — posted as part of a real data engineering journey.

