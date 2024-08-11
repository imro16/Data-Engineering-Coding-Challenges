import csv
import hashlib

def anonymize_value(value):
    """Hashes a value using SHA-256"""
    return hashlib.sha256(value.encode()).hexdigest()

# Read and anonymize CSV
def anonymize_csv(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            row['first_name'] = anonymize_value(row['first_name'])
            row['last_name'] = anonymize_value(row['last_name'])
            row['address'] = anonymize_value(row['address'])
            writer.writerow(row)

anonymize_csv('data.csv', 'anonymized_data.csv')
print(f"Anonymized CSV file 'anonymized_data.csv' generated successfully.")
