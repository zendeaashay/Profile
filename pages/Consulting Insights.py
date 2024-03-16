import streamlit as st
import PyPDF2
import base64

# Function to read PDF file and convert to base64
def get_base64_of_pdf_data(pdf_file_path):
    with open(pdf_file_path, "rb") as f:
        pdf_data = f.read()
    return base64.b64encode(pdf_data).decode('utf-8')

# Embeds the PDF file in the Streamlit app
def st_display_pdf(pdf_file_path):
    pdf_base64 = get_base64_of_pdf_data(pdf_file_path)
    pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Display the PDF
st_display_pdf("eComm India.pdf")