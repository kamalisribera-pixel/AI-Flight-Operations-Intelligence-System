import logging

import streamlit as st

from src.exceptions import (
    AgentError,
    AppError,
    ConfigurationError,
    DatabaseError,
    DocumentError,
    EmbeddingError,
    ExportError,
    GenerationError,
    RetrievalError,
    ValidationError,
)

logger = logging.getLogger(__name__)


def handle_exception(error: Exception) -> None:
    """
    Centralized exception handler for the Streamlit application.
    """

    logger.exception(error)

    if isinstance(error, ConfigurationError):
        st.error(
            "⚙️ Configuration Error\n\n"
            "The application configuration is invalid. "
            "Please verify your settings and restart the application."
        )

    elif isinstance(error, ValidationError):
        st.warning(
            f"⚠️ {error}"
        )

    elif isinstance(error, DocumentError):
        st.error(
            "📄 Document Processing Error\n\n"
            "The uploaded document could not be processed."
        )

    elif isinstance(error, EmbeddingError):
        st.error(
            "🧠 Embedding Generation Failed\n\n"
            "Unable to generate document embeddings."
        )

    elif isinstance(error, RetrievalError):
        st.error(
            "🔍 Retrieval Error\n\n"
            "No relevant information could be retrieved from the knowledge base."
        )

    elif isinstance(error, GenerationError):
        st.error(
            "🤖 AI Generation Error\n\n"
            "The language model could not generate a response."
        )

    elif isinstance(error, AgentError):
        st.error(
            "🛠 Engineering Agent Error\n\n"
            "The engineering analysis could not be completed."
        )

    elif isinstance(error, DatabaseError):
        st.error(
            "🗄 Database Error\n\n"
            "Unable to access the application database."
        )

    elif isinstance(error, ExportError):
        st.error(
            "📄 Export Error\n\n"
            "The report could not be exported."
        )

    elif isinstance(error, AppError):
        st.error(str(error))

    else:
        st.error(
            "❌ Unexpected Error\n\n"
            "An unexpected error occurred.\n\n"
            "Please check the application logs for more details."
        )

    st.stop()