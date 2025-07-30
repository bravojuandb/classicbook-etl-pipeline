# Extract Phase

This phase retrieves the full text of *The Imitation of Christ* from two separate online sources — one in English and one in Latin.

---

## Sources

- **English text**: [Project Gutenberg](https://www.gutenberg.org/cache/epub/1653/pg1653-images.html)  
- **Latin text**: [The Latin Library](https://www.thelatinlibrary.com/kempis.html)

---

## Scripts

Two dedicated scripts handle the extraction logic in parallel:

- `extract_english.py`  
  - Steps: ensure output folder exists → fetch webpage → parse HTML → save raw text.
  
- `extract_latin.py`  
  - Steps: ensure output folder exists → fetch main page → extract book links → fetch each book → combine and save raw text.

---

## Configuration

- All source URLs and output file paths are managed centrally in the shared `config.py` file.
- This promotes modularity, consistency, and reuse across the entire pipeline.

---

## Output

Both raw texts are saved in the `data/raw/` directory with the following filenames:

- `raw_english_kempis.txt`
- `raw_latin_kempis.txt`

---

## Reproducibility and Idempotency

To support repeatable, production-grade pipelines:

- The extraction logic is designed to be **idempotent**: if the output files already exist, the script skips re-downloading (optional behavior, configurable).
- Future upgrades may include **hash-based content comparison** to detect silent changes in source text.

---

## How to Run the Scripts

Clone the repository.

To extract the raw texts, run the following commands from the project root directory:

```bash
python3 -m src.extract.extract_english
python3 -m src.extract.extract_latin
```
Use python instead of python3 if your environment defaults to Python 3.

## Prerequisites

	•	Python 3.8 or later
	•	Dependencies installed via requirements.txt:

```bash
pip install -r requirements.txt
```

## Output Confirmation

After running the scripts, you should see the following files created in data/raw/:
	•	raw_english_kempis.txt
	•	raw_latin_kempis.txt