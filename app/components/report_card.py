import streamlit as st


def render_report_card(result):
    st.markdown("### Engineering response")
    st.markdown(result.get("answer", ""))
    references = result.get("retrieval", {}).get("metadatas", [[]])[0]
    if references:
        st.markdown("#### Retrieved references")
        for reference in references:
            st.markdown(
                f"<div class='reference'><strong>{reference.get('source', 'Unknown document')}</strong> "
                f"<small>Page {reference.get('page_number', 'N/A')}</small></div>",
                unsafe_allow_html=True
            )
