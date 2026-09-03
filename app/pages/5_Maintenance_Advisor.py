import streamlit as st

from app.components.footer import render_footer
from app.components.navbar import render_navbar
from app.components.sidebar import render_sidebar
from app.runtime import get_agent_service, initialize_state, load_styles


st.set_page_config(page_title="Maintenance Advisor | AI_FOIS", page_icon="✈️", layout="wide")
initialize_state(); load_styles(); render_sidebar(); render_navbar()
st.markdown("<div class='hero'><div class='eyebrow'>Maintenance workspace / inspection planning</div><h1>Maintenance advisor</h1><p>Turn a field observation into a structured troubleshooting and inspection request.</p></div>", unsafe_allow_html=True)

system = st.text_input("System or component", placeholder="Fuel control unit")
request = st.text_area("Repair or inspection question", placeholder="What should I inspect first and what precautions apply?")
if st.button("Generate maintenance guidance", type="primary"):
    if not system or not request:
        st.warning("Add a system and maintenance question.")
    else:
        with st.spinner("Preparing maintenance guidance..."):
            answer = get_agent_service().analyze(f"Maintenance failure: {system}. {request}")
        st.markdown("### Recommended guidance")
        st.markdown(answer)
render_footer()
