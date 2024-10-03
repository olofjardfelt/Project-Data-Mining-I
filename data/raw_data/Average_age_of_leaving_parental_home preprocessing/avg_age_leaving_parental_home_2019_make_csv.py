import csv

# Function to process each line
def process_line(line):
    # Replace semicolon with comma
    line = line.replace(';', ',')
    # Replace comma with period in the numeric part
    parts = line.split(',')
    if len(parts) > 1:
        parts[1] = parts[1].replace(',', '.')
    return ','.join(parts)

# Read the input data from CSV file
input_filename = 'avg_age_leaving_parental_home_2019.csv'
output_filename = 'processed_data.csv'

try:
    with open(input_filename, 'r', encoding='utf-8') as input_file, \
         open(output_filename, 'w', encoding='utf-8', newline='') as output_file:
        
        csv_reader = csv.reader(input_file, delimiter=';')
        csv_writer = csv.writer(output_file)
        
        for row in csv_reader:
            if len(row) > 1:
                country = row[0]
                value = row[1].replace(',', '.')
                csv_writer.writerow([country, value])

    print(f"Data has been processed and saved to {output_filename}")
    
    # Print the first few lines of the processed data
    print("\nFirst few lines of the processed data:")
    with open(output_filename, 'r', encoding='utf-8') as output_file:
        for _ in range(5):  # Print first 5 lines
            print(output_file.readline().strip())

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")