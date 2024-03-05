import streamlit as st
import geopandas as gpd
import pandas as pd
import pydeck as pdk
import pyproj

def load_data():
    neighborhoods = gpd.read_file("Boston_Neighborhoods.shp")
    survey = pd.read_csv("Survey_responses.csv")
    survey['How much do you spend on transportation daily?'] = survey['How much do you spend on transportation daily?'].replace('20-Oct', '10 - 20')
    survey['What range does your age lie in?'] = survey['What range does your age lie in?'].replace('20-Oct', '10 - 20')
    merged_df = pd.read_csv('merged_df.csv')
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
    # Convert GeoDataFrame to pydeck data format
    neighborhoods_pydeck = neighborhoods.to_crs(pyproj.CRS.from_epsg(4326))
    layer = pdk.Layer(
        'GeoJsonLayer',
        data=neighborhoods_pydeck.__geo_interface__,
        opacity=0.8,
        stroked=False,
        filled=True,
        extruded=True,
        wireframe=True
    )
    view_state = pdk.ViewState(latitude=neighborhoods_pydeck.geometry.centroid.y.mean(), longitude=neighborhoods_pydeck.geometry.centroid.x.mean(), zoom=11, bearing=0, pitch=45)
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

    st.header('Survey Responses Overview')
    st.write(survey.head())

    st.header('Aggregated Data Overview')
    st.write(merged_df.head())

if __name__ == "__main__":
    app()