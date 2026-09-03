import streamlit as st

from app.components.footer import render_footer
from app.components.navbar import render_navbar
from app.components.sidebar import render_sidebar
from app.runtime import get_query_service, initialize_state, load_styles


st.set_page_config(page_title="History | AI_FOIS", page_icon="✈️", layout="wide")
initialize_state(); load_styles(); render_sidebar(); render_navbar()
st.markdown("<div class='hero'><div class='eyebrow'>Session memory / previous analyses</div><h1>History</h1><p>Search the questions and responses recorded in this session.</p></div>", unsafe_allow_html=True)

search = st.text_input("Search history", placeholder="Filter by question or answer")
rows = get_query_service().history_service.recent(100)
for row in rows:
    text = f"{row.get('question', '')} {row.get('answer') or ''}"
    if search.lower() in text.lower():
        with st.expander(f"{row['question']} · {row.get('created_at', row.get('timestamp', ''))}"):
            st.markdown(row.get("answer") or "No report saved yet.")
if not rows:
    st.info("No questions recorded in this session.")
render_footer()
