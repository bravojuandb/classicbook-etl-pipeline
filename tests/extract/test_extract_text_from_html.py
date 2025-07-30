"""
Tests if HTML text is extracted correctly
Behaves identically for extract_english.py and extract_latin.py
"""

from extract.extract_english import extract_text_from_html

def test_extract_text_from_html():
    sample_html = """
    <html>
      <body>
        <h1>Book I</h1>
        <p>This is a paragraph.</p>
        <p>*** START OF THE PROJECT GUTENBERG EBOOK ***</p>
        <p>Another paragraph.</p>
      </body>
    </html>
    """

    paragraphs = extract_text_from_html(sample_html)

    # Should exclude the Gutenberg line and include the two valid ones
    assert paragraphs == ["Book I", "This is a paragraph.", "Another paragraph."]