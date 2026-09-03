CREATE TABLE IF NOT EXISTS documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    source TEXT NOT NULL,
    upload_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    pages INTEGER NOT NULL DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'processed'
);

CREATE TABLE IF NOT EXISTS chunks (
    chunk_id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER NOT NULL,
    chunk_index INTEGER NOT NULL,
    text TEXT NOT NULL,
    metadata TEXT NOT NULL DEFAULT '{}',
    FOREIGN KEY (document_id) REFERENCES documents(document_id)
);

CREATE TABLE IF NOT EXISTS embedding_metadata (
    embedding_id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER NOT NULL,
    embedding_model TEXT NOT NULL,
    chunk_count INTEGER NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (document_id) REFERENCES documents(document_id)
);

CREATE TABLE IF NOT EXISTS sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_active TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS queries (
    query_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id)
);

CREATE TABLE IF NOT EXISTS reports (
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    query_id INTEGER NOT NULL,
    summary TEXT NOT NULL,
    recommendation TEXT NOT NULL DEFAULT '',
    risk TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (query_id) REFERENCES queries(query_id)
);

CREATE TABLE IF NOT EXISTS tool_results (
    tool_result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    query_id INTEGER NOT NULL,
    agent_name TEXT NOT NULL,
    result TEXT NOT NULL,
    execution_time REAL,
    FOREIGN KEY (query_id) REFERENCES queries(query_id)
);

CREATE INDEX IF NOT EXISTS idx_queries_session_id ON queries(session_id);
CREATE INDEX IF NOT EXISTS idx_reports_query_id ON reports(query_id);
CREATE INDEX IF NOT EXISTS idx_tool_results_query_id ON tool_results(query_id);
