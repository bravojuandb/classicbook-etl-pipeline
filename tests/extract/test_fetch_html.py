"""Test fetch URL"""

from unittest.mock import patch, Mock
from extract.extract_english import fetch_html

@patch("extract.extract_english.requests.get")
def test_fetch_html_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "<html><body>Test</body></html>"
    mock_response.encoding = 'UTF-8'
    mock_get.return_value = mock_response

    url = "https://example.com"
    html = fetch_html(url)

    assert "Test" in html
    mock_get.assert_called_once_with("https://example.com", timeout=10)