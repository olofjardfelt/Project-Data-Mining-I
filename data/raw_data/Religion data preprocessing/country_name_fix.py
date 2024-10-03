import csv

# Read the country codes and names
country_codes = {}
with open('EU_countries.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        country_codes[row['2-letter Country Code']] = row['Country Name']

# Read the religion importance data and create a new CSV with country names
with open('religion_importance_weighted_scores.csv', 'r') as input_file, \
     open('religion_importance_by_country_name.csv', 'w', newline='') as output_file:
    
    csv_reader = csv.DictReader(input_file)
    fieldnames = ['Country', 'Weighted Score']
    csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    
    for row in csv_reader:
        country_code = row['Country']
        country_name = country_codes.get(country_code, country_code)  # Use code if name not found
        csv_writer.writerow({
            'Country': country_name,
            'Weighted Score': row['Weighted Score']
        })

print("New CSV file 'religion_importance_by_country_name.csv' has been created.")