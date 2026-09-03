import sqlite3
from contextlib import contextmanager
from pathlib import Path

from config.settings import APP_DATABASE_FILE, DATABASE_SCHEMA_FILE
from config.logging_config import logger
from src.exceptions import DatabaseError


class Database:

    def __init__(self, database_path=APP_DATABASE_FILE, schema_path=DATABASE_SCHEMA_FILE):
        self.database_path = Path(database_path)
        self.schema_path = Path(schema_path)
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self.initialize()

    @contextmanager
    def connection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.database_path)
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA foreign_keys = ON")
            yield connection
            connection.commit()
        except Exception as error:
            if connection is not None:
                connection.rollback()
            logger.exception("Database operation failed")
            if isinstance(error, DatabaseError):
                raise
            raise DatabaseError("Database operation failed.") from error
        finally:
            if connection is not None:
                connection.close()

    def initialize(self):
        try:
            schema = self.schema_path.read_text(encoding="utf-8")
            with self.connection() as connection:
                connection.executescript(schema)
        except DatabaseError:
            raise
        except Exception as error:
            logger.exception("Database initialization failed")
            raise DatabaseError("Database initialization failed.") from error
