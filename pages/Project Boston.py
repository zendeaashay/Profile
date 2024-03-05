import streamlit as st
import geopandas as gpd
import pandas as pd
from shapely import wkt
import folium

def load_data():
    # Assuming 'Boston_Neighborhoods.shp' and 'Survey_responses.csv' are correct paths
    neighborhoods = gpd.read_file("Boston_Neighborhoods.shp")
    survey = pd.read_csv("Survey_responses.csv")
    merged_df = pd.read_csv('merg_padl.csv')
    # Convert the WKT format in the 'geometry' column to actual geometry
    merged_df['geometry'] = merged_df['geometry'].apply(wkt.loads)
    merged_gdf = gpd.GeoDataFrame(merged_df, geometry='geometry')
    merged_gdf.crs = "EPSG:4326"  # assuming the CRS is WGS84
    return neighborhoods, survey, merged_gdf

def create_folium_map(gdf, value_column):
    # Initialize a Folium map at a central point
    m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)
    # Add neighborhoods as GeoJson
    folium.GeoJson(
        gdf,
        name="geometry",
        style_function=lambda x: {
            'weight': 2,
            'fillOpacity': 0.5
        }
    ).add_to(m)
    return m

def app():
    st.title('Boston Neighborhood Analysis')

    neighborhoods, survey, merged_gdf = load_data()

    # Dropdown to select the value to plot
    option = st.selectbox(
        'Choose a value to plot on the map:',
        ('fatalities', 'bike_stations_count', 'robbery', 'drug', 'assault', 'SHOOTING')
    )

    # Create the map with the selected option
    folium_map = create_folium_map(merged_gdf, option)
    # Streamlit cannot render folium map directly, so we need to use components
    folium_static(folium_map)

    # Optionally, display other data
    st.header('Survey Responses Overview')
    st.write(survey.head())

    st.header('Aggregated Data Overview')
    st.write(merged_gdf.head())

# Add this line to make the folium map render in the Streamlit app
from streamlit_folium import folium_static

if __name__ == "__main__":
    app()