import csv
import random
from faker import Faker

fake = Faker()

# Parameters
num_rows = 10**6  # Adjust to generate larger or smaller files
file_name = 'data.csv'

# Generate CSV
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])

    for _ in range(num_rows):
        writer.writerow([fake.first_name(), fake.last_name(), fake.address(), fake.date_of_birth()])

print(f"CSV file '{file_name}' with {num_rows} rows generated successfully.")
