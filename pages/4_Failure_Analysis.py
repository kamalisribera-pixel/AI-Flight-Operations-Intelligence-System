import streamlit as st

from app.components.footer import render_footer
from app.components.navbar import render_navbar
from app.components.report_card import render_structured_report
from app.components.sidebar import render_sidebar
from app.runtime import get_agent_service, initialize_state, load_styles


st.set_page_config(page_title="Failure Analysis | AI_FOIS", page_icon="✈️", layout="wide")
initialize_state(); load_styles(); render_sidebar(); render_navbar()
st.markdown("<div class='hero compact-hero'><div class='eyebrow'>Agent workspace / fault isolation</div><h1>Failure analysis</h1><p>Describe the observed condition and let the engineering agent assemble causes, impact, risk, and next actions.</p></div>", unsafe_allow_html=True)

system = st.text_input("Affected system", placeholder="Hydraulic system")
symptom = st.text_input("Observed symptom", placeholder="Pressure drops during extension")
failure = st.text_area("Failure description", placeholder="Include timing, indications, and operating conditions.")
if st.button("Analyze failure", type="primary"):
    prompt = f"Failure in {system}: {symptom}. {failure}"
    if not system or not symptom:
        st.warning("Add a system and observed symptom.")
    else:
        with st.spinner("Running failure analysis agents..."):
            answer = get_agent_service().analyze(prompt)
        with st.container(border=True):
            if isinstance(answer, dict):
                render_structured_report(answer)
            else:
                st.markdown(answer)
render_footer()
