import streamlit as st
import geopandas as gpd
import pandas as pd

def load_data():
    neighborhoods = gpd.read_file("Boston_Neighborhoods.shp")
    survey = pd.read_csv("Survey_responses.csv")
    # Cleaning the data after observing it manually
    survey['How much do you spend on transportation daily?'] = survey['How much do you spend on transportation daily?'].replace('20-Oct', '10 - 20')
    survey['What range does your age lie in?'] = survey['What range does your age lie in?'].replace('20-Oct', '10 - 20')

    # Read the merged_df.csv file
    merged_df = pd.read_csv('/mnt/data/merged_df.csv')
    
    return neighborhoods, survey, merged_df

def app():
    st.title('Boston Neighborhood Analysis')

    st.write("""
    This project aims to analyze the geographical distribution and characteristics of Boston's neighborhoods. 
    We start by visualizing the neighborhoods and then delve into a survey that collects data on residents' 
    transportation habits, accommodation costs, and satisfaction levels. Additionally, we explore aggregated data
    from various sources to gain deeper insights into each neighborhood.
    """)

    neighborhoods, survey, merged_df = load_data()

    st.header('Boston Neighborhoods')
    # Visualization code for neighborhoods goes here

    st.header('Survey Responses Overview')
    st.write(survey.head())

    st.header('Aggregated Data Overview')
    st.write(merged_df.head())

if __name__ == "__main__":
    app()