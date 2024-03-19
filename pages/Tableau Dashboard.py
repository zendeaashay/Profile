import streamlit as st
import base64

# Function to convert PDF file to base64
def get_base64_of_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Embedding the PDF in an iframe
def show_pdf(file_path):
    base64_pdf = get_base64_of_pdf(file_path)
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

st.title("Amazon Analysis Dashboard")

# Path to your PDF file
pdf_file_path = 'dashb/Amazon.pdf'

show_pdf(pdf_file_path)