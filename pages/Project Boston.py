import streamlit as st
import geopandas as gpd
import pandas as pd

def show_neighborhoods_and_survey():
    # Load and plot the Boston Neighborhoods
    neighborhoods = gpd.read_file("Boston_Neighborhoods.shp")
    st.write(neighborhoods.plot(column='Name', legend=True))

    # Load the survey data
    survey = pd.read_csv("Survey_responses.csv")

    # Data cleaning
    survey['How much do you spend on transportation daily?'] = survey['How much do you spend on transportation daily?'].replace('20-Oct', '10 - 20')
    survey['What range does your age lie in?'] = survey['What range does your age lie in?'].replace('20-Oct', '10 - 20')

    # Display the cleaned survey data
    st.write(survey)

# Call the function to display the content on a Streamlit page
show_neighborhoods_and_survey()