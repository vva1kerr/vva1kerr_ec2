import streamlit as st
from src.auth.auth_utils import check_login

def show_sidebar():
    # st.sidebar.title("Navigation")

    # Check if user is logged in
    if not check_login():
        st.stop()

    # Add version info and credits
    # st.sidebar.markdown("---")
    st.sidebar.markdown("v1.0.0")
    st.sidebar.markdown("Created by Space Cowboy") 