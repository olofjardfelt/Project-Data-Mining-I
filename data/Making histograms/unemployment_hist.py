import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('EU2019_unemployment_rate.csv')

# Create the histogram
plt.figure(figsize=(12, 6))
plt.hist(df['2019'], bins=10, edgecolor='black')

# Customize the plot
plt.title('Histogram of EU Unemployment Rates (2019)')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Frequency')

# Add grid lines
plt.grid(axis='y', alpha=0.75)

# Show the plot
plt.show()

# Optional: Save the plot as an image file
# plt.savefig('eu_unemployment_histogram.png')