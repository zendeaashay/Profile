import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

def show_pdf():
    st.title('My Consulting Analysis and Insigths on the Indian E-Tailing Market')

    pdf_viewer("eComm India.pdf", width=850, height=1000)


# Execute the function to display the resume
show_pdf()