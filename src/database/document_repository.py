import json

from src.database.database import Database


class DocumentRepository:

    def __init__(self, database=None):
        self.database = database or Database()

    def add_document(self, filename, source, pages=0, status="processed"):
        with self.database.connection() as connection:
            cursor = connection.execute(
                "INSERT INTO documents (filename, source, pages, status) VALUES (?, ?, ?, ?)",
                (filename, source, pages, status)
            )
            return cursor.lastrowid

    def add_chunks(self, document_id, chunks):
        with self.database.connection() as connection:
            connection.executemany(
                "INSERT INTO chunks (document_id, chunk_index, text, metadata) VALUES (?, ?, ?, ?)",
                [
                    (document_id, index, chunk["text"], json.dumps(chunk.get("metadata", {})))
                    for index, chunk in enumerate(chunks)
                ]
            )

    def add_embedding_metadata(self, document_id, embedding_model, chunk_count):
        with self.database.connection() as connection:
            cursor = connection.execute(
                "INSERT INTO embedding_metadata "
                "(document_id, embedding_model, chunk_count) VALUES (?, ?, ?)",
                (document_id, embedding_model, chunk_count)
            )
            return cursor.lastrowid
