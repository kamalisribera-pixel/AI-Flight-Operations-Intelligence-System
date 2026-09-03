from config.config import RETRIEVAL_TOP_K
from config.logging_config import logger

from src.exceptions import RetrievalError, ValidationError
from src.retrieval.retriever import AerospaceRetriever


class RetrievalService:

    def __init__(self, retriever=None):
        self.retriever = retriever or AerospaceRetriever()

    def retrieve(self, question, top_k=RETRIEVAL_TOP_K):

        if not question or not question.strip():
            raise ValidationError(
                "Please enter a question before searching the manuals."
            )

        try:
            results = self.retriever.retrieve(
                question,
                top_k=top_k
            )

        except Exception as error:
            logger.exception(
                "Document retrieval failed."
            )

            raise RetrievalError(
                "Unable to search the knowledge base."
            ) from error

        if not results.get("documents", [[]])[0]:

            logger.warning(
                "No relevant documents found for query: %s",
                question
            )

            raise RetrievalError(
                "No relevant documents were found."
            )

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