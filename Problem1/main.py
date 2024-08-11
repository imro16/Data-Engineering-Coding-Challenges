from parse_fixed_width_file import parse_fixed_width_file

field_lengths = [5, 10, 10, 8, 4]  # Example specification for employees.txt

parse_fixed_width_file('employees.txt', field_lengths, 'employees.csv')
