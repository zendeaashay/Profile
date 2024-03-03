import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv('amz.csv')

st.set_page_config( page_title='Welcome to my page!', 
                   page_icon="🏂",
                   layout='wide',
                   initial_sidebar_state="expanded")
alt.themes.enable("dark")




# Sidebar
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a page:',
                           ['Home', 'Resume', 'Photography', 'Surfing', 'Power BI Visualizations', 'ML Predictions', 'About'])

if options == 'Home':
    st.header('Home Page')
    st.write('Welcome to my world of adventures and analytics!')
    st.image('image.jpeg', caption='Exploring the Himalayas with my furry friends!')
    st.subheader('Aashay Zende')
    st.caption('Data Wizard | Adventurer | Photographer | Surfer')

    # Introduction text
    st.write(""" Hey there! I'm Aashay, a data wizard by day and an adventurous spirit by... well, also by day (and sometimes night).
    Currently weaving my magic with numbers and analytics at the prestigious DAmore McKim School of Business,
    Northeastern University, I'm on a quest to make sense of the world, one dataset at a time.
    Born and raised in the bustling city of Mumbai, India, I've always been a bit of a nomad at heart,
    with my compass pointing towards icy mountain peaks and the soothing waves of beaches, [surfing](#).
    I also love [painting](#) and [photography](#)
    """)



def photography_page():
    st.header('Photography')
    st.write("Here's my photography portfolio...")

def surfing_page():
    st.header('Surfing')
    st.write("Here's my surfing adventures...")

def dashboard_page():
    st.header('E-comm Visualizations')
    st.write("Here are my Amazon visualizations...")
    

def ml_predictions_page():
    st.header('ML Predictions')
    st.write("Here are my machine learning predictions...")

def about_page():
    st.header('About Me')
    st.write("Here's some information about me...")

# Page content based on navigation choice
if options == 'Home':
    home_page()
elif options == 'Photography':
    photography_page()
elif options == 'Surfing':
    surfing_page()
elif options == 'Power BI Visualizations':
    power_bi_page()
elif options == 'ML Predictions':
    ml_predictions_page()
elif options == 'About':
    about_page()