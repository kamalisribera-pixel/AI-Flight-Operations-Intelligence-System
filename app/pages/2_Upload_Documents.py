import time
from pathlib import Path

import streamlit as st

from app.components.footer import render_footer
from app.components.navbar import render_navbar
from app.components.sidebar import render_sidebar
from app.runtime import get_ingestion_service, initialize_state, load_styles
from config.settings import DOCUMENTS_DIR
from src.exceptions import AppError


st.set_page_config(page_title="Upload Documents | AI_FOIS", page_icon="✈️", layout="wide")
initialize_state(); load_styles(); render_sidebar(); render_navbar()
st.markdown("<div class='hero'><div class='eyebrow'>Knowledge base / ingestion</div><h1>Upload manuals</h1><p>Load PDF source material into the searchable FOIS knowledge base.</p></div>", unsafe_allow_html=True)

files = st.file_uploader("PDF documents", type=["pdf"], accept_multiple_files=True)
if files and st.button("Process documents", type="primary"):
    DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
    for uploaded in files:
        target = DOCUMENTS_DIR / Path(uploaded.name).name
        target.write_bytes(uploaded.getbuffer())
        st.session_state.uploaded_documents.append(uploaded.name)
    started = time.perf_counter()
    try:
        with st.spinner("Extracting, chunking, embedding, and indexing..."):
            result = get_ingestion_service().ingest(DOCUMENTS_DIR)
    except AppError as error:
        st.error(str(error))
        st.stop()
    elapsed = time.perf_counter() - started
    stats = result["statistics"]
    c1, c2, c3 = st.columns(3)
    c1.metric("Documents", stats["documents_processed"])
    c2.metric("Chunks", len(result["chunks"]))
    c3.metric("Elapsed", f"{elapsed:.1f}s")
    st.success("Knowledge base updated successfully.")

if st.session_state.uploaded_documents:
    st.markdown("### Uploaded this session")
    for name in st.session_state.uploaded_documents:
        st.markdown(f"<div class='reference'><strong>{name}</strong> <small>PDF source</small></div>", unsafe_allow_html=True)
render_footer()
