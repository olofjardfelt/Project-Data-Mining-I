import csv

# Step 1: Read the countries_with_codes.csv file
with open('data/raw_data/countries_with_codes.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    countries_with_codes = {row[0] for row in reader}

# Step 2: Read the alcohol_consumption_per_capita.csv file
with open('data/raw_data/alcohol_consumption_per_capita.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    header = next(reader)  # Save the header
    filtered_rows = [row for row in reader if row[0].strip() in countries_with_codes]

# Step 3: Write the filtered data to a new CSV file
with open('data/raw_data/filtered_alcohol_consumption.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(header)  # Write the header
    writer.writerows(filtered_rows)  # Write the filtered rows