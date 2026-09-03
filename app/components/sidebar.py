import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.markdown("## AI_FOIS")
        st.caption("Engineering decision support")
        st.divider()
        st.markdown("**SYSTEM STATUS**")
        st.markdown('<span class="status">Operational</span>', unsafe_allow_html=True)
        st.markdown(" ")
        st.caption("Use the page navigation to move between knowledge, analysis, and reports.")
        if st.button("New session"):
            st.session_state.pop("query_service", None)
            st.session_state.pop("chat_history", None)
            st.rerun()
