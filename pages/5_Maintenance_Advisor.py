import streamlit as st

from app.components.footer import render_footer
from app.components.navbar import render_navbar
from app.components.sidebar import render_sidebar
from app.runtime import get_agent_service, initialize_state, load_styles


st.set_page_config(page_title="Maintenance Advisor | AI_FOIS", page_icon="✈️", layout="wide")
initialize_state(); load_styles(); render_sidebar(); render_navbar()
st.markdown("<div class='hero compact-hero'><div class='eyebrow'>Maintenance workspace / inspection planning</div><h1>Maintenance advisor</h1><p>Turn a field observation into a structured troubleshooting and inspection request.</p></div>", unsafe_allow_html=True)

system = st.text_input("System or component", placeholder="Fuel control unit")
request = st.text_area("Repair or inspection question", placeholder="What should I inspect first and what precautions apply?")
if st.button("Generate maintenance guidance", type="primary"):
    if not system or not request:
        st.warning("Add a system and maintenance question.")
    else:
        with st.spinner("Preparing maintenance guidance..."):
            answer = get_agent_service().analyze(f"Maintenance failure: {system}. {request}")
        with st.container(border=True):

            st.markdown("### Recommended Guidance")

            st.markdown(f"**System**")
            st.write(answer["system"])

            st.markdown("**Engineering Assessment**")
            st.write(answer["summary"])

            st.markdown("**Maintenance Actions**")
            for item in answer["maintenance"]:
                st.markdown(f"- {item}")

            st.markdown("**Troubleshooting**")
            for item in answer["troubleshooting"]:
                st.markdown(f"- {item}")

            st.markdown("**Likely Root Causes**")
            for cause in answer["root_causes"]:
                st.markdown(
                    f"- **{cause['cause']}** ({cause['probability']})"
                )

            st.markdown("**Flight Impact**")
            for item in answer["flight_impact"]:
                st.markdown(f"- {item}")

            st.markdown("**Recommended Procedures**")
            for item in answer["procedures"]:
                st.markdown(f"- {item}")

            st.markdown("**Risk Level**")
            st.info(answer["risk"])
render_footer()
