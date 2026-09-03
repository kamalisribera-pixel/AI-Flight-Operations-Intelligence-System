import streamlit as st

from app.components.navbar import render_navbar
from app.components.sidebar import render_sidebar
from app.runtime import initialize_state, load_styles


st.set_page_config(page_title="AI_FOIS", page_icon="✈️", layout="wide")
initialize_state()
load_styles()
render_sidebar()
render_navbar()

st.title("AI Flight Operations Intelligence System")
st.caption("Aerospace engineering decision support")

st.info("Choose Home from the page navigation to begin.")
