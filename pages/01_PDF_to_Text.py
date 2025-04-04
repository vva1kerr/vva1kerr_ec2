import streamlit as st
import pyocr
import pyocr.builders
from PIL import Image
import io
from pdf2image import convert_from_bytes
# import tempfile
import PyPDF2
# import time
# import pytesseract
from src.auth.auth_utils import check_login
if not check_login():
    st.stop()
# Set page config
st.set_page_config(
    page_title="OCR Tool",
    page_icon="📝",
    layout="wide"
)

 
    
# Initialize OCR
try:
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        st.error("No OCR tools found. Please install Tesseract-OCR.")
    else:
        tool = tools[0]
        st.success(f"Using OCR tool: {tool.get_name()}")
except Exception as e:
    st.error(f"Error initializing OCR: {str(e)}")

# Title and description
st.title("📝 OCR Tool")
st.markdown("""
This tool uses PyOCR to extract text from images and PDFs. Upload a file and get the extracted text.
""")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=['png', 'jpg', 'jpeg', 'pdf'])

if uploaded_file is not None:
    file_type = uploaded_file.type
    
    if file_type == "application/pdf":
        # Handle PDF files
        try:
            # First, validate the PDF file
            pdf_bytes = uploaded_file.read()
            pdf_valid = True
            
            # Try to read the PDF with PyPDF2 to validate it
            try:
                pdf_file = io.BytesIO(pdf_bytes)
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                if len(pdf_reader.pages) == 0:
                    st.error("The PDF file appears to be empty or corrupted.")
                    pdf_valid = False
            except Exception as pdf_error:
                st.error(f"Error reading PDF file: {str(pdf_error)}")
                pdf_valid = False
            
            if pdf_valid:
                # Reset the file pointer
                pdf_file.seek(0)
                
                # Convert PDF to images
                try:
                    images = convert_from_bytes(pdf_bytes)
                    if not images:
                        st.error("No pages were found in the PDF file.")
                    else:
                        # Create a list of page numbers for selection
                        page_numbers = list(range(1, len(images) + 1))
                        selected_page = st.selectbox(
                            "Select a page to process",
                            page_numbers,
                            format_func=lambda x: f"Page {x}"
                        )
                        
                        # Display the selected page
                        st.image(images[selected_page - 1], caption=f'Page {selected_page}', use_column_width=True)
                        
                        # Add a button to process the selected page
                        if st.button("Extract Text"):
                            progress_bar = st.progress(0)
                            status_text = st.empty()
                            
                            try:
                                # Update progress
                                status_text.text("Preparing image...")
                                progress_bar.progress(20)
                                
                                # Convert image to RGB if necessary
                                image = images[selected_page - 1]
                                if image.mode != 'RGB':
                                    image = image.convert('RGB')
                                
                                # Update progress
                                status_text.text("Processing image with OCR...")
                                progress_bar.progress(50)
                                
                                # Extract text from the image
                                text = tool.image_to_string(
                                    image,
                                    lang='eng',
                                    builder=pyocr.builders.TextBuilder()
                                )
                                
                                # Update progress
                                status_text.text("Finalizing results...")
                                progress_bar.progress(100)
                                
                                # Display the extracted text
                                st.subheader("Extracted Text:")
                                st.text_area("", text, height=200)
                                
                                # Add download button for the extracted text
                                st.download_button(
                                    label="Download Text",
                                    data=text,
                                    file_name=f"extracted_text_page_{selected_page}.txt",
                                    mime="text/plain"
                                )
                                
                            except Exception as e:
                                st.error(f"Error processing page: {str(e)}")
                            finally:
                                progress_bar.empty()
                                status_text.empty()
                        
                        # Add option to process all pages
                        if st.button("Process All Pages"):
                            progress_bar = st.progress(0)
                            status_text = st.empty()
                            all_text = []
                            
                            try:
                                total_pages = len(images)
                                for i, image in enumerate(images, 1):
                                    # Update progress
                                    status_text.text(f"Processing page {i} of {total_pages}...")
                                    progress = int((i / total_pages) * 100)
                                    progress_bar.progress(progress)
                                    
                                    try:
                                        if image.mode != 'RGB':
                                            image = image.convert('RGB')
                                        text = tool.image_to_string(
                                            image,
                                            lang='eng',
                                            builder=pyocr.builders.TextBuilder()
                                        )
                                        all_text.append(f"=== Page {i} ===\n{text}\n")
                                    except Exception as e:
                                        all_text.append(f"=== Page {i} ===\nError processing page: {str(e)}\n")
                                
                                # Update progress
                                status_text.text("Finalizing results...")
                                progress_bar.progress(100)
                                
                                combined_text = "\n".join(all_text)
                                st.subheader("Extracted Text (All Pages):")
                                st.text_area("", combined_text, height=400)
                                
                                # Add download button for all pages
                                st.download_button(
                                    label="Download All Pages Text",
                                    data=combined_text,
                                    file_name="extracted_text_all_pages.txt",
                                    mime="text/plain"
                                )
                            except Exception as e:
                                st.error(f"Error processing pages: {str(e)}")
                            finally:
                                progress_bar.empty()
                                status_text.empty()
                                
                except Exception as convert_error:
                    st.error(f"Error converting PDF to images: {str(convert_error)}")
                    
        except Exception as e:
            st.error(f"Error processing PDF: {str(e)}")
            st.info("Please make sure the PDF file is not corrupted and try again.")
    else:
        # Handle image files (existing code)
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        if st.button("Extract Text"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Update progress
                status_text.text("Preparing image...")
                progress_bar.progress(20)
                
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                
                # Update progress
                status_text.text("Processing image with OCR...")
                progress_bar.progress(50)
                
                text = tool.image_to_string(
                    image,
                    lang='eng',
                    builder=pyocr.builders.TextBuilder()
                )
                
                # Update progress
                status_text.text("Finalizing results...")
                progress_bar.progress(100)
                
                st.subheader("Extracted Text:")
                st.text_area("", text, height=200)
                
                st.download_button(
                    label="Download Text",
                    data=text,
                    file_name="extracted_text.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"Error processing image: {str(e)}")
            finally:
                progress_bar.empty()
                status_text.empty()

# Add footer with instructions
st.markdown("---")
st.markdown("""
### Instructions:
1. Upload an image file (PNG, JPG, JPEG) or PDF
2. For PDFs:
   - Select a specific page to process
   - Click 'Extract Text' to process the selected page
   - Or click 'Process All Pages' to extract text from all pages
3. For images:
   - Click 'Extract Text' to process the image
4. View the extracted text
5. Download the text if needed

Note: For best results, use clear, well-lit images with good contrast.
""") 