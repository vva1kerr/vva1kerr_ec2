import streamlit as st
import src.drive.get_pdf as get_pdf
from src.auth.login import verify_user
from src.markdown.md_utils import read_markdown_file

st.set_page_config(layout="wide", page_title="Chemistry")

# If already logged in, redirect to home
if 'logged_in' in st.session_state and st.session_state.logged_in:
    st.switch_page("main.py")

st.markdown("### FOUR_DIMENSIONAL_STOCK_MARKET_STRUCTURES_AND_CYCLES_BY_BRADLEY_COWAN")
get_pdf.get_pdf("FOUR_DIMENSIONAL_STOCK_MARKET_STRUCTURES_AND_CYCLES_BY_BRADLEY_COWAN")

st.markdown(read_markdown_file("markdown/Bradley_Cowan.md"))