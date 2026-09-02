import chromadb



class AerospaceVectorStore:


    def __init__(
        self,
        path="vector_db"
    ):

        self.client = chromadb.PersistentClient(
            path=path
        )


        self.collection = self.client.get_or_create_collection(
            name="aerospace_knowledge"
        )



    def add_documents(
        self,
        chunks,
        embeddings,
        batch_size=5000
    ):

        # Prevent duplicate insertion
        if self.collection.count() > 0:

            print(
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

        print(
            f"Inserted {end}/{total} chunks"
        )


    def search(
        self,
        query_embedding,
        n_results=5
    ):

        return self.collection.query(

            query_embeddings=[
                query_embedding
            ],

            n_results=n_results

        )