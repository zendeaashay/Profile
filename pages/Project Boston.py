import streamlit as st
import geopandas as gpd
import pandas as pd

def load_data():
    neighborhoods = gpd.read_file("Boston_Neighborhoods.shp")
    survey = pd.read_csv("Survey_responses.csv")
    survey['How much do you spend on transportation daily?'] = survey['How much do you spend on transportation daily?'].replace('20-Oct', '10 - 20')
    survey['What range does your age lie in?'] = survey['What range does your age lie in?'].replace('20-Oct', '10 - 20')
    return neighborhoods, survey

def app():
    st.title('Boston Neighborhood Analysis')

    st.write("""
    This project aims to analyze the geographical distribution and characteristics of Boston's neighborhoods. 
    We start by visualizing the neighborhoods and then delve into a survey that collects data on residents' 
    transportation habits, accommodation costs, and satisfaction levels.
    """)

    neighborhoods, survey = load_data()

    st.header('Boston Neighborhoods')
    st.map(neighborhoods)

    st.header('Survey Responses Overview')
    st.write(survey.head())

if __name__ == "__main__":
    app()