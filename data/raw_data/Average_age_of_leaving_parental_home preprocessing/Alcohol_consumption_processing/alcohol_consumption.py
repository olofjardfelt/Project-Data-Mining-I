import pandas as pd

# CSV data as a string
df = pd.read_csv("data/raw_data/alcohol_consumption.csv")

# Mapping of frequency values to integers
freq_mapping = {
    'DAY': 4,
    'WEEK': 3,
    'MTH': 2,
    'LT1M': 1,
    'NVR_NM12': 0
}

# Apply the mapping to the 'frequenc' column
df['freq_value'] = df['frequenc'].map(freq_mapping)

# Multiply the mapped values by the existing values in the 'frequenc' column
df['adjusted_freq_value'] = df['freq_value'] * df['OBS_VALUE']

# Group by country and aggregate the frequency values
result = df.groupby('geo')['adjusted_freq_value'].mean().reset_index()

# Print the result
print(result)

#Save as new csv file
result.to_csv("data/alcohol_consumption_processed.csv", index=False)
