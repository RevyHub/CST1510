## Week 11
# Tasks 3-8 are a multipage Streamlit app in ../streamlit_app/.
# Start it from the CST1510 folder with:
# python -m streamlit run .\ExtraWork\streamlit_app\Home.py
#
# Task 9, Reflection Questions
# 1. Streamlit reruns the script from the top on every interaction, which resets normal variables.
#    st.session_state survives reruns, so login status and chat history persist.
# 2. st.stop() halts the script at that point, so nothing below (the protected content) is shown.
# 3. st.form() groups the inputs and only reruns the app when the submit button is pressed,
#    instead of rerunning on every keystroke or widget change.

