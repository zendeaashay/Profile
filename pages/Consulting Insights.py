import streamlit as st
from streamlit_pdf_viewer import st_pdf_viewer

# Assuming your Streamlit app has multiple pages, use an if statement or a function to control page display
def show_pdf_viewer_page():
    # Load the PDF file into the app
    with open("eComm India.pdf", "rb") as pdf_file:
        st_pdf_viewer(pdf_file)

# Call the function to display the PDF viewer page
show_pdf_viewer_page()