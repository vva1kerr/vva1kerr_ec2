import streamlit as st

def check_login():
    """Check if user is logged in, if not redirect to login page."""
    if 'logged_in' not in st.session_state or not st.session_state.logged_in:
        st.switch_page("pages/login.py")
        return False
    return True 