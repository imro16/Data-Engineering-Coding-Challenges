from parse_fixed_width_line import parse_fixed_width_line
from write_to_csv import write_to_csv

def parse_fixed_width_file(input_file, field_lengths, output_file):
    parsed_lines = []
    with open(input_file, 'r') as file:
        for line in file:
            parsed_line = parse_fixed_width_line(line, field_lengths)
            parsed_lines.append(parsed_line)
    
    write_to_csv(parsed_lines, output_file)
