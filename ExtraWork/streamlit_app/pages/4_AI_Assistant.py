import os

import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Assistant")

if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.switch_page("Home.py")
    st.stop()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Set the OPENAI_API_KEY environment variable to use the AI assistant.")
    st.stop()

prompts = {
    "Cybersecurity": "You are a senior incident response analyst. Be structured and prioritise containment.",
    "Data Science": "You are an experienced data scientist. Prioritise data quality and correct statistics.",
    "IT Operations": "You are an IT operations lead. Prioritise availability and safe, reversible changes.",
}
client = OpenAI(api_key=api_key)
st.session_state.setdefault("ai_messages", [])

with st.sidebar:
    domain = st.selectbox("Domain", list(prompts))
    counter = st.empty()
    if st.button("Clear Chat"):
        st.session_state.ai_messages = []
        st.rerun()

st.title("AI Assistant")
for message in st.session_state.ai_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_text := st.chat_input("Ask a question..."):
    st.session_state.ai_messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)
    with st.chat_message("assistant"):
        placeholder = st.empty()
        reply = ""
        try:
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": prompts[domain]}] + st.session_state.ai_messages,
                stream=True,
            )
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    reply += chunk.choices[0].delta.content
                    placeholder.markdown(reply + "|")
            placeholder.markdown(reply)
            st.session_state.ai_messages.append({"role": "assistant", "content": reply})
        except Exception as error:
            st.session_state.ai_messages.pop()
            placeholder.error(f"API error: {error}")
counter.metric("Messages", len(st.session_state.ai_messages))