import json
import re

import numpy as np

from config.settings import CHUNKS_FILE, DOCUMENTS_DIR, EMBEDDINGS_FILE, PROCESSED_DOCUMENTS_FILE
from src.database.vector_store import AerospaceVectorStore
from src.database.document_repository import DocumentRepository
from src.embeddings.embedding_model import AerospaceEmbeddingModel
from src.ingestion.chunker import AerospaceDocumentChunker
from src.ingestion.document_loader import AerospaceDocumentLoader
from src.exceptions import IngestionError
from config.logging_config import logger


class IngestionService:

	def __init__(
		self,
		loader_factory=AerospaceDocumentLoader,
		chunker_factory=AerospaceDocumentChunker,
		embedding_model=None,
		vector_store=None,
		document_repository=None
	):
		self.loader_factory = loader_factory
		self.chunker_factory = chunker_factory
		self.embedding_model = embedding_model or AerospaceEmbeddingModel()
		self.vector_store = vector_store or AerospaceVectorStore()
		self.document_repository = document_repository or DocumentRepository()

	@staticmethod
	def _clean_documents(documents):
		cleaned = []
		for document in documents:
			text = re.sub(r"\s+", " ", document["text"]).strip()
			if text:
				cleaned.append({"text": text, "metadata": document["metadata"]})
		return cleaned

	def ingest(self, directory=DOCUMENTS_DIR):
		try:
			loader = self.loader_factory(directory)
			documents = self._clean_documents(loader.load_documents())
		except Exception as error:
			logger.exception("Document ingestion failed during loading")
			raise IngestionError(
				"Documents could not be loaded. Verify the PDF files and try again."
			) from error
		PROCESSED_DOCUMENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
		with open(PROCESSED_DOCUMENTS_FILE, "w", encoding="utf-8") as file:
			json.dump(documents, file, indent=4, ensure_ascii=False)

		chunks = self.chunker_factory(documents).create_chunks()
		CHUNKS_FILE.parent.mkdir(parents=True, exist_ok=True)
		with open(CHUNKS_FILE, "w", encoding="utf-8") as file:
			json.dump(chunks, file, indent=4, ensure_ascii=False)

		try:
			embeddings = self.embedding_model.generate_embeddings(
			[chunk["text"] for chunk in chunks]
		)
		except Exception as error:
			logger.exception("Embedding generation failed")
			raise IngestionError(
				"Embeddings could not be generated. Check the embedding model."
			) from error
		EMBEDDINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
		np.save(EMBEDDINGS_FILE, embeddings)
		try:
			self.vector_store.add_documents(chunks, embeddings)
		except Exception as error:
			logger.exception("Vector database update failed")
			raise IngestionError(
				"The vector database could not be updated. Check database access."
			) from error

		for filename in {document["metadata"].get("source") for document in documents}:
			document_chunks = [
				chunk for chunk in chunks
				if chunk["metadata"].get("source") == filename
			]
			document_id = self.document_repository.add_document(
				filename=filename,
				source=filename,
				pages=max(
					document["metadata"].get("page_number", 0)
					for document in documents
					if document["metadata"].get("source") == filename
				)
			)
			self.document_repository.add_chunks(document_id, document_chunks)
			embedding_model_name = getattr(
				self.embedding_model, "model_name", self.embedding_model.__class__.__name__
			)
			self.document_repository.add_embedding_metadata(
				document_id,
				embedding_model_name,
				len(document_chunks)
			)

		return {
			"documents": documents,
			"chunks": chunks,
			"embeddings": embeddings,
			"statistics": loader.get_statistics()
		}
