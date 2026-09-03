from src.services.retrieval_service import RetrievalService


class TestRetrievalPipeline:

    def test_retrieve_documents(self):

        service = RetrievalService()

        results = service.retrieve(
            "What is hydraulic pressure?"
        )

        assert results is not None

        assert "documents" in results

        assert len(results["documents"][0]) > 0