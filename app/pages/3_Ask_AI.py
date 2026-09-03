import streamlit as st

from app.components.chat_box import render_chat_history
from app.components.footer import render_footer
from app.components.navbar import render_navbar
from app.components.report_card import render_report_card
from app.components.sidebar import render_sidebar
from app.runtime import get_query_service, initialize_state, load_styles
from src.exceptions import AppError


st.set_page_config(page_title="Ask AI | AI_FOIS", page_icon="✈️", layout="wide")
initialize_state(); load_styles(); render_sidebar(); render_navbar()
st.markdown("<div class='hero'><div class='eyebrow'>Operational copilot / grounded retrieval</div><h1>Ask AI</h1><p>Ask a question across your indexed aerospace manuals and receive a cited engineering response.</p></div>", unsafe_allow_html=True)

question = st.chat_input("Ask about a system, procedure, or failure...")
if question:
    try:
        with st.spinner("Retrieving evidence and composing response..."):
            result = get_query_service().ask(question)
    except AppError as error:
        st.error(str(error))
        st.stop()
    st.session_state.chat_history.append({"question": question, "answer": result["answer"]})
    st.session_state.selected_report = result
    render_report_card(result)
render_chat_history()
render_footer()
