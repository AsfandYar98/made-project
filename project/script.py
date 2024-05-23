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
    'PM10 (μg/m3)',
    'NO2 (μg/m3)',
    'PM25 temporal coverage (%)',
    'PM10 temporal coverage (%)',
    'NO2 temporal coverage (%)'
]
climate_df = climate_df[columns_to_keep]

climate_df = climate_df.groupby(['Country', 'ISO3']).agg({
    'PM2.5 (μg/m3)': 'mean',
    'PM10 (μg/m3)': 'mean',
    'NO2 (μg/m3)': 'mean',
    'PM25 temporal coverage (%)': 'mean',
    'PM10 temporal coverage (%)': 'mean',
    'NO2 temporal coverage (%)': 'mean'
}).reset_index()

# Filter rows where Disaster Group is "Natural"
disaster_natural = disaster_df[disaster_df['Disaster Group'] == 'Natural']

# Select only the ISO and Disaster Type columns
disaster_df_filtered = disaster_natural[['ISO', 'Disaster Type']]

# Merge the two DataFrames on ISO3 and ISO
merged_df = pd.merge(climate_df, disaster_df_filtered, left_on='ISO3', right_on='ISO', how='inner')

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