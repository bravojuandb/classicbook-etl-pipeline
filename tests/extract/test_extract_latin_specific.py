"""
Tests specific functions of extract_latin.py

From root run Pytest as a module:

python -m pytest tests/extract/test_extract_latin_specific.py

"""

import pytest
from unittest.mock import patch

from extract.extract_latin import (
    extract_book_links,
    parse_book_html,
    extract_all_paragraphs,
)

### --- TEST 1: extract_book_links ---
def test_extract_book_links_returns_expected_links():
    html = """
    <html>
      <body>
        <a href="kempis/kempis1.shtml">Book 1</a>
        <a href="kempis/kempis2.shtml">Book 2</a>
        <a href="notvalid.html">Other</a>
      </body>
    </html>
    """
    links = extract_book_links(html)
    assert links == ["kempis/kempis1.shtml", "kempis/kempis2.shtml"]


### --- TEST 2: parse_book_html filters empty and boilerplate ---
def test_parse_book_html_filters_irrelevant_text():
    html = """
    <html>
      <body>
        <p>  </p>
        <p>LATIN LIBRARY</p>
        <p>Domine, quid est homo?</p>
        <p>Ave Maria, gratia plena.</p>
      </body>
    </html>
    """
    result = parse_book_html(html)
    assert result == [
        "Domine, quid est homo?",
        "Ave Maria, gratia plena."
    ]


### --- TEST 3: extract_all_paragraphs integrates all steps ---
@patch("extract.extract_latin.fetch_book_html")
def test_extract_all_paragraphs_integrates_parsing(mock_fetch_book_html):
    # Simulate two book links in index page
    index_html = """
    <html>
      <body>
        <a href="kempis/kempis1.shtml">Book 1</a>
        <a href="kempis/kempis2.shtml">Book 2</a>
      </body>
    </html>
    """

    # Provide mocked HTML for both book pages
    mock_fetch_book_html.side_effect = [
        """
        <html><body>
          <p>LATIN LIBRARY</p>
          <p>Book 1 paragraph 1</p>
        </body></html>
        """,
        """
        <html><body>
          <p>Book 2 paragraph 1</p>
        </body></html>
        """
    ]

    from extract.extract_latin import BASE_LATIN_URL
    paragraphs = extract_all_paragraphs(index_html, base_url=BASE_LATIN_URL)

    assert paragraphs == [
        "Book 1 paragraph 1",
        "Book 2 paragraph 1"
    ]
    assert mock_fetch_book_html.call_count == 2