from pathlib import Path

import streamlit as st

from src.services.agent_service import AgentService
from src.services.ingestion_service import IngestionService
from src.services.query_service import QueryService


ROOT = Path(__file__).resolve().parent


def load_styles():
    css = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


@st.cache_resource
def _cached_query_service():
    return QueryService()


def get_query_service():
    if "query_service" not in st.session_state:
        st.session_state.query_service = _cached_query_service()
    return st.session_state.query_service


@st.cache_resource
def _cached_agent_service():
    return AgentService()


def get_agent_service():
    if "agent_service" not in st.session_state:
        st.session_state.agent_service = _cached_agent_service()
    return st.session_state.agent_service


@st.cache_resource
def _cached_ingestion_service():
    return IngestionService()


def get_ingestion_service():
    if "ingestion_service" not in st.session_state:
        st.session_state.ingestion_service = _cached_ingestion_service()
    return st.session_state.ingestion_service


def initialize_state():
    defaults = {
        "chat_history": [],
        "uploaded_documents": [],
        "selected_report": None,
        "theme": "operations",
        "current_page": "Home"
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)
