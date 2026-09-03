import json
import numpy as np

from config.settings import CHUNKS_FILE, EMBEDDINGS_FILE
from config.logging_config import logger
from src.embeddings.embedding_model import AerospaceEmbeddingModel
from src.database.vector_store import AerospaceVectorStore



INPUT_PATH = CHUNKS_FILE



def main():


    logger.info("Starting vector database build")



    with open(
        INPUT_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        chunks = json.load(file)



    texts = [

        chunk["text"]

        for chunk in chunks

    ]



    model = AerospaceEmbeddingModel()


    EMBEDDING_PATH = EMBEDDINGS_FILE

    if EMBEDDING_PATH.exists():

        logger.info("Loading existing embeddings")

        embeddings = np.load(
            EMBEDDING_PATH
        )


    else:

        logger.info("Generating embeddings")


        embeddings = model.generate_embeddings(
            texts
        )


        np.save(
            EMBEDDING_PATH,
            embeddings
        )


        logger.info("Embeddings saved")


    logger.info("Generated embeddings: %s", len(embeddings))



    database = AerospaceVectorStore()


    database.add_documents(
        chunks,
        embeddings
    )


    logger.info("Vector database created")



if __name__ == "__main__":
    main()
