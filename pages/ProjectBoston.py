#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install geopandas


# In[2]:


# pip install pyproj


# In[3]:


# pip install rtree


# In[4]:


# pip install statsmodels


# In[5]:


# pip install libomp


# In[6]:


# pip install tabulate


# In[7]:


# pip install fpdf


# In[8]:


# pip install streamlit


# In[9]:


# pip install matplotlib


# In[10]:


# pip install scikit-learn


# In[11]:


# pip install ipywidgets


# In[12]:


# pip install pandas_summary


# In[13]:


# pip install sweetviz


# In[14]:


import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from lazypredict.Supervised import LazyRegressor
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import ExtraTreesRegressor


# # This code uses GeoPandas to read a shapefile containing Boston neighborhood boundaries and creates a plot where each neighborhood is colored based on its name. This visualization helps in understanding the geographical distribution of neighborhoods in Boston, facilitating property grouping based on their location in whichever neighborhood.

# In[15]:


neighborhoods = gpd.read_file("Boston_Neighborhoods.shp")
neighborhoods.plot(column='Name', cmap=None, legend=True)


# In[16]:


survey = pd.read_csv("Survey_responses.csv")
# Cleaning the data after observing it manually
survey['How much do you spend on transportation daily?'] = survey['How much do you spend on transportation daily?'].replace('20-Oct', '10 - 20')
survey['What range does your age lie in?'] = survey['What range does your age lie in?'].replace('20-Oct', '10 - 20')
survey.info()


# In[17]:


survey


# In[18]:


# copy of the original DataFrame for modification
survey_df = survey.copy()

# Added a 'neighborhood' column based on the 'Which area do you reside in?' column
survey_df['neighborhood'] = survey_df['Which area do you reside in?']


# Grouped by neighborhood and performing required aggregations
survey_grouped = survey_df.groupby('neighborhood').agg(
    Avg_Age_Range=('What range does your age lie in?', lambda x: pd.Series.mode(x).max()),
    Highest_Gender_Dem=('What is your gender?', lambda x: pd.Series.mode(x).max()),
    Rent=('How much rent do you pay per month? ( in $ )', lambda x: pd.Series.mode(x).max()),
    Accomodation_Cost_Satisfaction=('How satisfied are you with the current cost of your accommodation? ', 'mean'),
    Mode_of_Transportation=('What mode of transportation do you primarily use to commute to your college? ', lambda x: x.value_counts(normalize=True).idxmax()),
    Public_Transportation_Options_Satisfaction=('How satisfied are you with the public transportation options available in your area', 'mean'),
    Transportation_Cost=('How much do you spend on transportation daily?', lambda x: pd.Series.mode(x).max())
).reset_index()


survey_grouped


# In[19]:


age_range_mapping = {'20-30': 25, '30-40': 35, '10 - 20': 18}
survey_grouped['Avg_Age_Range'] = survey_grouped['Avg_Age_Range'].map(age_range_mapping).fillna(survey_grouped['Avg_Age_Range'])


# Converting 'Rent' to numeric values
rent_mapping = {'1000 - 2000': 1500, '2000 - 4000': 3000, '4000 - 8000': 6000, '> 8000': 8000}
survey_grouped['Rent'] = survey_grouped['Rent'].map(rent_mapping)

# Converting 'Transportation_Cost' to numeric values
transportation_cost_mapping = {'0 - 10': 5, '10 - 20': 15, '20 - 30': 25}
survey_grouped['Transportation_Cost'] = survey_grouped['Transportation_Cost'].map(transportation_cost_mapping)

survey_grouped


# # 'prop23' datset provides a comprehensive and detailed overview of individual parcels in Boston. The information on property values, land use, building characteristics, and ownership details enables analysts to study trends in property assessments, identify patterns in land use, and assess the impact of factors like the year built and remodeling on property values. Additionally, details about heating systems, amenities, and parking spaces contribute valuable insights into the residential features of the properties, facilitating a thorough analysis of Boston's real estate landscape and aiding in informed decision-making for various stakeholders, including policymakers, researchers, and real estate professionals.

# In[20]:


prop23 = pd.read_csv("fy2023-property-assessment-data.csv")
display(prop23.shape)
prop23


# In[21]:


prop23_missing_values = prop23.isna().sum()

prop23_total_count = prop23.shape[0]

# Calculated the percentage of missing values for each column in 'prop23'
prop23_percentage_missing = (prop23_missing_values / prop23_total_count) * 100


prop23_missing_info = pd.DataFrame({
    'Column': prop23.columns,
    'Missing Values': prop23_missing_values,
    'Total Count': prop23_total_count,
    'Percentage Missing': prop23_percentage_missing
})

prop23_missing_info


# In[22]:


threshold = 20

prop23_missing_values = prop23.isna().sum()

prop23_total_count = prop23.shape[0]

# Calculated the percentage of missing values for each column in 'prop23'
prop23_percentage_missing = (prop23_missing_values / prop23_total_count) * 100

# Identified columns with more than 30% missing values
columns_to_drop = prop23_percentage_missing[prop23_percentage_missing > threshold].index

prop23 = prop23.drop(columns=columns_to_drop)

prop23


# In[23]:


prop23_missing_values = prop23.isna().sum()

prop23_total_count = prop23.shape[0]

prop23_percentage_missing = (prop23_missing_values / prop23_total_count) * 100

prop23_missing_info = pd.DataFrame({
    'Column': prop23.columns,
    'Missing Values': prop23_missing_values,
    'Total Count': prop23_total_count,
    'Percentage Missing': prop23_percentage_missing
})

prop23_missing_info


# # The dataset 'padl' contains detailed information about properties in the City of Boston from 2001 to 2021. It includes data such as PID, street details, zip codes, assessed values, land use types, and geographical coordinates (lat and long). The dataset is structured with identifying characteristics, property and building characteristics, and geographical information. The variables cover aspects like property ownership, valuation changes over time, and geographical details.

# In[24]:


padl = pd.read_csv("PAD.Long.2021.csv")
display(padl.shape)
padl.info()
columns_to_drop = ['ST_NUM', 'FY2001.LU', 'FY2001.RESEX', 'LU2001FourCat', 'FY2002.LU', 'FY2002.RESEX', 'LU2002FourCat', 'FY2003.LU', 'FY2003.RESEX', 'LU2003FourCat', 'FY2004.LU', 'FY2004.RESEX', 'LU2004FourCat', 'FY2005.LU', 'FY2005.RESEX', 'LU2005FourCat', 'FY2006.LU', 'FY2006.RESEX', 'LU2006FourCat', 'FY2007.LU', 'FY2007.RESEX', 'LU2007FourCat', 'FY2008.LU', 'FY2008.RESEX', 'LU2008FourCat', 'FY2009.LU', 'FY2009.RESEX', 'LU2009FourCat', 'FY2010.LU', 'FY2010.RESEX', 'LU2010FourCat', 'FY2011.LU', 'FY2011.RESEX', 'LU2011FourCat', 'FY2012.LU', 'FY2012.RESEX', 'LU2012FourCat', 'FY2013.LU', 'FY2013.RESEX', 'LU2013FourCat', 'FY2014.LU', 'FY2014.RESEX', 'LU2014FourCat', 'FY2015.LU', 'FY2015.RESEX', 'LU2015FourCat', 'FY2016.LU', 'FY2016.RESEX', 'LU2016FourCat', 'FY2017.LU', 'FY2017.RESEX', 'LU2017FourCat', 'FY2018.LU', 'FY2018.RESEX', 'LU2018FourCat', 'FY2019.LU', 'FY2019.RESEX', 'LU2019FourCat', 'FY2020.LU', 'FY2020.RESEX', 'LU2020FourCat', 'FY2021.LU', 'FY2021.RESEX', 'LU2021FourCat']
padl = padl.drop(columns=columns_to_drop)
padl


# In[25]:


missing_values = padl.isna().sum()

inverted_missing_values = missing_values.to_frame().T
inverted_missing_values.reset_index(drop=True, inplace=True)

counts = padl.count()
transposed_counts = counts.to_frame().T

percentage_missing_values = (inverted_missing_values.iloc[0] / transposed_counts.iloc[0]) * 100

# percentage of missing values
inverted_missing_values.loc[1] = percentage_missing_values
inverted_missing_values


# In[26]:


threshold = 40

padl_missing_values = padl.isna().sum()

padl_total_count = padl.shape[0]

# Calculated the percentage of missing values for each column in 'padl'
padl_percentage_missing = (padl_missing_values / padl_total_count) * 100

padl_missing_info = pd.DataFrame({
    'Column': padl.columns,
    'Missing Values': padl_missing_values,
    'Total Count': padl_total_count,
    'Percentage Missing': padl_percentage_missing
})

columns_to_drop_padl = padl_percentage_missing[padl_percentage_missing > threshold].index

# Drop columns with more than 30% missing values from 'padl'
padl = padl.drop(columns=columns_to_drop_padl)

padl


# In[27]:


missing_values = padl.isna().sum()

inverted_missing_values = missing_values.to_frame().T
inverted_missing_values.reset_index(drop=True, inplace=True)

counts = padl.count()
transposed_counts = counts.to_frame().T

percentage_missing_values = (inverted_missing_values.iloc[0] / transposed_counts.iloc[0]) * 100

# percentage of missing values
inverted_missing_values.loc[1] = percentage_missing_values
inverted_missing_values


# In[28]:


# https://data.boston.gov/dataset/vision-zero-fatality-records
crashrecords = pd.read_csv('Vision Zero Fatality.csv')
crashrecords


# In[29]:


from shapely.geometry import Point

crashrecords = pd.read_csv('Vision Zero Fatality.csv')

# Created a GeoDataFrame with the latitude and longitude information
crashrecords['geometry'] = [Point(xy) for xy in zip(crashrecords['long'], crashrecords['lat'])]
crashrecords_gdf = gpd.GeoDataFrame(crashrecords, geometry='geometry')

crashrecords['neighborhood'] = ""

# Function to determine if a crash record falls within a neighborhood
def assign_neighborhood(row):
    for idx, neighborhood in neighborhoods.iterrows():
        if row['geometry'].within(neighborhood['geometry']):
            return neighborhood['Name']
    return ""


crashrecords['neighborhood'] = crashrecords_gdf.apply(assign_neighborhood, axis=1)


crashrecords.drop('geometry', axis=1, inplace=True)


crashrecords


# In[30]:


bike_stations = pd.read_csv('Blue_Bike_Stations.csv')
bike_stations


# In[31]:


crime = pd.read_csv('crime.csv')
crime.shape


# In[32]:


# Dropped rows where 'Latitude' or 'Longitude' is NaN
crime = crime.dropna(subset=['Lat', 'Long'])

# Converted the 'Latitude' and 'Longitude' columns to a Point geometry
crime['geometry'] = crime.apply(lambda row: Point(row['Long'], row['Lat']), axis=1)

# GeoDataFrame
crime_gdf = gpd.GeoDataFrame(crime, geometry='geometry')


crime['neighborhood'] = ""


# Function to determine if a crime observation falls within a neighborhood
def assign_neighborhood(row):
    for idx, neighborhood in neighborhoods.iterrows():
        if row['geometry'].within(neighborhood['geometry']):
            return neighborhood['Name']
    return ""


crime['neighborhood'] = crime_gdf.apply(assign_neighborhood, axis=1)


crime.drop('geometry', axis=1, inplace=True)


crime


# In[33]:


# Created new columns 'robbery' and 'drug' and initialize them with zeros
crime['robbery'] = 0
crime['drug'] = 0
crime['assault'] = 0
# Identify and mark rows where the offense description indicates robbery or drug offences
crime['robbery'] = crime['OFFENSE_DESCRIPTION'].apply(lambda desc: 1 if desc.startswith('ROBBERY') else 0)
crime['drug'] = crime['OFFENSE_DESCRIPTION'].apply(lambda desc: 1 if desc.startswith('DRUG') else 0)
crime['assault'] = crime['OFFENSE_DESCRIPTION'].apply(lambda desc: 1 if desc.startswith('ASSAULT') else 0)

crime


# # This code is counting how many times each unique property identification number (PID) appears in the dataset. It then filters and identifies PIDs that occur more than once, prints those repeated PIDs along with their counts. This helps to identify any duplicates in the property data.

# In[34]:


pid_counts1 = prop23['PID'].value_counts()

# Filtered values that are repeated more than once
repeated_pids1 = pid_counts1[pid_counts1 > 1]

print("\nTotal number of unique PIDs:", len(pid_counts1))


# In[35]:


prop23 = prop23.drop_duplicates(subset='PID', keep='first')

print("Shape of DataFrame with unique PIDs:", prop23.shape)


# In[36]:


pid_counts2 = padl['PID'].value_counts()

repeated_pids2 = pid_counts2[pid_counts2 > 1]

print("\nTotal number of unique PIDs:", len(pid_counts2))


# In[37]:


padl = padl.drop_duplicates(subset='PID', keep='first')

print("Shape of DataFrame with unique PIDs:", padl.shape)


# # Merging both datasets

# 

# In[38]:


padl = pd.merge(padl, prop23[['PID', 'GIS_ID', 'BLDG_SEQ', 'NUM_BLDGS', 'LUC', 'LU', 'LU_DESC', 'BLDG_TYPE', 'RES_FLOOR', 'LAND_SF', 'GROSS_AREA', 'LIVING_AREA', 'LAND_VALUE', 'BLDG_VALUE', 'TOTAL_VALUE', 'GROSS_TAX', 'YR_BUILT', 'EXT_FNISHED', 'OVERALL_COND', 'FULL_BTH', 'HLF_BTH', 'KITCHENS', 'FIREPLACES']], on='PID', how='left', suffixes=('_left', '_right'))


padl.columns = padl.columns.str.replace('_left', '').str.replace('_right', '')


padl


# In[39]:


padl_missing_values = padl.isna().sum()


padl_total_count = padl.shape[0]


padl_percentage_missing = (padl_missing_values / padl_total_count) * 100


padl_missing_info = pd.DataFrame({
    'Column': padl.columns,
    'Missing Values': padl_missing_values,
    'Total Count': padl_total_count,
    'Percentage Missing': padl_percentage_missing
})

padl_missing_info


# In[40]:


from sklearn.preprocessing import LabelEncoder

padl_cleaned = padl.loc[:, ~padl.columns.duplicated()]
padl_sample = padl_cleaned.sample(frac=0.1, random_state=42)

# Convert categorical variables to numeric using Label Encoding
label_encoder = LabelEncoder()
padl_encoded = padl_sample.apply(lambda x: label_encoder.fit_transform(x) if x.dtype == 'O' else x)

target_column = 'RES_FLOOR'

padl_encoded = padl_encoded.dropna(subset=[target_column])

# Separated data into features (X) and target variable (y)
X = padl_encoded.drop(columns=[target_column, 'PID', 'X', 'Y'])
y = padl_encoded[target_column]

# Splitted data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


reg = LazyRegressor(verbose=0, ignore_warnings=False, custom_metric=None)
models, predictions = reg.fit(X_train, X_test, y_train, y_test)


print(models)
print(predictions)


# In[ ]:





# In[41]:


def impute_missing_values(df, target_column):

    selected_columns = ['X', 'Y', 'ZIPCODE', target_column]


    X_train = df[selected_columns].select_dtypes(include=['number'])
    y_train = df[target_column]
    X_test = df[df[target_column].isnull()]

    if not X_test.empty:
        imputer_X = SimpleImputer(strategy='mean')
        X_train_imputed = imputer_X.fit_transform(X_train)

        imputer_y = SimpleImputer(strategy='mean')
        y_train_imputed = imputer_y.fit_transform(y_train.values.reshape(-1, 1))


        imputer_model = ExtraTreesRegressor(n_estimators=100, random_state=42)
        imputer_model.fit(X_train_imputed, y_train_imputed.ravel())


        X_test_imputed = imputer_X.transform(X_test[selected_columns].select_dtypes(include=['number']))
        imputed_values = imputer_model.predict(X_test_imputed)


        df.loc[X_test.index, target_column] = imputed_values

    else:
        print("X_test has no samples. No imputation performed.")



# In[42]:


impute_missing_values(padl, 'FY2000.AV')


# In[43]:


impute_missing_values(padl, 'FY2021.AV')


# In[44]:


impute_missing_values(padl, 'PercChangeAV2021')


# In[45]:


impute_missing_values(padl, 'GrowthPercChangeAV')


# In[46]:


impute_missing_values(padl, 'CrashPercChangeAV')


# In[47]:


impute_missing_values(padl, 'RecoveryPercChangeAV')


# In[48]:


impute_missing_values(padl, 'RecoveryDiffAV')


# In[49]:


impute_missing_values(padl, 'NUM_BLDGS')


# In[50]:


impute_missing_values(padl, 'LAND_SF')


# In[51]:


impute_missing_values(padl, 'LAND_VALUE')


# In[52]:


impute_missing_values(padl, 'RES_FLOOR')


# In[53]:


impute_missing_values(padl, 'GROSS_AREA')


# In[54]:


impute_missing_values(padl, 'LIVING_AREA')


# In[55]:


impute_missing_values(padl, 'YR_BUILT')


# In[56]:


impute_missing_values(padl, 'BLDG_VALUE')


# In[57]:


impute_missing_values(padl, 'TOTAL_VALUE')


# In[58]:


impute_missing_values(padl, 'GROSS_TAX')


# In[59]:


columns = [
    'FY2000.AV','FY2021.AV', 'PercChangeAV2021', 'GrowthPercChangeAV', 'CrashPercChangeAV',
    'RecoveryPercChangeAV', 'RecoveryDiffAV', 'NUM_BLDGS', 'LAND_SF',
    'LAND_VALUE', 'RES_FLOOR', 'GROSS_AREA', 'LIVING_AREA',
    'YR_BUILT', 'BLDG_VALUE', 'TOTAL_VALUE', 'GROSS_TAX',
]
missing_percentage_additional = padl[columns].isnull().mean() * 100


print("Missing Value Percentages for Additional Columns:")
print(missing_percentage_additional)


# In[ ]:





# In[ ]:





# In[60]:


padl['geometry'] = [Point(xy) for xy in zip(padl['X'], padl['Y'])]
padl_gdf = gpd.GeoDataFrame(padl, geometry='geometry')


padl['neighborhood'] = ""


def assign_neighborhood(row):
    for idx, neighborhood in neighborhoods.iterrows():
        if row['geometry'].within(neighborhood['geometry']):
            return neighborhood['Name']
    return ""


padl['neighborhood'] = padl_gdf.apply(assign_neighborhood, axis=1)


padl.drop('geometry', axis=1, inplace=True)


# In[61]:


columns_to_keep = [
    "PID", "ZIPCODE", "FY2021.AV", "DiffAV2021", "PercChangeAV2021", "RecoveryDiffAV",
    "RecoveryPercChangeAV", 'RES_FLOOR', 'GROSS_AREA', 'LIVING_AREA', 'LAND_VALUE', 
    'BLDG_VALUE', 'TOTAL_VALUE', 'FY2000.AV', 'PercChangeAV2021', 'GrowthPercChangeAV', 
    'CrashPercChangeAV', 'RecoveryPercChangeAV', 'NUM_BLDGS', 'LAND_SF', 'LAND_VALUE', 
    'RES_FLOOR', 'GROSS_AREA', 'LIVING_AREA', 'YR_BUILT', 'BLDG_VALUE', 'TOTAL_VALUE', 
    'GROSS_TAX', 'neighborhood'
]

grouped_df = padl.groupby('neighborhood')[columns_to_keep].agg({
    'PID': ['min', 'max'],
    'ZIPCODE': ['min', 'max'],
    'FY2021.AV': 'mean',
    'DiffAV2021': 'mean',
    'PercChangeAV2021': 'mean',
    'RecoveryDiffAV': 'mean',
    'RecoveryPercChangeAV': 'mean',
    'GROSS_AREA': 'mean',
    'RES_FLOOR': 'mean',
    'LIVING_AREA': 'mean',
    'LAND_VALUE': 'mean',
    'BLDG_VALUE': 'mean',
    'TOTAL_VALUE': 'mean',
    'FY2000.AV': 'mean',  # Include the new columns here
    'PercChangeAV2021': 'mean',
    'GrowthPercChangeAV': 'mean',
    'CrashPercChangeAV': 'mean',
    'RecoveryPercChangeAV': 'mean',
    'NUM_BLDGS': 'mean',
    'LAND_SF': 'mean',
    'LAND_VALUE': 'mean',
    'RES_FLOOR': 'mean',
    'GROSS_AREA': 'mean',
    'LIVING_AREA': 'mean',
    'YR_BUILT': 'mean',
    'BLDG_VALUE': 'mean',
    'TOTAL_VALUE': 'mean',
    'GROSS_TAX': 'mean',
    'neighborhood': 'count' 
}).reset_index()


grouped_df.columns = ['_'.join(col) if col[1] != '' else col[0] for col in grouped_df.columns]


grouped_df.rename(columns={'neighborhood_count': 'Observation_Count'}, inplace=True)


# In[62]:


neighborhoods.rename(columns={'Name': 'neighborhood'}, inplace=True)


# In[63]:


merged_df = pd.merge(grouped_df, neighborhoods[['neighborhood', 'Acres', 'SqMiles', 'geometry']], on='neighborhood', how='left')


merged_df.dropna(subset=['neighborhood'], inplace=True)


merged_df.reset_index(drop=True, inplace=True)
merged_df = merged_df.iloc[1:]

merged_df


# In[64]:


fatalities_count = crashrecords.groupby('neighborhood').size().reset_index(name='fatalities')

merged_df = pd.merge(merged_df, fatalities_count, on='neighborhood', how='left')

merged_df


# In[65]:


geometry = [Point(xy) for xy in zip(bike_stations['Longitude'], bike_stations['Latitude'])]
bike_stations_gdf = gpd.GeoDataFrame(bike_stations, geometry=geometry)

bike_stations['neighborhood'] = ""

def assign_neighborhood(row):
    for idx, neighborhood in neighborhoods.iterrows():
        if row['geometry'].within(neighborhood['geometry']):
            return neighborhood['neighborhood']
    return ""


bike_stations['neighborhood'] = bike_stations_gdf.apply(assign_neighborhood, axis=1)


bike_stations_count = bike_stations.groupby('neighborhood').size().reset_index(name='bike_stations_count')

merged_df = pd.merge(merged_df, bike_stations_count, on='neighborhood', how='left')


merged_df['bike_stations_count'] = merged_df['bike_stations_count'].fillna(0).astype(int)
merged_df


# In[66]:


neighborhood_crime_counts = crime.groupby('neighborhood')[['robbery', 'drug', 'assault', 'SHOOTING']].sum().reset_index()


merged_df = pd.merge(merged_df, neighborhood_crime_counts, how='left', on='neighborhood')

merged_df[['robbery', 'drug', 'assault', 'SHOOTING']] = merged_df[['robbery', 'drug', 'assault', 'SHOOTING']].fillna(0).astype(int)

merged_df


# In[67]:


from shapely import wkt


gdf = gpd.GeoDataFrame(merged_df, geometry='geometry')


gdf.to_file("merged_df.geojson", driver="GeoJSON")


# In[68]:


null_percentages = merged_df.isnull().mean() * 100

null_percentage_summary = pd.DataFrame(null_percentages).transpose()

null_percentage_summary


# In[74]:


print(merged_df.columns)


# In[75]:


from ipywidgets import interact, Dropdown

# Assuming gdf is already defined as a GeoDataFrame
gdf = gpd.GeoDataFrame(merged_df, geometry='geometry')

def plot_geographical_heatmap(gdf, column, title):
    fig, ax = plt.subplots(figsize=(12, 8))
    
    vmin, vmax = gdf[column].min(), gdf[column].max()
    
    gdf.plot(column=column, cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, vmin=vmin, vmax=vmax)

    for x, y, label in zip(gdf.geometry.centroid.x, gdf.geometry.centroid.y, gdf['neighborhood']):
        ax.text(x, y, label, fontsize=6, ha='center', va='center', color='black')

    ax.set_title(f'Boston Neighborhoods: {title}')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt.show()

# Explicitly define column names
columns_to_plot = [
    'SHOOTING', 'fatalities', 'assault', 'robbery', 'drug', 'bike_stations_count', 
    'FY2021.AV_mean', 'DiffAV2021_mean', 'PercChangeAV2021_mean', 'RecoveryDiffAV_mean', 
    'RecoveryPercChangeAV_mean', 'GROSS_AREA_mean', 'RES_FLOOR_mean', 'LIVING_AREA_mean', 
    'LAND_VALUE_mean', 'BLDG_VALUE_mean', 'TOTAL_VALUE_mean', 'FY2000.AV_mean', 
    'GrowthPercChangeAV_mean', 'CrashPercChangeAV_mean', 'NUM_BLDGS_mean', 
    'LAND_SF_mean', 'YR_BUILT_mean', 'GROSS_TAX_mean', 'Observation_Count'
]

# Dropdown widget with explicitly defined column names
column_dropdown = Dropdown(options=columns_to_plot, description='Select Column')

def update_plot(selected_column):
    plot_geographical_heatmap(gdf, selected_column, selected_column.replace("_mean", "").replace("_", " "))

# Interact function to link the dropdown with the plot function
interact(update_plot, selected_column=column_dropdown)

# Display the plot
plt.show()


# In[76]:


from shapely.geometry import Polygon

geometry_column_name = 'geometry'

gdf_merged = gpd.GeoDataFrame(merged_df, geometry=geometry_column_name)

survey_grouped = survey_grouped.merge(gdf_merged[['neighborhood', geometry_column_name]], on='neighborhood', how='left')

survey_grouped = survey_grouped.drop(columns=[geometry_column_name+'_y'], errors='ignore')

survey_grouped = survey_grouped.rename(columns={geometry_column_name+'_x': 'geometry'})

survey_grouped['geometry'] = survey_grouped['geometry'].fillna(Polygon())

print(survey_grouped.head())


# In[77]:


gender_mapping = {'Male': 0, 'Female': 1}
survey_grouped['Highest_Gender_Dem'] = survey_grouped['Highest_Gender_Dem'].map(gender_mapping)
gdf = gpd.GeoDataFrame(survey_grouped, geometry='geometry')

def plot_geographical_heatmap(gdf, column, title):
    fig, ax = plt.subplots(figsize=(12, 8))
    
    vmin, vmax = gdf[column].min(), gdf[column].max()
    
    gdf.boundary.plot(linewidth=1, ax=ax)  # Plot the boundaries of neighborhoods
    gdf.plot(column=column, cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, vmin=vmin, vmax=vmax)

    for x, y, label in zip(gdf.geometry.centroid.x, gdf.geometry.centroid.y, gdf['neighborhood']):
        ax.text(x, y, label, fontsize=6, ha='center', va='center', color='black')

    ax.set_title(f'Boston Neighborhoods: {title}')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt.show()

columns_to_plot = ['Avg_Age_Range', 'Highest_Gender_Dem', 'Rent', 'Accomodation_Cost_Satisfaction', 'Mode_of_Transportation', 'Public_Transportation_Options_Satisfaction', 'Transportation_Cost']

column_dropdown = Dropdown(options=columns_to_plot, description='Select Column')

def update_plot(selected_column):
    plot_geographical_heatmap(gdf, selected_column, selected_column.replace("_mean", "").replace("_", " "))

interact(update_plot, selected_column=column_dropdown)

plt.show()


# In[72]:


import sweetviz as sv


survey_grouped_report = sv.analyze(survey_grouped)

survey_grouped_report.show_html('survey_grouped_report.html')




# In[73]:


from ydata_profiling import ProfileReport

merged_df_profile = ProfileReport(merged_df, title="Merged Data Profiling Report")

merged_df_profile.to_file("merged_df_profiling_report.html")


# In[ ]:




