from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Students")

if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.switch_page("Home.py")
    st.stop()


@st.cache_data
def load_data():
    data_path = Path(__file__).resolve().parents[2] / "DATA" / "students.csv"
    return pd.read_csv(data_path)


students = load_data()
st.sidebar.header("Filters")
city = st.sidebar.selectbox("City", ["All"] + sorted(students["City"].dropna().unique()))
lowest, highest = int(students["Grade"].min()), int(students["Grade"].max())
minimum_grade = st.sidebar.slider("Minimum grade", lowest, highest, lowest)
filtered = students[students["Grade"] >= minimum_grade]
if city != "All":
    filtered = filtered[filtered["City"] == city]

st.title("Student Data")
col1, col2, col3 = st.columns(3)
col1.metric("Students", len(filtered))
col2.metric("Average grade", f"{filtered['Grade'].mean():.1f}" if len(filtered) else "N/A")
col3.metric("Average attendance", f"{filtered['Attendance'].mean():.1f}" if len(filtered) else "N/A")

tab_table, tab_charts = st.tabs(["Table", "Charts"])
with tab_table:
    st.dataframe(filtered)
with tab_charts:
    if len(filtered):
        st.bar_chart(filtered.groupby("Course")["Grade"].mean())
    else:
        st.info("No students match the filters.")