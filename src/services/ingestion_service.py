import json
import re

import numpy as np

from config.logging_config import logger
from config.settings import (
    CHUNKS_FILE,
    DOCUMENTS_DIR,
    EMBEDDINGS_FILE,
    PROCESSED_DOCUMENTS_FILE,
)
from src.database.document_repository import DocumentRepository
from src.database.vector_store import AerospaceVectorStore
from src.embeddings.embedding_model import AerospaceEmbeddingModel
from src.exceptions import (
    DatabaseError,
    DocumentError,
    EmbeddingError,
)
from src.ingestion.chunker import AerospaceDocumentChunker
from src.ingestion.document_loader import AerospaceDocumentLoader


class IngestionService:

    def __init__(
        self,
        loader_factory=AerospaceDocumentLoader,
        chunker_factory=AerospaceDocumentChunker,
        embedding_model=None,
        vector_store=None,
        document_repository=None,
    ):
        self.loader_factory = loader_factory
        self.chunker_factory = chunker_factory
        self.embedding_model = embedding_model or AerospaceEmbeddingModel()
        self.vector_store = vector_store or AerospaceVectorStore()
        self.document_repository = (
            document_repository or DocumentRepository()
        )

    @staticmethod
    def _clean_documents(documents):
        cleaned = []

        for document in documents:
            text = re.sub(r"\s+", " ", document["text"]).strip()

            if text:
                cleaned.append(
                    {
                        "text": text,
                        "metadata": document["metadata"],
                    }
                )

        return cleaned

    def ingest(self, directory=DOCUMENTS_DIR):

        # -----------------------------
        # Load documents
        # -----------------------------
        try:
            loader = self.loader_factory(directory)
            documents = self._clean_documents(
                loader.load_documents()
            )

        except Exception as error:
            logger.exception("Document loading failed.")

            raise DocumentError(
                "Unable to load the uploaded documents."
            ) from error

        # -----------------------------
        # Save processed documents
        # -----------------------------
        try:
            PROCESSED_DOCUMENTS_FILE.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            with open(
                PROCESSED_DOCUMENTS_FILE,
                "w",
                encoding="utf-8",
            ) as file:
                json.dump(
                    documents,
                    file,
                    indent=4,
                    ensure_ascii=False,
                )

        except Exception as error:
            logger.exception(
                "Failed to save processed documents."
            )

            raise DocumentError(
                "Unable to save processed documents."
            ) from error

        # -----------------------------
        # Chunk documents
        # -----------------------------
        try:
            chunks = self.chunker_factory(
                documents
            ).create_chunks()

        except Exception as error:
            logger.exception("Document chunking failed.")

            raise DocumentError(
                "Unable to prepare documents for indexing."
            ) from error

        # -----------------------------
        # Save chunks
        # -----------------------------
        try:
            CHUNKS_FILE.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            with open(
                CHUNKS_FILE,
                "w",
                encoding="utf-8",
            ) as file:
                json.dump(
                    chunks,
                    file,
                    indent=4,
                    ensure_ascii=False,
                )

        except Exception as error:
            logger.exception("Failed to save chunks.")

            raise DocumentError(
                "Unable to save generated chunks."
            ) from error

        # -----------------------------
        # Generate embeddings
        # -----------------------------
        try:
            embeddings = (
                self.embedding_model.generate_embeddings(
                    [chunk["text"] for chunk in chunks]
                )
            )

        except Exception as error:
            logger.exception(
                "Embedding generation failed."
            )

            raise EmbeddingError(
                "Unable to generate document embeddings."
            ) from error

        # -----------------------------
        # Save embeddings
        # -----------------------------
        try:
            EMBEDDINGS_FILE.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            np.save(
                EMBEDDINGS_FILE,
                embeddings,
            )

        except Exception as error:
            logger.exception(
                "Failed to save embeddings."
            )

            raise EmbeddingError(
                "Unable to save document embeddings."
            ) from error

        # -----------------------------
        # Update vector database
        # -----------------------------
        try:
            self.vector_store.add_documents(
                chunks,
                embeddings,
            )

        except Exception as error:
            logger.exception(
                "Vector database update failed."
            )

            raise DatabaseError(
                "Unable to update the vector database."
            ) from error

        # -----------------------------
        # Save SQLite metadata
        # -----------------------------
        try:
            for filename in {
                document["metadata"].get("source")
                for document in documents
            }:

                document_chunks = [
                    chunk
                    for chunk in chunks
                    if chunk["metadata"].get("source")
                    == filename
                ]

                document_id = (
                    self.document_repository.add_document(
                        filename=filename,
                        source=filename,
                        pages=max(
                            document["metadata"].get(
                                "page_number",
                                0,
                            )
                            for document in documents
                            if document["metadata"].get(
                                "source"
                            )
                            == filename
                        ),
                    )
                )

                self.document_repository.add_chunks(
                    document_id,
                    document_chunks,
                )

                embedding_model_name = getattr(
                    self.embedding_model,
                    "model_name",
                    self.embedding_model.__class__.__name__,
                )

                self.document_repository.add_embedding_metadata(
                    document_id,
                    embedding_model_name,
                    len(document_chunks),
                )

        except Exception as error:
            logger.exception(
                "Failed to save document metadata."
            )

            raise DatabaseError(
                "Unable to save document metadata."
            ) from error

        return {
            "documents": documents,
            "chunks": chunks,
            "embeddings": embeddings,
            "statistics": loader.get_statistics(),
        }