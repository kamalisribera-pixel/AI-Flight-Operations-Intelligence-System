from sentence_transformers import SentenceTransformer



class AerospaceEmbeddingModel:


    """
    Generates embeddings for aerospace
    knowledge chunks.
    """


    def __init__(self):

        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
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