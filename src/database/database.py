import sqlite3
from contextlib import contextmanager
from pathlib import Path

from config.settings import APP_DATABASE_FILE, DATABASE_SCHEMA_FILE


class Database:

    def __init__(self, database_path=APP_DATABASE_FILE, schema_path=DATABASE_SCHEMA_FILE):
        self.database_path = Path(database_path)
        self.schema_path = Path(schema_path)
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self.initialize()

    @contextmanager
    def connection(self):
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        try:
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def initialize(self):
        schema = self.schema_path.read_text(encoding="utf-8")
        with self.connection() as connection:
            connection.executescript(schema)
