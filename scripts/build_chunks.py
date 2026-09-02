from pathlib import Path
import json

from src.ingestion.chunker import AerospaceDocumentChunker


INPUT_PATH = Path(
    "data/processed/documents.json"
)


OUTPUT_PATH = Path(
    "data/processed/chunks.json"
)



def main():


    print("=" * 60)
    print("AI_FOIS DOCUMENT CHUNKING")
    print("=" * 60)


    with open(
        INPUT_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        documents = json.load(file)



    chunker = AerospaceDocumentChunker(
        documents
    )


    chunks = chunker.create_chunks()



    print(
        f"Chunks Created: {len(chunks)}"
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
            chunks,
            file,
            indent=4,
            ensure_ascii=False
        )



    print(
        f"Saved: {OUTPUT_PATH}"
    )


    print("=" * 60)
    print("CHUNKING COMPLETE")
    print("=" * 60)



if __name__ == "__main__":
    main()