import streamlit as st
import src.drive.get_pdf as get_pdf
from src.auth.login import verify_user
from src.markdown.md_utils import read_markdown_file
from src.auth.auth_utils import check_login
if not check_login():
    st.stop()
st.set_page_config(layout="wide", page_title="Chemistry")

 

st.markdown("### ENGINEERING_COMPUTATION_WITH_MATLAB_3_ED_PDF_01") 
get_pdf.get_pdf("ENGINEERING_COMPUTATION_WITH_MATLAB_3_ED_PDF_01")

st.markdown(read_markdown_file("markdown/MATLAB.md"))