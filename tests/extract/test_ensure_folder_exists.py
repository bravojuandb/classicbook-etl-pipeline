"""
It creates the directory if it does not exist. 
Behaves identically for extract_english.py and extract_latin.py
"""

from extract.extract_english import ensure_folder_exists
from pathlib import Path

def test_ensure_folder_creates_directory(tmp_path):
    test_dir = tmp_path / "new_folder"
    
    # Ensure it doesn't exist yet
    assert not test_dir.exists()

    # Create it
    ensure_folder_exists(test_dir)

    # Now it should exist
    assert test_dir.exists()
    assert test_dir.is_dir()