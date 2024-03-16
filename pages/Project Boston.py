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
    st.write("""Overview
Project Title: Boston Neighborhood Analysis


Introduction: Our project delves into the evolving landscape of property valuations and characteristics within Boston's diverse neighborhoods. We aimed to uncover the intricate patterns of real estate dynamics, crime statistics, urban planning, and sustainability efforts across the city.


Business Problem: We explored how property valuations and characteristics have transformed over the years in different Boston neighborhoods and examined the distribution of crime, urban planning, and sustainability metrics across these areas.


Importance: Real estate analytics is crucial for informed decision-making in urban planning and sustainability. Our work provides valuable insights for real estate professionals, policymakers, and individuals interested in Boston's housing market.

Target Audience: Real Estate Professionals, Policymakers, Prospective Residents, Businesses, 


Methodology
Data Collection:
Primary Dataset: Survey with 63 rows and 12 columns.
Secondary Datasets: Property assessments, crime incident reports, Vision Zero fatality records, and Blue Bike station locations from various sources including Harvard Dataverse and Analyze Boston.


Data Pre-Processing:
Data Formatting: We standardized the datasets to a common format, ensuring consistency across various data sources.
Data Cleaning: Employed ExtraTreesRegressor for imputing missing values and standardized the data for ease of analysis.


Tools & Techniques:
Python Packages: Pandas for data manipulation, Plotly and Matplotlib for visualization, Geopandas for map building, and ipywidgets for interactive components.
Data Imputation: Used LazyRegressor to identify the best model for imputing missing values and opted for ExtraTreesRegressor due to its efficiency and effectiveness.

Results and Analysis
Data Analysis:
Conducted thorough analysis using feature engineering, regression models for imputation, and created heatmaps for neighborhood-level insights.
Addressed challenges like data sufficiency and accuracy, and merged data from various sources to create comprehensive neighborhood profiles.

Visualizations: Developed interactive visualizations using ipywidgets and created heatmaps using Geopandas and Matplotlib to display property values, crime statistics, and other relevant metrics at the neighborhood level.

Outcomes: Our analysis revealed significant insights into the evolution of property valuations, the geographical distribution of various property characteristics, and the correlation with crime rates and urban infrastructure. These findings can guide strategic urban planning and investment decisions in Boston's real estate market.

Heatmaps of Boston: Below are the heatmaps generated as part of our analysis, showcasing the spatial distribution of key metrics across Boston neighborhoods. These visual representations provide a clear and intuitive understanding of the complex data we've analyzed.

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
