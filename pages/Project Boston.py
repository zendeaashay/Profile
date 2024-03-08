import streamlit as st
import geopandas as gpd
import pandas as pd
from shapely import wkt
import folium
from streamlit_folium import folium_static

# Load your data here
def load_data():
    # Replace these paths with the actual paths of your files
    neighborhoods = gpd.read_file("Boston_Neighborhoods.shp")
    survey = pd.read_csv("Survey_responses.csv")
    merged_df = pd.read_csv('merg_padl.csv')
    merged_df['geometry'] = merged_df['geometry'].apply(wkt.loads)
    merged_gdf = gpd.GeoDataFrame(merged_df, geometry='geometry')
    merged_gdf.crs = "EPSG:4326"
    return neighborhoods, survey, merged_gdf

def create_folium_map(gdf, value_column):
    m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)
    folium.Choropleth(
        geo_data=gdf,
        name='choropleth',
        data=gdf,
        columns=['neighborhood', value_column],
        key_on='feature.properties.neighborhood',
        fill_color='YlOrBr',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=value_column
    ).add_to(m)
    folium.LayerControl().add_to(m)
    return m

# Main app function
def app():
    st.title('Boston Neighborhood Analysis')
    
    # Project description and steps
    st.header('Project Description')
    st.write("""
- Data Collection: We gathered datasets related to property assessments, crime records, 
          transportation, and demographic surveys.
        - Data Preprocessing and Cleaning: We cleaned the datasets for quality and consistency.
        - Exploratory Data Analysis (EDA): To uncover trends and patterns.
        - Geospatial Analysis: Used GeoPandas for visual mapping of neighborhoods.
        - Predictive Modeling: Employed ExtraTreesRegressor for property value predictions.
        - Heatmap Visualization: Used folium for interactive visualization of crime rates and property values.
     """)

    # Functionality for selecting data to be displayed on the map
    neighborhoods, survey, merged_gdf = load_data()
    option = st.selectbox(
       'Choose a value to plot on the map:',
       ('fatalities', 'bike_stations_count', 'robbery', 'drug', 'assault', 'SHOOTING')
    )
    folium_map = create_folium_map(merged_gdf, option)
    folium_static(folium_map)

    # Display other data overview if needed
    st.header('Survey Responses Overview')
    st.write(survey.head())
    st.header('Aggregated Data Overview')
    st.write(merged_gdf.head())

    # Section for downloading the project PDF and PPTX
    st.header('Project Materials')

    # Buttons to download PDF and PPTX
    with open("Project Group5 Final Report.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Project Report",
            data=file,
            file_name="Project_Group5_Final_Report.pdf",
            mime="application/octet-stream"
        )

    with open("Presentation Group 5.pptx", "rb") as file:
        btn = st.download_button(
            label="Download Presentation Slides",
            data=file,
            file_name="Presentation_Group_5.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )

if __name__ == "__main__":
    app()