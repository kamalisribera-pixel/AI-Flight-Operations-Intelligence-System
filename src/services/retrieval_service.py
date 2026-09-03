from config.config import RETRIEVAL_TOP_K
from src.retrieval.retriever import AerospaceRetriever
from src.exceptions import RetrievalError
from config.logging_config import logger


class RetrievalService:

	def __init__(self, retriever=None):
		self.retriever = retriever or AerospaceRetriever()

	def retrieve(self, question, top_k=RETRIEVAL_TOP_K):
		if not question or not question.strip():
			raise RetrievalError("Enter a question before searching the manuals.")
		try:
			results = self.retriever.retrieve(question, top_k=top_k)
		except Exception as error:
			logger.exception("Retrieval failed")
			raise RetrievalError("Manual search is currently unavailable.") from error
		if not results.get("documents", [[]])[0]:
			logger.warning("No documents retrieved for query")
			raise RetrievalError("No relevant documents were found.")
		return results

	def build_context(self, question, top_k=RETRIEVAL_TOP_K):
		results = self.retrieve(question, top_k)
		context_parts = []
		for document, metadata in zip(
			results.get("documents", [[]])[0],
			results.get("metadatas", [[]])[0]
		):
			context_parts.append(
				f"Document:\n{metadata.get('source')}\n\n"
				f"Page:\n{metadata.get('page_number')}\n\n"
				f"Content:\n{document}"
			)
		return "\n\n".join(context_parts), results
