import streamlit as st
import altair as alt
from streamlit_star_rating import st_star_rating





st.set_page_config(page_title="Welcome to my Page!", page_icon="🌟", layout="wide")
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
# Enable Altair dark theme for charts
alt.themes.enable("dark")
    
# Custom CSS
with open('homestyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    

def show_resume():
    st.title('My Resume')
    st.write("Here is my resume showcasing my experience and skills.")
    # Display the resume PDF
    pdf_viewer("ResumeWOnumber.pdf", width=800, height=1000)
    # Link to download resume
    resume_link = 'ResumeWOnumber.pdf'
    with open(resume_link, "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="ResumeWOnumber.pdf",
            mime="application/pdf"
        )   



st.title("Aashay Zende")
st.markdown("""
    <div class="bio">
        <h4>Data Analyst | Business Analyst | Datacamp SQL Associate Certified | PowerBI and Tableau Specialist | Portfolio Management | Strategy Consulting </h4>
        <p>I am a passionate Data and Business Analyst, pursuing a Master of Science in Business Analytics at Northeastern University. I am actively seeking opportunities in business or data analytics, where I can leverage my advanced skills in Data Analytics, Python, SQL, R, PowerBI, Tableau, MS Office, Management and more, in strategic consulting, marketing, and supply chain management projects, utilizing my analytical prowess to drive data-informed decision-making and strategic initiatives.
        
My portfolio is a testament to my multifaceted skills, from developing strategic marketing campaigns and investment portfolio optimization to spearheading groundbreaking projects like the transformative PowerBI dashboard that revolutionized data visualization and decision-making processes.

For recruiters looking to harness my blend of analytical rigor, strategic thinking, and dynamic leadership in the realms of business analysis, strategy consulting, marketing, supply chain management, and beyond, feel free to reach out. You can contact me at zende.a@northeastern.edu, or connect with me on LinkedIn.

Let's navigate the data-driven landscapes together and turn complex challenges into strategic opportunities. </p>
        </div>
    """, unsafe_allow_html=True)
st.image('image.jpg', caption='Exploring the Himalayas with my furry friends!')
    
from streamlit_pdf_viewer import pdf_viewer

   

    # Execute the function to display the resume
show_resume()

    
import json
from streamlit_timeline import timeline


def show_timeline():
 st.title("My Professional Timeline")
        
with open('timeline_data.json', "r") as f:
 timeline_data = json.load(f)  
 timeline(timeline_data, height=800)
 show_timeline()


        
from streamlit_star_rating import st_star_rating
# Define a function to toggle the visibility of the star rating
def toggle_rating():
    st.session_state.show_rating = not st.session_state.show_rating

# Initialize the session state variable
if 'show_rating' not in st.session_state:
    st.session_state.show_rating = True

# Add a button to toggle the star rating visibility
st.button('Show/Hide', on_click=toggle_rating)

# Show the star rating if the toggle is set to show it
if st.session_state.show_rating:

    # Create a container for the star rating
  with st.container():
        st.write("Please rate your experience with this page:")
        stars = st_star_rating(label="", maxValue=5, defaultValue=5, key="rating", dark_theme=True)
