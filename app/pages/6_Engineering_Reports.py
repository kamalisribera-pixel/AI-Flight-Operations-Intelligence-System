import streamlit as st

from app.components.footer import render_footer
from app.components.navbar import render_navbar
from app.components.sidebar import render_sidebar
from app.runtime import get_query_service, initialize_state, load_styles


st.set_page_config(page_title="Engineering Reports | AI_FOIS", page_icon="✈️", layout="wide")
initialize_state(); load_styles(); render_sidebar(); render_navbar()
st.markdown("<div class='hero'><div class='eyebrow'>Decision archive / traceable outputs</div><h1>Engineering reports</h1><p>Review generated conclusions, recommendations, and risk assessments.</p></div>", unsafe_allow_html=True)

reports = get_query_service().report_service.recent()
if not reports:
    st.info("No reports have been generated yet.")
for report in reports:
    with st.expander(f"Report {report['report_id']} · {report['created_at']}"):
        st.markdown(report["summary"])
        if report["recommendation"]:
            st.markdown(f"**Recommendation**\n\n{report['recommendation']}")
        if report["risk"]:
            st.markdown(f"**Risk**\n\n{report['risk']}")
render_footer()
