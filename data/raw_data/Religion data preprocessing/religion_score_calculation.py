import csv

# Function to convert percentage string to float
def percentage_to_float(percentage):
    return float(percentage.strip('%')) / 100

# Read the data from the CSV file
filename = "How important is religion to you - T4.csv"
with open(filename, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)

# Extract country names and data
countries = rows[0]
data_rows = [list(map(percentage_to_float, row)) for row in rows[1:]]

# Calculate weighted scores
weights = [2, 1, 0]
weighted_scores = {}

for i, country in enumerate(countries):
    score = sum(data_rows[j][i] * weights[j] for j in range(3))
    weighted_scores[country] = score

# Print results
for country, score in weighted_scores.items():
    print(f"{country}: {score:.4f}")

# Find country with highest weighted score
max_country = max(weighted_scores, key=weighted_scores.get)
max_score = weighted_scores[max_country]

print(f"\nCountry with highest weighted score: {max_country} ({max_score:.4f})")