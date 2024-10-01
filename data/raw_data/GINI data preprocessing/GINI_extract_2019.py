import pandas as pd

# Load the Gini index data from the EU_Gini_Data.csv file
gini_data = pd.read_csv('EU_Gini_Data.csv')

# Extract the year 2019 data
gini_2019 = gini_data[['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', '2019']]

# Rename the '2019' column to 'Gini Index 2019' for clarity
gini_2019.rename(columns={'2019': 'Gini Index 2019'}, inplace=True)

# Save the extracted data to a new CSV file
gini_2019.to_csv('Gini_Index_2019.csv', index=False)

print("Gini index data for 2019 saved to 'Gini_Index_2019.csv'")
