import pandas as pd
import matplotlib.pyplot as plt

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


# Loop over files, create a histogram for each, normalize the data, and save it
for file in files:
    # Read the CSV file
    df = pd.read_csv(file)
    # Get the label from the second header of each file (used for title and saving the file)
    label = df.columns[1]
    # Extract and normalize the data
    values = df.iloc[:, 1].dropna().values.reshape(-1, 1)
    
    # Create a figure for the histogram
    plt.figure(figsize=(8, 5))
    
    # Plot the histogram
    plt.hist(values, bins=10, color='skyblue', edgecolor='black')
    
    # Add title and labels
    plt.title(f'Histogram of {label}')
    plt.xlabel(f'{label}')
    plt.ylabel('Frequency')
    
    # Save the histogram as an image (using label for the filename)
    filename = f'histogram_{label.replace(" ", "_")}.png'
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    
    # Optionally close the plot to free memory
    plt.close()
