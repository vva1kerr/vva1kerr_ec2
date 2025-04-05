import streamlit as st
import src.drive.get_pdf as get_pdf
from src.auth.login import verify_user
from src.markdown.md_utils import read_markdown_file
from src.auth.auth_utils import check_login
if not check_login():
    st.stop()
st.set_page_config(layout="wide", page_title="Chemistry")

 

st.markdown("### CHEMISTRY_THE_MOLECULAR_NATURE_OF_MATTER_AND_CHANGE_9_ED_PDF_02") 
get_pdf.get_pdf("CHEMISTRY_THE_MOLECULAR_NATURE_OF_MATTER_AND_CHANGE_9_ED_PDF_02")

st.markdown("### PREPARING_FOR_YOUR_ACS_EXAMINATION_IN_GENERAL_CHEMISTRY_2_ED") 
get_pdf.get_pdf("PREPARING_FOR_YOUR_ACS_EXAMINATION_IN_GENERAL_CHEMISTRY_2_ED")

st.markdown(read_markdown_file("markdown/Chemistry.md"))