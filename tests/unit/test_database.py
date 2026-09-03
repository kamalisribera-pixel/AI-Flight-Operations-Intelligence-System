from pathlib import Path

from src.database.database import Database
from src.database.history_repository import HistoryRepository
from src.database.session_repository import SessionRepository


def test_database_creates_session_and_query(tmp_path):
    database = Database(tmp_path / "fois.db", Path("database/schema.sql"))
    session_id = SessionRepository(database).create_session()
    query_id = HistoryRepository(database).save_query(session_id, "What is lift?")
    assert session_id > 0
    assert query_id > 0