import csv

def write_to_csv(parsed_lines, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for line in parsed_lines:
            writer.writerow(line)
