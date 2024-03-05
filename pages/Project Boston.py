import streamlit as st
import geopandas as gpd
import pandas as pd

def load_data():
    neighborhoods = gpd.read_file("Boston_Neighborhoods.shp")
    survey = pd.read_csv("Survey_responses.csv")
    # Clean and process survey data
    survey['How much do you spend on transportation daily?'] = survey['How much do you spend on transportation daily?'].replace('20-Oct', '10 - 20')
    survey['What range does your age lie in?'] = survey['What range does your age lie in?'].replace('20-Oct', '10 - 20')
    
    # Add a 'neighborhood' column and group by it
    survey['neighborhood'] = survey['Which area do you reside in?']
    survey_grouped = survey.groupby('neighborhood').agg({
        'What range does your age lie in?': lambda x: pd.Series.mode(x).max(),
        'What is your gender?': lambda x: pd.Series.mode(x).max(),
        'How much rent do you pay per month? ( in $ )': lambda x: pd.Series.mode(x).max(),
        'How satisfied are you with the current cost of your accommodation? ': 'mean',
        'What mode of transportation do you primarily use to commute to your college? ': lambda x: x.value_counts(normalize=True).idxmax(),
        'How satisfied are you with the public transportation options available in your area': 'mean',
        'How much do you spend on transportation daily?': lambda x: pd.Series.mode(x).max(),
    }).reset_index()
    return neighborhoods, survey_grouped

def app():
    st.title('Boston Neighborhood Analysis')

    st.write("""
    This project explores Boston's neighborhoods, focusing on transportation habits, accommodation costs, and satisfaction levels based on survey responses. We visualize neighborhoods and analyze aggregated survey data to understand the community's dynamics.
    """)

    neighborhoods, survey_grouped = load_data()

    st.header('Boston Neighborhoods')
    st.map(neighborhoods.explore(column='Name'))

    st.header('Aggregated Survey Responses by Neighborhood')
    st.write(survey_grouped)

if __name__ == "__main__":
    app()