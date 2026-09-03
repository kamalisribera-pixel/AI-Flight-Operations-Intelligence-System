from src.database.database import Database
from src.database.history_repository import HistoryRepository
from src.database.report_repository import ReportRepository
from src.database.session_repository import SessionRepository


class HistoryService:

	def __init__(self, database=None, session_id=None):
		self.database = database or Database()
		self.sessions = SessionRepository(self.database)
		self.queries = HistoryRepository(self.database)
		self.reports = ReportRepository(self.database)
		self.session_id = session_id or self.sessions.create_session()

	def save(self, question, answer):
		query_id = self.save_query(question)
		return self.save_report(query_id, answer)

	def save_query(self, question):
		self.sessions.touch(self.session_id)
		return self.queries.save_query(self.session_id, question)

	def save_report(self, query_id, answer, recommendation="", risk=""):
		return self.reports.save_report(query_id, answer, recommendation, risk)

	def save_tool_result(self, query_id, agent_name, result, execution_time=None):
		return self.reports.save_tool_result(
			query_id, agent_name, result, execution_time
		)

	def recent(self, limit=20):
		rows = self.queries.get_queries(self.session_id, limit)
		return rows
