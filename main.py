import streamlit as st
from components.sidebar import show_sidebar
from src.markdown.md_utils import read_markdown_file
from src.auth.auth_utils import check_login

st.set_page_config(layout="wide", page_title="vva1kerr")

# Check if user is logged in
if not check_login():
    st.stop()

# Main content (only shown to logged-in users)
show_sidebar()

# Show logout button
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# Your main content here
st.markdown(read_markdown_file("markdown/testing.md"))
