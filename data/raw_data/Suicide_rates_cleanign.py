## Takes the file "suicide_rates.csv", cleans it and spits out:
# *nr of total suicides per 100 000 (suicide RATE)
# *in EU countries
# one row per country

import pandas as pd


# loads the reference list used for picking out the relevant countries 
eu_countries = pd.read_csv('Full_EU-countries_with_codes.csv')
eu_country_list = eu_countries['3-digit Country Code'].tolist()

#Loads the data to clean
SR  = pd.read_csv('suicide_rates.csv')

#Filters so that only 2019 data is on
SR_2019 = SR[SR['DIM_TIME'] == 2019]
#filters so that only the relevant countries are on
SR_EU_2019 = SR_2019[SR_2019['DIM_GEO_CODE_M49'].isin(eu_country_list)]
#filters so that the data shown are only total suicide rates, not divided by gender
SR_TOTSEX_EU_2019 = SR_EU_2019[SR_EU_2019['DIM_SEX'] == 'TOTAL']
#filters so that only data that takes all ages into account are on
SR_TOTAGE_TOTSEX_EU_2019 = SR_TOTSEX_EU_2019[SR_TOTSEX_EU_2019['DIM_AGE'] == 'TOTAL']

#Cleans all info we do not need from the original data
Attributes = ['DIM_GEO_CODE_M49', 'RATE_PER_100000_N']
SR_CLEAN = SR_TOTAGE_TOTSEX_EU_2019[Attributes]

# ----- Some checking if it actually works
# print(len(eu_country_list))
# print(len(SR_CLEAN))
# list_DF = SR_CLEAN['DIM_GEO_CODE_M49'].tolist()

# #print('\n \n \n')
# #print(list_DF)
# #print('\n')
# #print(eu_country_list)
# for eu in eu_country_list:
#     if eu not in list_DF:
#         print(f'not in dataframe: {eu}')

# for eu in list_DF:
#     if eu not in eu_countries:
#         print(f'not in list of countries but in datalist: {eu}')
# ----- checking completed ----- 


#adds country names to DF, from reference list also used for cleaning:
DF_merged = pd.merge(SR_CLEAN, eu_countries[['Country Name', '3-digit Country Code']], left_on='DIM_GEO_CODE_M49', right_on='3-digit Country Code', how='left')
#make the order of columns make more sence
SR_CLEANED_ORDERED = DF_merged[['Country Name', 'RATE_PER_100000_N']]

#Make the CSV:
SR_CLEANED_ORDERED.to_csv('suicide_rates_2019_cleaned.csv', sep=',')
