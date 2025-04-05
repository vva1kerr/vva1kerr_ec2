import streamlit as st
import src.drive.get_pdf as get_pdf
from src.auth.login import verify_user
from src.markdown.md_utils import read_markdown_file
from src.auth.auth_utils import check_login
if not check_login():
    st.stop()
st.set_page_config(layout="wide", page_title="Chemistry")

 
st.markdown("### 1910_SPECULATION_AS_A_PROFITABLE_PROFESSION_W_D_Gann_PDF_06")
get_pdf.get_pdf("1910_SPECULATION_AS_A_PROFITABLE_PROFESSION_W_D_Gann_PDF_06")
st.markdown("### 1923_TRUTH_OF_THE_STOCK_TAPE_W_D_Gann_PDF_07")
get_pdf.get_pdf("1923_TRUTH_OF_THE_STOCK_TAPE_W_D_Gann_PDF_07")
st.markdown("### 1927_THE_TUNNEL_THRU_THE_AIR_W_D_Gann_PDF_08")
get_pdf.get_pdf("1927_THE_TUNNEL_THRU_THE_AIR_W_D_Gann_PDF_08")
st.markdown("### 1930_WALL_STREET_STOCK_SELECTOR_W_D_Gann_PDF_09")
get_pdf.get_pdf("1930_WALL_STREET_STOCK_SELECTOR_W_D_Gann_PDF_09")
st.markdown("### 1936_NEW_STOCK_TREND_DETECTOR_W_D_Gann_PDF_10")
get_pdf.get_pdf("1936_NEW_STOCK_TREND_DETECTOR_W_D_Gann_PDF_10")
st.markdown("### 1940_FACE_FACTS_USA_W_D_Gann_PDF_11")
get_pdf.get_pdf("1940_FACE_FACTS_USA_W_D_Gann_PDF_11")
st.markdown("### 1941_HOW_TO_MAKE_PROFITS_TRADING_IN_COMMODITIES_W_D_Gann_PDF_12")
get_pdf.get_pdf("1941_HOW_TO_MAKE_PROFITS_TRADING_IN_PUTS_AND_CALLS_W_D_Gann_PDF_13")
st.markdown("### 1949_45_YEARS_IN_WALL_STREET_W_D_Gann_PDF_14")
get_pdf.get_pdf("1949_45_YEARS_IN_WALL_STREET_W_D_Gann_PDF_14")
st.markdown("### 1950_THE_MAGIC_WORD_W_D_Gann_PDF_15")
get_pdf.get_pdf("1950_THE_MAGIC_WORD_W_D_Gann_PDF_15")
st.markdown("### 1954_SCIENTIFIC_STOCK_FORECASTING_W_D_Gann_PDF_16")
get_pdf.get_pdf("1954_SCIENTIFIC_STOCK_FORECASTING_W_D_Gann_PDF_16")


st.markdown(read_markdown_file("markdown/GANN.md"))