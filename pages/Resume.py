import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

def show_resume():
    st.title('My Resume')

    # You can add more content here as needed
    st.write("Here is my resume showcasing my experience and skills.")

    # Display the resume PDF
    pdf_viewer("Aashay Zende - Resume.pdf", width=850, height=1000)

    # Link to download resume
    resume_link = 'Aashay Zende - Resume.pdf'
    with open(resume_link, "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="Aashay Zende - Resume.pdf",
            mime="application/pdf"
        )

# Execute the function to display the resume
show_resume()

import json
import streamlit as st


def show_timeline():
    st.title("My Professional Timeline")
    
    with open('timeline_data.json', "r") as f:
        timeline_data = json.load(f)

    
    timeline(timeline_data, height=800)


show_timeline()