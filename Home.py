import streamlit as st
import pandas as pd
import altair as alt
from streamlit_star_rating import st_star_rating
pip install st-star-rating

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

from streamlit_text_rating.st_text_rater import st_text_rater

stars = st_star_rating(label = "Please rate you experience", maxValue = 5, defaultValue = 1, key = "rating", dark_theme = True )
