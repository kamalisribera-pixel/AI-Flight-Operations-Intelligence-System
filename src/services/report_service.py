from src.database.report_repository import ReportRepository


class ReportService:

	def __init__(self, repository=None):
		self.repository = repository or ReportRepository()

	def create(self, question, answer, context="", analysis=None):
		return {
			"question": question,
			"answer": answer,
			"context": context,
			"analysis": analysis
		}

	def recent(self, limit=50):
		return self.repository.recent(limit)
