from src.database.database import Database


class ReportRepository:

    def __init__(self, database=None):
        self.database = database or Database()

    def save_report(self, query_id, summary, recommendation="", risk=""):
        with self.database.connection() as connection:
            cursor = connection.execute(
                "INSERT INTO reports (query_id, summary, recommendation, risk) "
                "VALUES (?, ?, ?, ?)",
                (query_id, summary, recommendation, risk)
            )
            return cursor.lastrowid

    def get_report(self, report_id):
        with self.database.connection() as connection:
            row = connection.execute(
                "SELECT * FROM reports WHERE report_id = ?", (report_id,)
            ).fetchone()
        return dict(row) if row else None

    def recent(self, limit=50):
        with self.database.connection() as connection:
            rows = connection.execute(
                "SELECT * FROM reports ORDER BY report_id DESC LIMIT ?",
                (limit,)
            ).fetchall()
        return [dict(row) for row in rows]

    def save_tool_result(self, query_id, agent_name, result, execution_time=None):
        with self.database.connection() as connection:
            cursor = connection.execute(
                "INSERT INTO tool_results "
                "(query_id, agent_name, result, execution_time) VALUES (?, ?, ?, ?)",
                (query_id, agent_name, result, execution_time)
            )
            return cursor.lastrowid
