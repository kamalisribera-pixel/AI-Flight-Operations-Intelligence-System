import streamlit as st


def render_status_card(label, value, accent="cyan"):
    st.markdown(
        f"<div class='metric' style='border-color:var(--{accent})'>"
        f"<strong style='color:var(--{accent})'>{value}</strong><span>{label}</span></div>",
        unsafe_allow_html=True
    )
