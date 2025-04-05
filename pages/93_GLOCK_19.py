import streamlit as st
import src.drive.get_pdf as get_pdf
from src.auth.login import verify_user
from src.markdown.md_utils import read_markdown_file
from src.auth.auth_utils import check_login
import os
import re

if not check_login():
    st.stop()
st.set_page_config(layout="wide", page_title="GENERAL_ART")

st.markdown("### GENERAL ART") 

# Read the markdown content
content = read_markdown_file("markdown/GLOCK_19.md")

# Split content into sections
sections = content.split("#")
for section in sections:
    if section.strip():
        # Split into title and content
        lines = section.strip().split("\n")
        title = lines[0]
        st.markdown(f"# {title}")
        
        # Process images in the section
        for line in lines[1:]:
            if line.strip().startswith("!["):
                try:
                    # Extract image path
                    image_path = line.split("(")[1].split(")")[0]
                    if image_path.startswith("/"):
                        image_path = image_path[1:]  # Remove leading slash
                    if image_path.startswith("assets/"):
                        image_path = image_path[7:]  # Remove "assets/" prefix
                    
                    # Get the base filename and directory
                    base_name = os.path.basename(image_path)
                    dir_name = os.path.dirname(image_path)
                    

                    # # Clean up the filename while preserving important characters
                    # base_name = re.sub(r'[^a-zA-Z0-9_.α-ωΑ-Ω]', '_', base_name)
                    # base_name = re.sub(r'_+', '_', base_name)  # Replace multiple underscores with single
                    
                    # Construct the full path
                    full_path = os.path.join("assets", dir_name, base_name)
                    
                    # Debug information
                    st.write(f"Looking for image at: {full_path}")
                    
                    # Check if file exists
                    if os.path.exists(full_path):
                        st.image(full_path, use_container_width=True)
                    else:
                        st.error(f"Image not found: {full_path}")
                except Exception as e:
                    st.error(f"Error processing image: {str(e)}")
            else:
                st.markdown(line)