def parse_fixed_width_line(line, field_lengths):
    fields = []
    start = 0
    for length in field_lengths:
        field = line[start:start + length].strip()
        fields.append(field)
        start += length
    return fields
