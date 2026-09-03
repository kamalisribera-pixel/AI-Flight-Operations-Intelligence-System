from pathlib import Path

from src.services.ingestion_service import IngestionService


class TestDocumentIngestionPipeline:

    def test_ingest_documents(self):

        service = IngestionService()

        result = service.ingest()

        assert result is not None

        assert "documents" in result
        assert "chunks" in result
        assert "embeddings" in result
        assert "statistics" in result

        assert len(result["documents"]) > 0
        assert len(result["chunks"]) > 0
        assert len(result["embeddings"]) > 0