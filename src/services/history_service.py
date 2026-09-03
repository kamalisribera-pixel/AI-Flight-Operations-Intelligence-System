from config.logging_config import logger

from src.database.database import Database
from src.database.history_repository import HistoryRepository
from src.database.report_repository import ReportRepository
from src.database.session_repository import SessionRepository
from src.exceptions import DatabaseError, ValidationError


class HistoryService:

    def __init__(self, database=None, session_id=None):

        self.database = database or Database()

        self.sessions = SessionRepository(self.database)
        self.queries = HistoryRepository(self.database)
        self.reports = ReportRepository(self.database)

        try:
            self.session_id = (
                session_id
                or self.sessions.create_session()
            )

        except Exception as error:
            logger.exception(
                "Failed to initialize history session."
            )

            raise DatabaseError(
                "Unable to initialize session history."
            ) from error

    def save(self, question, answer):

        query_id = self.save_query(question)

        return self.save_report(
            query_id,
            answer,
        )

    def save_query(self, question):

        if not question or not question.strip():
            raise ValidationError(
                "Question cannot be empty."
            )

        try:
            self.sessions.touch(self.session_id)

            return self.queries.save_query(
                self.session_id,
                question,
            )

        except Exception as error:

            logger.exception(
                "Failed to save query."
            )

            raise DatabaseError(
                "Unable to save query history."
            ) from error

    def save_report(
        self,
        query_id,
        answer,
        recommendation="",
        risk="",
    ):

        if not answer or not str(answer).strip():
            raise ValidationError(
                "Answer cannot be empty."
            )

        try:
            return self.reports.save_report(
                query_id,
                answer,
                recommendation,
                risk,
            )

        except Exception as error:

            logger.exception(
                "Failed to save report."
            )

            raise DatabaseError(
                "Unable to save engineering report."
            ) from error

    def save_tool_result(
        self,
        query_id,
        agent_name,
        result,
        execution_time=None,
    ):

        try:
            return self.reports.save_tool_result(
                query_id,
                agent_name,
                result,
                execution_time,
            )

        except Exception as error:

            logger.exception(
                "Failed to save tool result."
            )

            raise DatabaseError(
                "Unable to save tool execution."
            ) from error

    def recent(self, limit=20):

        try:
            return self.queries.get_queries(
                self.session_id,
                limit,
            )

        except Exception as error:

            logger.exception(
                "Failed to retrieve query history."
            )

            raise DatabaseError(
                "Unable to retrieve query history."
            ) from error