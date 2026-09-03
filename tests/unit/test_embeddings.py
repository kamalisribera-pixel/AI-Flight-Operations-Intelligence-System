from src.embeddings.embedding_model import AerospaceEmbeddingModel


class FakeModel:
    def encode(self, texts, **kwargs):
        return [[len(text)] for text in texts]


def test_embedding_generation_delegates_to_model():
    model = AerospaceEmbeddingModel.__new__(AerospaceEmbeddingModel)
    model.model = FakeModel()
    assert model.generate_embeddings(["lift", "drag"]) == [[4], [4]]