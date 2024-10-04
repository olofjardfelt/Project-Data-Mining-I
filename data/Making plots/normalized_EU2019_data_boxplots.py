import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Define the file names and the corresponding headers to extract
files = [
    "EU2019_unemployment_rate.csv",
    "EU2019_Alcohol_consumption.csv",
    "EU2019_avg_age_of_leaving_parental_home.csv",
    "EU2019_Gini_Index.csv",
    "EU2019_internet_usage.csv",
    "EU2019_religion_importance_weighted_scores.csv",
    "EU2019_suicide_rates.csv"
]

# Empty lists to store the normalized data and labels
data = []
# labels = []
labels = ['Unemployment', 'Alcohol Consumption', 'Leaving parental home', 'Gini Index', 'Internet Usage', 'Religious Importance', 'Suicide mortality']


# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Loop over files, normalize the second column, and store the data
for file in files:
    df = pd.read_csv(file)
    # Get the label from the second header of each file
    # labels.append(df.columns[1]) (ANVÄND DETTA FÖR AUTOMATISK LABEL SKAPANDE)
    # Extract the second column values, reshape for scaling, and normalize using MinMaxScaler
    values = df.iloc[:, 1].dropna().values.reshape(-1, 1)
    normalized_values = scaler.fit_transform(values).flatten()  # Normalize and flatten to 1D array
    data.append(normalized_values)

# Create a figure for boxplots
plt.figure(figsize=(10, 6))

# Plot the boxplots of the normalized data
plt.boxplot(data, labels=labels)

# Rotate the labels if they are too long
plt.xticks(rotation=45, ha="right")

# Add a title and grid for clarity
plt.title('Normalized EU2019 Data Boxplots')
plt.grid(True)

# Save the plot as an image (e.g., PNG file)
plt.tight_layout()
plt.savefig('normalized_EU2019_data_boxplots.png', dpi=300)

# Optionally, close the plot if you are running this in a script to avoid memory leaks
plt.close()
