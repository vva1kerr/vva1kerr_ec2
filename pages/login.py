import streamlit as st
from src.auth.login import verify_user

st.set_page_config(layout="wide", page_title="Login")

# If already logged in, redirect to home
if 'logged_in' in st.session_state and st.session_state.logged_in:
    st.switch_page("main.py")

st.title("Login")
    
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button("Login")
    
    if submit_button:
        success, error = verify_user(username, password, "tutorial")
        if success:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error(error) 