# Script that takes this website' info: https://www.iban.com/country-codes
# Which is first must be saved to CSV via excel
# and adds the row "3 digit country code" to create a full list of eu countries with names and all sorts of codes used. 

import pandas as pd

df_original = pd.read_csv('countries_with_codes.csv')

#print(df_original.columns) # = ['Country Name', '2-letter Country Code', '3-letter Country Code'], dtype='object')

#Assign headers as
column_names = ['Country name', '2-letter Country Code', '3-letter Country Code', '3-digit Country Code']

# loads the file
# Saves the 3 digit country code as string to avoid number like '040' to become just '40'. 
df  = pd.read_csv('Country_codes_world.csv', sep = ';', names=column_names, dtype={'3-digit Country Code': str})

# join the two dataframes on the two letter code
DF_EU_updated = pd.merge(df_original, df[['2-letter Country Code', '3-digit Country Code']], on='2-letter Country Code', how='left')
#print(DF_EU_updated)

#write to a new CSV:
DF_EU_updated.to_csv('Full_EU-countries_with_codes.csv', sep=',')