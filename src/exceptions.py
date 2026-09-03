class AppError(Exception):
    """Expected, user-displayable application failure."""


class RetrievalError(AppError):
    pass


class GenerationError(AppError):
    pass


class IngestionError(AppError):
    pass