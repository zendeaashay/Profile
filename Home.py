import streamlit as st
import pandas as pd
import altair as alt


df = pd.read_csv('amz.csv')

st.set_page_config( page_title='Welcome to my page!', 
                   page_icon="🏂",
                   layout='wide',
                   initial_sidebar_state="expanded")
alt.themes.enable("dark")

st.header('Home Page')
st.write('Welcome to my world of adventures and analytics!')
st.image('image.jpeg', caption='Exploring the Himalayas with my furry friends!')
st.subheader('Aashay Zende')
st.caption('Data Wizard | Adventurer | Photographer | Surfer')
st.write(""" Hey there! I'm Aashay, a data wizard by day and an adventurous spirit by... well, also by day (and sometimes night).
    Currently weaving my magic with numbers and analytics at the prestigious DAmore McKim School of Business,
    Northeastern University, I'm on a quest to make sense of the world, one dataset at a time.
    Born and raised in the bustling city of Mumbai, India, I've always been a bit of a nomad at heart,
    with my compass pointing towards icy mountain peaks and the soothing waves of beaches, [surfing](#).
    I also love [painting](#) and [photography](#)
    """)

from st_on_hover_tabs import on_hover_tabs

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'AI Chat', 'Project Boston', 'Resume', 'Tableau Dashboard'], 
                         iconName=['Home', 'AI Chat', 'Project Boston', 'Resume', 'Tableau Dashboard'], 
                         default_choice=0)

# Conditional rendering based on the selected tab
if tabs =='Home':
    # Include the content for Home tab
    st.write('This is the Home tab content.')

elif tabs == 'AI Chat':
    # Include the content for AI Chat tab
    st.write('This is the AI Chat tab content.')

elif tabs == 'Project Boston':
    # Include the content for Project Boston tab
    st.write('This is the Project Boston tab content.')
    
elif tabs == 'Resume':
    # Include the content for Resume tab
    st.write('This is the Resume tab content.')
    
elif tabs == 'Tableau Dashboard':
    # Include the content for Tableau Dashboard tab
    st.write('This is the Tableau Dashboard tab content.')
    
from streamlit_star_rating import st_star_rating

st.write("Please rate your experience with this page:")
stars = st_star_rating(label = " ", maxValue = 5, defaultValue = 5, key = "rating", dark_theme = True )
