import streamlit as st

from app.components.footer import render_footer
from app.components.navbar import render_navbar
from app.components.sidebar import render_sidebar
from app.components.status_card import render_status_card
from app.runtime import initialize_state, load_styles


st.set_page_config(page_title="Home | AI_FOIS", page_icon="✈️", layout="wide")
initialize_state()
load_styles()
render_sidebar()
render_navbar()

st.markdown(
    """
    <div class="hero">
      <div class="eyebrow">Aerospace engineering decision support</div>
      <h1>Read the manual.<br>Make the call.</h1>
      <p>FOIS turns technical PDFs into searchable, cited intelligence for flight operations and maintenance teams.</p>
    </div>
    """,
    unsafe_allow_html=True
)

left, right = st.columns([1.5, 1])
with left:
    st.markdown("### One operational loop")
    st.markdown("""
    <div class="pipeline"><span>Upload</span><i>→</i><span>Retrieve</span><i>→</i><span>Reason</span><i>→</i><span>Report</span></div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="panel"><h3>Built for grounded answers</h3>
    <p>Every response starts with your indexed aerospace documents. References, agent reasoning, risk, and recommendations remain close to the source material.</p>
    <p class="eyebrow">RAG / AGENTS / TRACEABILITY</p></div>
    """, unsafe_allow_html=True)
with right:
    st.markdown("### System profile")
    a, b = st.columns(2)
    with a: render_status_card("Knowledge source", "PDF")
    with b: render_status_card("Vector search", "Chroma", "amber")
    st.markdown(" ")
    a, b = st.columns(2)
    with a: render_status_card("Reasoning", "LLM")
    with b: render_status_card("Memory", "SQLite", "amber")

st.markdown("### Technology stack")
for title, text in [("Knowledge", "PyMuPDF · Sentence Transformers · ChromaDB"), ("Reasoning", "Ollama · Llama · Specialized engineering tools"), ("Interface", "Streamlit · Modular services · Persistent history")]:
    st.markdown(f"<div class='panel'><h3>{title}</h3><p>{text}</p></div>", unsafe_allow_html=True)
render_footer()
