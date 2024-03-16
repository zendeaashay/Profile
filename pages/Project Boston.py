import streamlit as st
import geopandas as gpd
import pandas as pd
from shapely import wkt
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

# Function to format the y-axis as millions
def millions_formatter(x, pos):
    return f'{int(x / 1e6)}M'
# Load your data
data = pd.read_csv('merg_padl.csv')
# Additional functions to create charts for new chapters
def create_living_area_chart(data):
    # Assuming 'LIVING_AREA_mean' is a column in your data
    living_area_data = data[['neighborhood', 'LIVING_AREA_mean']].dropna()
    living_area_data = living_area_data.groupby('neighborhood').mean().sort_values('LIVING_AREA_mean', ascending=False)

    # Creating the bar chart
    fig, ax = plt.subplots(figsize=(10, 8))
    living_area_data['LIVING_AREA_mean'].plot(kind='bar', ax=ax)
    ax.set_title('Average Living Area by Neighborhood')
    ax.set_xlabel('Neighborhood')
    ax.set_ylabel('Average Living Area (sq ft)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    return fig

def create_res_floor_chart(data):
    # Assuming 'RES_FLOOR_mean' is a column in your data
    res_floor_data = data[['neighborhood', 'RES_FLOOR_mean']].dropna()
    res_floor_data = res_floor_data.groupby('neighborhood').mean().sort_values('RES_FLOOR_mean', ascending=False)

    # Creating the bar chart
    fig, ax = plt.subplots(figsize=(10, 8))
    res_floor_data['RES_FLOOR_mean'].plot(kind='bar', ax=ax)
    ax.set_title('Average Residential Floors by Neighborhood')
    ax.set_xlabel('Neighborhood')
    ax.set_ylabel('Average Residential Floors')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    return fig

def create_property_value_comparison_chart(data):
    # Prepare the data
    comparison_data = data[['neighborhood', 'FY2000.AV_mean', 'FY2021.AV_mean']].dropna()
    neighborhoods = comparison_data['neighborhood']
    values_2000 = comparison_data['FY2000.AV_mean']
    values_2021 = comparison_data['FY2021.AV_mean']

    # Calculate the number of neighborhoods and create a range for them
    n = len(neighborhoods)
    index = np.arange(n)

    # Define the width of the bars
    bar_width = 0.35

    # Start plotting
    fig, ax = plt.subplots(figsize=(15, 10))

    # Create bars for 2000 and 2021
    bars_2000 = ax.bar(index, values_2000, bar_width, label='2000', color='b')
    bars_2021 = ax.bar(index + bar_width, values_2021, bar_width, label='2021', color='r')

    # Add labels and title
    ax.set_xlabel('Neighborhood')
    ax.set_ylabel('Property Value')
    ax.set_title('Property Value Comparison 2000 vs 2021 by Neighborhood')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(neighborhoods, rotation=90)
    ax.legend()

    # Format the y-axis as millions
    ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))

    # Show the figure with a tight layout
    plt.tight_layout()

    return fig

# Calculate crime rates by neighborhood
# Assuming 'robbery', 'drug', 'assault', and 'SHOOTING' are your columns for crimes, you can create a new column for total crimes
data['total_crimes'] = data[['robbery', 'drug', 'assault', 'SHOOTING']].sum(axis=1)

# Filter the data to include only the total crimes and neighborhood name
crime_data = data[['neighborhood', 'total_crimes']]

# Sort the DataFrame based on the total crimes
sorted_crime_data = crime_data.sort_values('total_crimes', ascending=False)

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))

# Color for highlighting Dorchester and Charlestown
colors = ['#1f77b4' if (x not in ['Dorchester', 'Roxbury']) else '#ff7f0e' for x in sorted_crime_data['neighborhood']]

# Create a bar chart
ax.bar(sorted_crime_data['neighborhood'], sorted_crime_data['total_crimes'], color=colors)

# Highlight Dorchester and Charlestown by adding a label
for i, neighborhood in enumerate(sorted_crime_data['neighborhood']):
    if neighborhood in ['Dorchester', 'Roxbury']:
        ax.text(i, sorted_crime_data['total_crimes'].iloc[i], neighborhood, ha='center', va='bottom')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Set titles and labels
ax.set_title('Total Crime Rates by Neighborhood')
ax.set_xlabel('Neighborhood')
ax.set_ylabel('Total Crimes')
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
def create_valuation_comparison_chart(merged_gdf):
    # Assuming 'neighborhood' and 'TOTAL_VALUE_mean' are columns in your GeoDataFrame
    # You can change 'TOTAL_VALUE_mean' to the actual valuation column you have
    valuation_data = merged_gdf[['neighborhood', 'TOTAL_VALUE_mean']].dropna()
    valuation_data = valuation_data.groupby('neighborhood').mean().sort_values('TOTAL_VALUE_mean', ascending=False)

    # Creating the bar chart
    fig, ax = plt.subplots(figsize=(10, 8))
    valuation_data['TOTAL_VALUE_mean'].plot(kind='bar', ax=ax)
    ax.set_title('Average Property Valuation by Neighborhood')
    ax.set_xlabel('Neighborhood')
    ax.set_ylabel('Average Valuation')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    
    return fig
# Main app function
def app():
    
    # Introduction: The Fabric of Boston
    st.title("Boston Neighborhood Analysis")
    st.markdown("""
    Embarking on a journey to unravel the evolving tapestry of Boston's neighborhoods, 
    this narrative unfolds an intricate story of property dynamics, safety, and community resilience, 
    reflecting the collective aspirations and challenges of its inhabitants.
    """)
    # Chapter 1: The Evolution of Property Valuations
    st.header("Chapter 1: The Evolution of Property Valuations")
    st.markdown("""
Our journey begins with an analysis of property valuations across Boston's neighborhoods. 
Using property assessment data, we've traced the ebb and flow of the real estate market, 
revealing how historical events, economic shifts, and urban policies have sculpted the city's landscape.
    """)
    # Display graph for Chapter 1
    neighborhoods, survey, merged_gdf = load_data()  # Ensure this line is uncommented to load your data
    chart = create_valuation_comparison_chart(merged_gdf)
    st.pyplot(chart)

# Insight 1: The Ripple Effect of Urban Development
    st.subheader("Insight 1: The Ripple Effect of Urban Development")
    st.markdown("""
In neighborhoods like the Seaport District, we observed a dramatic increase in property values, 
coinciding with major development projects. This trend highlights the transformative impact 
of urban development on local real estate markets.""")
# Display map or chart for Insight 1
# Example placeholder for a map or a chart
    

# Insight 2: The Resilience of Historic Districts
    st.subheader("Insight 2: The Resilience of Historic Districts")
    st.markdown("""
Contrastingly, historic areas such as Beacon Hill and Back Bay have shown remarkable stability in 
property valuations, underscoring the enduring appeal of historical charm in a modern city.
""")
# Display map or chart for Insight 2
# Example placeholder for a map or a chart
    

# Chapter 2: Navigating Through Crime Statistics
    st.header("Chapter 2: Navigating Through Crime Statistics")
    st.markdown("""
Our narrative takes a darker turn as we navigate through the crime statistics, seeking to 
understand the challenges Boston faces in ensuring the safety and well-being of its residents.
""")

# Insight 3: The Tale of Two Cities
    st.subheader("Insight 3: The Tale of Two Cities")
    st.markdown("""
The juxtaposition of crime rates in Dorchester against those in Roxbury presents a tale of 
two cities within Boston, where socioeconomic disparities are starkly reflected in crime statistics.
""")
    st.pyplot(fig)

# Display map or chart for Insight 3
# Example placeholder for a map or a chart


# Insight 4: The Beacon of Hope
    st.subheader("Insight 4: The Beacon of Hope")
    st.markdown("""
However, it's not all grim. Initiatives like the Boston Police Department's community policing 
have shown promising results in areas like Roxbury, where engagement and trust-building efforts 
have led to a noticeable decrease in crime rates across the past couple of years.
""")
# Display map or chart for Insight 4
# Example placeholder for a map or a chart


    # Chapter for Living Area Statistics
    st.header("Chapter 3: Living Area Statistics")
    st.markdown("""
    Here we explore the living areas of all properties within Boston's neighborhoods, highlighting the spatial dynamics of urban housing.
    """)
    # Display Living Area Chart
    living_area_chart = create_living_area_chart(data)
    st.pyplot(living_area_chart)

    # Chapter for Residential Floors
    st.header("Chapter 4: Residential Floors")
    st.markdown("""
    We delve into the vertical expansion of Boston's neighborhoods, examining the average number of residential floors.
    """)
    # Display Residential Floors Chart
    res_floor_chart = create_res_floor_chart(data)
    st.pyplot(res_floor_chart)

    # Chapter for Property Value Changes
    st.header("Chapter 5: Property Value Changes")
    st.markdown("""
    Reflecting on two decades of economic activity, we visualize the changes in property values from the year 2000 to 2021.
    """)
    # Display Property Value Change Chart
    property_value_comparison_chart = create_property_value_comparison_chart(data)
    st.pyplot(property_value_comparison_chart)

# Conclusion: The Mosaic of Boston's Future
    st.header("Conclusion: The Mosaic of Boston's Future")
    st.markdown("""
As our journey through Boston's neighborhoods concludes, we're left with a mosaic of insights 
that together depict a city in flux. Boston is a tapestry of history, culture, challenges, and aspirations. 
The data tells a story of a city that honors its past while boldly facing the future, striving for a balance 
between growth, safety, and sustainability.
""")

# Additional Interactive Elements
# You can include interactive elements such as sliders, buttons, or user input fields to engage users further

# Final Note
    st.markdown("""
In the heart of this narrative lies the essence of Boston - resilient, diverse, and ever-evolving. 
Our project not only sheds light on the complexities of urban living but also celebrates the spirit 
of a city that refuses to stand still.
""")
    # Functionality for selecting data to be displayed on the map
    neighborhoods, survey, merged_gdf = load_data()
    option = st.selectbox(
       'Choose a value to plot on the map:',
       ('FY2021.AV_mean', 'DiffAV2021_mean', 'PercChangeAV2021_mean', 'RecoveryDiffAV_mean', 'RecoveryPercChangeAV_mean', 'GROSS_AREA_mean', 'RES_FLOOR_mean', 'LIVING_AREA_mean', 'LAND_VALUE_mean', 'BLDG_VALUE_mean', 'TOTAL_VALUE_mean', 'FY2000.AV_mean', 'GrowthPercChangeAV_mean', 'CrashPercChangeAV_mean', 'NUM_BLDGS_mean', 'LAND_SF_mean', 'YR_BUILT_mean', 'GROSS_TAX_mean', 'Observation_Count', 'fatalities', 'bike_stations_count', 'robbery', 'drug', 'assault', 'SHOOTING')
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
