import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard")

if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.switch_page("Home.py")
    st.stop()

st.title("Security Dashboard")
st.write(f"Welcome, {st.session_state.username} ({st.session_state.role})")

incidents = pd.DataFrame({
    "severity": ["High", "Critical", "Low", "Medium", "Critical", "High"],
    "category": ["Phishing", "Ransomware", "Policy", "Malware", "Phishing", "DDoS"],
    "status": ["Open", "Open", "Closed", "Investigating", "Closed", "Open"],
})

col1, col2, col3 = st.columns(3)
col1.metric("Total incidents", len(incidents))
col2.metric("Open", int((incidents["status"] == "Open").sum()))
col3.metric("Critical", int((incidents["severity"] == "Critical").sum()))
st.bar_chart(incidents["category"].value_counts())
st.dataframe(incidents)

with st.sidebar:
    if st.button("Logout"):
        st.session_state.clear()
        st.switch_page("Home.py")