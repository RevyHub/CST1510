import hmac

import streamlit as st

st.set_page_config(page_title="Login")

USERS = {
    "alice": {"password": "admin123", "role": "admin"},
    "bob": {"password": "user123", "role": "user"},
}

for key, default in {"logged_in": False, "username": None, "role": None}.items():
    st.session_state.setdefault(key, default)

if st.session_state.logged_in:
    st.switch_page("pages/1_Dashboard.py")

st.title("Login")
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Log in")

if submitted:
    user = USERS.get(username)
    if user and hmac.compare_digest(user["password"].encode(), password.encode()):
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.role = user["role"]
        st.switch_page("pages/1_Dashboard.py")
    else:
        st.error("Invalid credentials")