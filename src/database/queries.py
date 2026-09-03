SAVE_QUERY = "INSERT INTO queries (session_id, question) VALUES (?, ?)"
SAVE_REPORT = (
    "INSERT INTO reports (query_id, summary, recommendation, risk) "
    "VALUES (?, ?, ?, ?)"
)
SAVE_TOOL_RESULT = (
    "INSERT INTO tool_results (query_id, agent_name, result, execution_time) "
    "VALUES (?, ?, ?, ?)"
)
