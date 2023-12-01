def get_calibration_value(authorized_values: dict[str, str], line: str) -> int:
    digits = find_values_in_string(authorized_values.keys(), line)
    if len(digits) == 0:
        raise ValueError('No digits found in line')
    first_digit, last_digit = authorized_values.get(digits[0]), authorized_values.get(digits[-1])
    print(first_digit, last_digit)
    return int(first_digit + last_digit)

def find_values_in_string(values: list[str], string: str) -> list[tuple[str, int]]:
    return [value for value in values if value in string]