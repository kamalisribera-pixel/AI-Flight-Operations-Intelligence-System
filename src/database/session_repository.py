from datetime import datetime, timezone

from src.database.database import Database


class SessionRepository:

    def __init__(self, database=None):
        self.database = database or Database()

    def create_session(self):
        now = datetime.now(timezone.utc).isoformat()
        with self.database.connection() as connection:
            cursor = connection.execute(
                "INSERT INTO sessions (created_at, last_active) VALUES (?, ?)",
                (now, now)
            )
            return cursor.lastrowid

    def touch(self, session_id):
        with self.database.connection() as connection:
            connection.execute(
                "UPDATE sessions SET last_active = CURRENT_TIMESTAMP WHERE session_id = ?",
                (session_id,)
            )

    def get(self, session_id):
        with self.database.connection() as connection:
            row = connection.execute(
                "SELECT * FROM sessions WHERE session_id = ?", (session_id,)
            ).fetchone()
        return dict(row) if row else None
