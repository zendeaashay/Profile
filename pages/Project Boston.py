import streamlit as st
import geopandas as gpd
import pandas as pd

def load_data():
    neighborhoods = gpd.read_file("Boston_Neighborhoods.shp")
    survey = pd.read_csv("Survey_responses.csv")
    # Clean and process survey data
    survey['How much do you spend on transportation daily?'] = survey['How much do you spend on transportation daily?'].replace('20-Oct', '10 - 20')
    survey['What range does your age lie in?'] = survey['What range does your age lie in?'].replace('20-Oct', '10 - 20')
    
    # Read merged_df.csv
    merged_df = pd.read_csv('merged_df.csv')

    return neighborhoods, survey, merged_df

def app():
    st.title('Boston Neighborhood Analysis')

    st.write("""
    This project explores Boston's neighborhoods, focusing on transportation habits, accommodation costs, and satisfaction levels based on survey responses. We visualize neighborhoods and analyze aggregated survey data to understand the community's dynamics.
    """)

    neighborhoods, survey, merged_df = load_data()

    st.header('Boston Neighborhoods')
    st.map(neighborhoods.explore(column='Name'))

    st.header('Survey Responses Overview')
    st.write(survey.head())

    st.header('Aggregated Survey Responses by Neighborhood')
    st.write(merged_df)

if __name__ == "__main__":
    app()