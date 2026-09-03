from pathlib import Path
import sys
import json

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(
    str(PROJECT_ROOT)
)
 

from config.settings import DOCUMENTS_DIR, PROCESSED_DOCUMENTS_FILE
from config.logging_config import logger
from src.ingestion.document_loader import AerospaceDocumentLoader
# =========================================================
# CONFIGURATION
# =========================================================

DOCUMENT_PATH = DOCUMENTS_DIR

OUTPUT_PATH = PROCESSED_DOCUMENTS_FILE


# =========================================================
# MAIN
# =========================================================

def main():

    logger.info("Starting document ingestion")


    loader = AerospaceDocumentLoader(
        DOCUMENT_PATH
    )


    documents = loader.load_documents()
    stats = loader.get_statistics()


    logger.info("Ingestion statistics")


    logger.info("Documents found: %s", stats["documents_found"])


    logger.info("Documents processed: %s", stats["documents_processed"])


    logger.info("Total pages: %s", stats["total_pages"])

    for document in stats["documents"]:

        logger.info(
            "Processed %s (%s pages)",
            document["filename"],
            document["pages"]
        )


    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    with open(
        OUTPUT_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            documents,
            file,
            indent=4,
            ensure_ascii=False
        )


    logger.info("Documents saved: %s", OUTPUT_PATH)
    logger.info("Document ingestion complete")



if __name__ == "__main__":
    main()
