import streamlit as st


def render_structured_report(report):
    st.markdown(f"## {report.get('title', 'Engineering Report')}")

    if report.get("system"):
        st.markdown("### Detected System")
        st.write(report["system"])

    if report.get("failure"):
        st.markdown("### Failure")
        st.write(report["failure"])

    st.markdown("### Summary")
    st.write(report.get("summary", "No summary available."))

    if report.get("recommendation"):
        st.markdown("### Recommendation")
        st.write(report["recommendation"])

    if report.get("risk"):
        st.markdown("### Risk")
        st.write(report["risk"])

    if report.get("references"):
        st.markdown("### References")
        st.write(report["references"])


def render_report_card(result):
    with st.container(border=True):
        st.markdown("### Engineering response")
        answer = result.get("answer", "")
        if isinstance(answer, dict):
            render_structured_report(answer)
        else:
            st.markdown(answer)
        references = result.get("retrieval", {}).get("metadatas", [[]])[0]
        if references:
            st.markdown("#### Retrieved references")
            for reference in references:
                st.markdown(
                    f"<div class='reference'><strong>{reference.get('source', 'Unknown document')}</strong> "
                    f"<small>Page {reference.get('page_number', 'N/A')}</small></div>",
                    unsafe_allow_html=True
                )
