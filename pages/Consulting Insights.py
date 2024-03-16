import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

def show_resume():
    st.title('My Resume')

    # You can add more content here as needed
    st.write("Here is my resume showcasing my experience and skills.")

    # Display the resume PDF
    with open("eComm India.pdf", "rb") as file:
        pdf_viewer(file, width=850, height=1000)

    # Link to download resume
    resume_link = 'eComm India.pdf'  # Make sure this is the correct path to your resume PDF
    with open(resume_link, "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="Aashay Zende - Resume.pdf",
            mime="application/pdf"
        )

# Execute the function to display the resume
show_resume()