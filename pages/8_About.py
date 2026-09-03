import streamlit as st

from app.components.footer import render_footer
from app.components.navbar import render_navbar
from app.components.sidebar import render_sidebar
from app.runtime import initialize_state, load_styles


st.set_page_config(page_title="About | AI_FOIS", page_icon="✈️", layout="wide")
initialize_state(); load_styles(); render_sidebar(); render_navbar()
st.markdown("<div class='hero'><div class='eyebrow'>System brief / version 0.1.0</div><h1>About FOIS</h1><p>A modular aerospace intelligence platform for document-grounded analysis and operational decision support.</p></div>", unsafe_allow_html=True)

for title, body in [("Architecture", "Streamlit presents the workspace. Services orchestrate ingestion, retrieval, generation, agents, reports, and history. SQLite stores application memory while ChromaDB stores vector search data."), ("Dataset", "FOIS is designed for technical aerospace PDFs including maintenance manuals, operating handbooks, procedures, and engineering references."), ("Engineering decisions", "Responses are grounded in retrieved source material, cite document references where available, and separate document evidence from interpretation."), ("Technology", "Python · Streamlit · PyMuPDF · Sentence Transformers · ChromaDB · SQLite · Ollama")]:
    st.markdown(f"<div class='panel'><h3>{title}</h3><p>{body}</p></div>", unsafe_allow_html=True)
render_footer()
