import chromadb

from config.config import (
    CHROMA_COLLECTION_NAME,
    CHROMA_PERSIST_DIR,
    RETRIEVAL_TOP_K,
    VECTOR_INSERT_BATCH_SIZE
)
from config.logging_config import logger
from src.exceptions import DatabaseError



class AerospaceVectorStore:


    def __init__(
        self,
        path=CHROMA_PERSIST_DIR
    ):

        try:
            self.client = chromadb.PersistentClient(path=str(path))
            self.collection = self.client.get_or_create_collection(
                name=CHROMA_COLLECTION_NAME
            )
        except Exception as error:
            logger.exception("Vector database initialization failed")
            raise DatabaseError(
                "Vector database is unavailable."
            ) from error



    def add_documents(
        self,
        chunks,
        embeddings,
        batch_size=VECTOR_INSERT_BATCH_SIZE
    ):
        try:
            if self.collection.count() > 0:
                logger.info("Vector database already exists.")
                return

            total = len(chunks)
            for start in range(0, total, batch_size):
                end = min(start + batch_size, total)
                batch_chunks = chunks[start:end]
                batch_embeddings = embeddings[start:end]
                self.collection.add(
                    ids=[str(start + index) for index in range(len(batch_chunks))],
                    documents=[chunk["text"] for chunk in batch_chunks],
                    embeddings=batch_embeddings.tolist(),
                    metadatas=[chunk["metadata"] for chunk in batch_chunks]
                )

            logger.info("Inserted %s/%s chunks", end if total else 0, total)
        except Exception as error:
            logger.exception("Vector database write failed")
            raise DatabaseError("Vector database operation failed.") from error


    def search(
        self,
        query_embedding,
        n_results=RETRIEVAL_TOP_K
    ):

        try:
            return self.collection.query(

            query_embeddings=[
                query_embedding
            ],

            n_results=n_results

            )
        except Exception as error:
            logger.exception("Vector database search failed")
            raise DatabaseError("Vector database operation failed.") from error
