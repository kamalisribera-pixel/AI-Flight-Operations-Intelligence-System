import chromadb

from config.config import (
    CHROMA_COLLECTION_NAME,
    CHROMA_PERSIST_DIR,
    RETRIEVAL_TOP_K,
    VECTOR_INSERT_BATCH_SIZE
)
from config.logging_config import logger



class AerospaceVectorStore:


    def __init__(
        self,
        path=CHROMA_PERSIST_DIR
    ):

        self.client = chromadb.PersistentClient(
            path=str(path)
        )


        self.collection = self.client.get_or_create_collection(
            name=CHROMA_COLLECTION_NAME
        )



    def add_documents(
        self,
        chunks,
        embeddings,
        batch_size=VECTOR_INSERT_BATCH_SIZE
    ):

        # Prevent duplicate insertion
        if self.collection.count() > 0:

            logger.info(
                "Vector database already exists."
            )

            return


        total = len(chunks)


        for start in range(
            0,
            total,
            batch_size
        ):

            end = min(
                start + batch_size,
                total
            )


            batch_chunks = chunks[start:end]

            batch_embeddings = embeddings[start:end]


            ids = []

            documents = []

            metadata = []


            for index, chunk in enumerate(batch_chunks):

                ids.append(
                    str(start + index)
                )


                documents.append(
                    chunk["text"]
                )


                metadata.append(
                    chunk["metadata"]
                )


            self.collection.add(

                ids=ids,

                documents=documents,

                embeddings=batch_embeddings.tolist(),

                metadatas=metadata

            )

        logger.info(
            f"Inserted {end}/{total} chunks"
        )


    def search(
        self,
        query_embedding,
        n_results=RETRIEVAL_TOP_K
    ):

        return self.collection.query(

            query_embeddings=[
                query_embedding
            ],

            n_results=n_results

        )
