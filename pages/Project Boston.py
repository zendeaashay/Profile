import streamlit as st
import geopandas as gpd
import pandas as pd
import pydeck as pdk
import pyproj
from shapely import wkt

def load_data():
    neighborhoods = gpd.read_file("Boston_Neighborhoods.shp")
    survey = pd.read_csv("Survey_responses.csv")
    merged_df = pd.read_csv('merg_padl.csv')
    # Convert the WKT format in the 'geometry' column to actual geometry
    merged_df['geometry'] = merged_df['geometry'].apply(wkt.loads)
    merged_gdf = gpd.GeoDataFrame(merged_df, geometry='geometry')
    merged_gdf.crs = "EPSG:4326"  # assuming the CRS is WGS84
    return neighborhoods, survey, merged_gdf

def app():
    st.title('Boston Neighborhood Analysis')

    neighborhoods, survey, merged_gdf = load_data()

    # Dropdown to select the value to plot
    option = st.selectbox(
        'Choose a value to plot on the map:',
        ('fatalities', 'bike_stations_count', 'robbery', 'drug', 'assault', 'SHOOTING')
    )

    # Convert GeoDataFrame to pydeck data format
    neighborhoods_pydeck = neighborhoods.to_crs(pyproj.CRS.from_epsg(4326))

    # Define the initial view state
    view_state = pdk.ViewState(
        latitude=neighborhoods_pydeck.geometry.centroid.y.mean(), 
        longitude=neighborhoods_pydeck.geometry.centroid.x.mean(), 
        zoom=11, 
        bearing=0, 
        pitch=45
    )

    # Create a heatmap layer
    heatmap_layer = pdk.Layer(
        "HeatmapLayer",
        data=merged_gdf,
        get_position=["lon", "lat"],
        get_weight=option,
        radius_pixels=50,
    )

    # Render the map
    st.pydeck_chart(pdk.Deck(layers=[heatmap_layer], initial_view_state=view_state))

    # Optionally, display other data
    st.header('Survey Responses Overview')
    st.write(survey.head())

    st.header('Aggregated Data Overview')
    st.write(merged_gdf.head())

if __name__ == "__main__":
    app()