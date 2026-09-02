from pathlib import Path
import sys
import json

from scipy import stats

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(
    str(PROJECT_ROOT)
)
 

from src.ingestion.document_loader import AerospaceDocumentLoader
# =========================================================
# CONFIGURATION
# =========================================================

DOCUMENT_PATH = Path(
    "data/documents"
)

OUTPUT_PATH = Path(
    "data/processed/documents.json"
)


# =========================================================
# MAIN
# =========================================================

def main():

    print("=" * 60)
    print("AI_FOIS DOCUMENT INGESTION")
    print("=" * 60)


    loader = AerospaceDocumentLoader(
        DOCUMENT_PATH
    )


    documents = loader.load_documents()
    stats = loader.get_statistics()


    print()

    print("=" * 60)
    print("INGESTION STATISTICS")
    print("=" * 60)


    print(
        f"Documents Found: {stats['documents_found']}"
    )


    print(
        f"Documents Processed: {stats['documents_processed']}"
    )


    print(
        f"Total Pages: {stats['total_pages']}"
    )


    print()

    for document in stats["documents"]:

        print(
            f"{document['filename']}"
        )

        print(
            f"Pages: {document['pages']}"
        )

        print("-" * 40)


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


    print(
        f"Saved: {OUTPUT_PATH}"
    )


    print("=" * 60)
    print("DOCUMENT INGESTION COMPLETE")
    print("=" * 60)



if __name__ == "__main__":
    main()