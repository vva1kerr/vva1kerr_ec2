import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

@st.cache_data
def get_pdf(file_id):
    viewer_url = f"{os.getenv(file_id)}"
    st.markdown(f'<iframe src="{viewer_url}" width="100%" height="600px"></iframe>', unsafe_allow_html=True)