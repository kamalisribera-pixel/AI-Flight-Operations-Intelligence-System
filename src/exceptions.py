class AppError(Exception):
    """Base application exception."""


class ConfigurationError(AppError):
    """Raised when application configuration is invalid."""


class ValidationError(AppError):
    """Raised when user input is invalid."""


class DocumentError(AppError):
    """Raised during document ingestion."""


class IngestionError(DocumentError):
    """Backward-compatible alias for ingestion failures."""


class EmbeddingError(AppError):
    """Raised while generating embeddings."""


class RetrievalError(AppError):
    """Raised during document retrieval."""


class GenerationError(AppError):
    """Raised during LLM response generation."""


class AgentError(AppError):
    """Raised by engineering agents."""


class DatabaseError(AppError):
    """Raised for SQLite/ChromaDB failures."""


class ExportError(AppError):
    """Raised while exporting reports."""