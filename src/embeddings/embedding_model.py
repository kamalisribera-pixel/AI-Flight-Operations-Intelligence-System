from config.config import EMBEDDING_MODEL_NAME
from sentence_transformers import SentenceTransformer



class AerospaceEmbeddingModel:


    """
    Generates embeddings for aerospace
    knowledge chunks.
    """


    def __init__(self):

        self.model = SentenceTransformer(
            EMBEDDING_MODEL_NAME
        )


    def generate_embeddings(
        self,
        texts
    ):

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        return embeddings
