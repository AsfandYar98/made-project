# Project Plan

## Title
Air-Extreme: Analyzing the Impact of Air Quality on Extreme Weather Events

## Main Question
How does air quality influence the frequency and severity of extreme weather events?

## Description

Air pollution is the fourth leading risk factor for early death and the leading environmental cause of death worldwide, contributing to nearly 7 million (1 out of 9) deaths in 2019. This project investigates the relationship between air quality and extreme weather events by leveraging data from OpenAQ and EM-DAT. OpenAQ provides comprehensive air quality data, including pollutant concentrations, while EM-DAT offers detailed records of global extreme weather events. The results aim to enhance our understanding of how air pollution may contribute to extreme weather events, aiding in the development of effective environmental policies.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: WHO Air Quality Database
* Metadata URL 1: https://cdn.who.int/media/docs/default-source/air-pollution-documents/air-quality-and-health/who_database_template_2022.xlsx?sfvrsn=c948d71a_11
* Data URL 1: https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database/2022
* Data Type: CSV

Aggregates air quality data from various sources worldwide. Provides real-time and historical data on pollutants such as PM2.5, PM10, NO2, SO2, CO, and O3.

### Datasource2: EM-DAT (International Disaster Database)
* Metadata URL 2: https://doc.emdat.be/docs/data-structure-and-content/emdat-public-table/
* Data URL 2: https://public.emdat.be/data
* Data Type: CSV

Contains data on the occurrence and effects of over 22,000 mass disasters globally, including extreme weather events.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Data Acquisition and Preparation
2. Exploratory Data Analysis (EDA)
3. Statistical Analysis
4. Machine Learning Modeling
5. Interpretation and Insights