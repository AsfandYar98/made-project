import os
import pandas as pd
import sqlite3

# Define the paths to the Excel file
climate_csv = '/Users/asfand/Downloads/who_aap_2021_v9_11august2022.xlsx'
disaster_csv = '/Users/asfand/Downloads/public_emdat_custom_request_2024-05-23_610a0e6c-e145-4ade-91f4-c63e8bc51e9e.xlsx'

# Read the Excel files
climate_df = pd.read_excel(climate_csv, sheet_name=1)
disaster_df = pd.read_excel(disaster_csv)

climate_df.rename(columns={'WHO Country Name': 'Country'}, inplace=True)

columns_to_keep = [
    'ISO3',
    'Country',
    'PM2.5 (μg/m3)',
    'PM10 (μg/m3)'
]
climate_df = climate_df[columns_to_keep]

# Handle missing values by filling them with the mean of the respective column
climate_df['PM2.5 (μg/m3)'].fillna(climate_df['PM2.5 (μg/m3)'].mean(), inplace=True)
climate_df['PM10 (μg/m3)'].fillna(climate_df['PM10 (μg/m3)'].mean(), inplace=True)

climate_df = climate_df.groupby(['Country', 'ISO3']).agg({
    'PM2.5 (μg/m3)': 'mean',
    'PM10 (μg/m3)': 'mean'
}).reset_index()

# Filter to keep only natural disasters and relevant subgroups
relevant_subgroups = ['Climatological', 'Meteorological']
filtered_disasters = disaster_df[
    (disaster_df['Disaster Group'] == 'Natural') & 
    (disaster_df['Disaster Subgroup'].isin(relevant_subgroups))
]

# Calculate the count of disasters per country
disaster_counts = filtered_disasters['ISO'].value_counts().reset_index()
disaster_counts.columns = ['ISO', 'Disasters']

# Merge the two DataFrames on ISO3 and ISO
merged_df = pd.merge(climate_df, disaster_counts, left_on='ISO3', right_on='ISO', how='left')

# Fill NaN values in the Disasters column with 0 (countries with no disasters recorded)
merged_df['Disasters'].fillna(0, inplace=True)

# Drop the redundant ISO column from the merged DataFrame
merged_df.drop(columns=['ISO'], inplace=True)

# Display the resulting DataFrame
print(merged_df.head())

# Connect to SQLite database
# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the SQLite database file
db_path = os.path.join(script_dir, "../data/weather_data.sqlite")
conn = sqlite3.connect(db_path)

# Save the DataFrame to a SQL table
merged_df.to_sql('merged_data', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print("Data has been successfully saved to the SQLite database.")