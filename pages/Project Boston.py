import streamlit as st
import geopandas as gpd
import pandas as pd
from shapely import wkt
import folium
from streamlit_folium import folium_static
from branca.colormap import linear

def app():
    st.title('Boston Neighborhood Analysis')
    
    # Description of the Project
    st.header('Project Description')
    st.write('''
        The Boston Neighborhood Analysis project was undertaken as part of the Data Wrangling for Business 
        subject during my MS in Business Analytics. Our team aimed to analyze various aspects of Boston's 
        neighborhoods, such as property values, crime rates, and infrastructure, to understand the factors 
        that contribute to their livability and economic status. 
    ''')

    # Steps Taken in the Project
    st.header('Project Steps')
    st.write('''
        The project involved several key steps:
        - **Data Collection**: We gathered datasets related to property assessments, crime records, 
          transportation, and demographic surveys.
        - **Data Preprocessing and Cleaning**: Our initial step was to clean the datasets, where we handled 
          missing values, standardized categories, and filtered necessary columns. This ensured the quality 
          and consistency of our data for analysis.
        - **Exploratory Data Analysis (EDA)**: We conducted a thorough EDA to uncover trends and patterns 
          within the data, which helped guide our further analysis.
        - **Geospatial Analysis**: Utilizing GeoPandas, we created visualizations to map the neighborhoods 
          and understand the spatial distribution of various factors.
        - **Predictive Modeling**: We employed an ExtraTreesRegressor to predict property values based on 
          features like location, property size, and amenities.
        - **Heatmap Visualization**: The final step was to create interactive heatmaps using folium to 
          visualize complex data such as crime rates and property values, allowing for an intuitive understanding 
          of the neighborhood dynamics.
    ''')

    # Including PDF and presentation
    st.header('Project Materials')
    st.write('''
        Dive deeper into our project through the following materials:
    ''')
    
    # PDF
    st.write('**Project Report**')
    with open("Project Group5 Final Report.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Download Project Report",
                       data=PDFbyte,
                       file_name="Project_Group5_Final_Report.pdf",
                       mime='application/pdf')
    
    # Presentation
    st.write('**Presentation Slides**')
    with open("Presentation Group 5.pptx", "rb") as pptx_file:
        PPTXbyte = pptx_file.read()
    st.download_button(label="Download Presentation",
                       data=PPTXbyte,
                       file_name="Presentation_Group_5.pptx",
                       mime='application/vnd.openxmlformats-officedocument.presentationml.presentation')


def load_data():
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

def app():
    st.title('Boston Neighborhood Analysis')
    neighborhoods, survey, merged_gdf = load_data()
    option = st.selectbox(
        'Choose a value to plot on the map:',
        ('fatalities', 'bike_stations_count', 'robbery', 'drug', 'assault', 'SHOOTING')
    )
    folium_map = create_folium_map(merged_gdf, option)
    folium_static(folium_map)
    st.header('Survey Responses Overview')
    st.write(survey.head())
    st.header('Aggregated Data Overview')
    st.write(merged_gdf.head())

if __name__ == "__main__":
    app()