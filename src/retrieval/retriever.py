from config.config import RETRIEVAL_TOP_K
from src.database.vector_store import AerospaceVectorStore
from src.embeddings.embedding_model import AerospaceEmbeddingModel



class AerospaceRetriever:


    def __init__(self):

        self.embedding_model = AerospaceEmbeddingModel()

        self.vector_store = AerospaceVectorStore()



    def retrieve(
        self,
        query,
        top_k=RETRIEVAL_TOP_K
    ):


        query_embedding = (
            self.embedding_model.model.encode(
                query
            )
        )


        results = self.vector_store.search(
            query_embedding,
            n_results=top_k
        )


        return results
