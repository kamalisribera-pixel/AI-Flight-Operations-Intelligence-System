import json

from config.settings import CHUNKS_FILE, PROCESSED_DOCUMENTS_FILE
from config.logging_config import logger
from src.ingestion.chunker import AerospaceDocumentChunker


INPUT_PATH = PROCESSED_DOCUMENTS_FILE


OUTPUT_PATH = CHUNKS_FILE



def main():


    logger.info("Starting document chunking")


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



    logger.info("Chunks created: %s", len(chunks))



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



    logger.info("Chunks saved: %s", OUTPUT_PATH)
    logger.info("Document chunking complete")



if __name__ == "__main__":
    main()
