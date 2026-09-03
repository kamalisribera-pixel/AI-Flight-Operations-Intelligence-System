from config.logging_config import logger

from src.database.report_repository import ReportRepository
from src.exceptions import DatabaseError, ValidationError


class ReportService:

    def __init__(self, repository=None):
        self.repository = repository or ReportRepository()

    def create(
        self,
        question,
        answer,
        context="",
        analysis=None,
    ):

        if not question or not question.strip():
            raise ValidationError(
                "Question cannot be empty."
            )

        if not answer or not str(answer).strip():
            raise ValidationError(
                "Answer cannot be empty."
            )

        logger.info(
            "Engineering report created."
        )

        if isinstance(analysis, dict):
            report = dict(analysis)
        else:
            report = {
                "title": "Engineering Report",
                "summary": str(answer),
                "recommendation": "",
                "risk": "",
                "references": [],
            }

        report.setdefault("title", "Engineering Report")
        report.setdefault("system", "")
        report.setdefault("failure", question)
        report.setdefault("summary", str(answer))
        report.setdefault("recommendation", "")
        report.setdefault("risk", "")
        report.setdefault("references", [])
        report.update({
            "question": question,
            "answer": answer,
            "context": context,
            "analysis": analysis,
        })
        return report

    def recent(self, limit=50):

        try:
            return self.repository.recent(limit)

        except Exception as error:

            logger.exception(
                "Unable to retrieve engineering reports."
            )

            raise DatabaseError(
                "Unable to load engineering reports."
            ) from error