import streamlit as st


def render_chat_history():
    for item in st.session_state.get("chat_history", []):
        with st.chat_message("user"):
            st.write(item["question"])
        with st.chat_message("assistant"):
            st.markdown(item["answer"])
