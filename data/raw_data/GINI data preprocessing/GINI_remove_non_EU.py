import pandas as pd

# Load the EU countries from the EU_countries.csv file
eu_countries = pd.read_csv('EU_Country_Name_WorldBank.csv')
eu_country_list = eu_countries['Country Name'].tolist()

# Load the Gini index data from the API_SI.POV.GINI_DS2_en_csv_v2_31732.csv file
gini_data = pd.read_csv('API_SI.POV.GINI_DS2_en_csv_v2_31732.csv', skiprows=4)  # Skip metadata rows

# Filter the data to only include EU countries
filtered_data = gini_data[gini_data['Country Name'].isin(eu_country_list)]

# Save the filtered data to a new CSV file
filtered_data.to_csv('EU_Gini_Data.csv', index=False)

print("Filtered data saved to 'EU_Gini_Data.csv'")
