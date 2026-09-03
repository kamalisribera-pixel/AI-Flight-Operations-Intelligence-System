from src.database.database import Database


class HistoryRepository:

    def __init__(self, database=None):
        self.database = database or Database()

    def save_query(self, session_id, question):
        with self.database.connection() as connection:
            cursor = connection.execute(
                "INSERT INTO queries (session_id, question) VALUES (?, ?)",
                (session_id, question)
            )
            return cursor.lastrowid

    def get_queries(self, session_id, limit=20):
        with self.database.connection() as connection:
            rows = connection.execute(
                "SELECT q.query_id AS id, q.query_id, q.session_id, q.question, "
                "q.timestamp, r.summary AS answer, r.created_at "
                "FROM queries q LEFT JOIN reports r ON r.query_id = q.query_id "
                "WHERE q.session_id = ? "
                "ORDER BY q.query_id DESC LIMIT ?",
                (session_id, limit)
            ).fetchall()
        return [dict(row) for row in rows]
