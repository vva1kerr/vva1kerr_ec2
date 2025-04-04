import streamlit as st
import src.drive.get_pdf as get_pdf
from src.auth.login import verify_user
from src.markdown.md_utils import read_markdown_file

st.set_page_config(layout="wide", page_title="Chemistry")

# # If already logged in, redirect to home
# if 'logged_in' in st.session_state and st.session_state.logged_in:
#     st.switch_page("main.py")

st.markdown("### AN_INTRODUCTION_TO_MODERN_ASTROPHYSICS_2_ED")
get_pdf.get_pdf("AN_INTRODUCTION_TO_MODERN_ASTROPHYSICS_2_ED")

st.markdown(read_markdown_file("markdown/Astronomy.md"))