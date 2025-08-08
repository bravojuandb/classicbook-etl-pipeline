"""
Performs the full transformations of the manually aligned latin-english text.


"""
import logging
from pathlib import Path
import pandas as pd
from pandas import DataFrame
import re
from src.config import INPUT_DIR

logger = logging.getLogger(__name__)  # Define logger globally

def load_and_merge() -> DataFrame:
    """Loads, validates, and merges all aligned book files into a single DataFrame."""
    
    folder = Path(INPUT_DIR)
    dfs = []

    # Collect all matching files
    files = folder.glob("book*_aligned.tsv")

    # Sort files numerically by book ID extracted via regex
    sorted_files = sorted(
        files,
        key=lambda f: int(re.search(r"book(\d+)", f.name).group(1))
    )

    logger.info(f"OK - Found {len(sorted_files)} files to load.")

    for file in sorted_files:
        if not file.exists():
            logger.warning(f"X Skipping missing file: {file.name}")
            continue

        match = re.search(r"book(\d+)", file.name)
        book_id = int(match.group(1))

        logger.info(f"--> Loading book {book_id}: {file.name}")

        df = pd.read_csv(file, sep="\t", names=["latin_text", "english_text"])
        df["book_id"] = book_id
        dfs.append(df)

    combined_df = pd.concat(dfs, ignore_index=True)
    logger.info(f"OK - Combined {len(combined_df)} rows into a single DataFrame.")

    return combined_df


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s — %(levelname)s — %(message)s"
    )

    logger.info("...Starting transformation debug session...")

    df = load_and_merge()

    logger.info(f"* Sample rows:\n{df.sample(5)}")
    logger.info(f"* Shape of combined DataFrame: {df.shape}")
    logger.info(f"* Unique book_ids: {df['book_id'].unique().tolist()}")


if __name__ == "__main__":
    main()
    