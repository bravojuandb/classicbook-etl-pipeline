"""
Main script. Currently, it only touches the extract phase.
"""

import logging
import traceback

from src.extract.extract_english import run_english_extraction
from src.extract.extract_latin import run_latin_extraction

# === CONFIGURE LOGGING ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)

# === MAIN EXECUTION ===
def main():
    logger.info("🚀 Starting Extract Phase")

    try:
        run_english_extraction()
        logger.info("✅ English extraction completed.")
    except Exception as e:
        logger.error("❌ Failed during English extraction.")
        logger.error(traceback.format_exc())

    try:
        run_latin_extraction()
        logger.info("✅ Latin extraction completed.")
    except Exception as e:
        logger.error("❌ Failed during Latin extraction.")
        logger.error(traceback.format_exc())

    logger.info("🏁 Extract Phase finished.")

if __name__ == "__main__":
    main()