authorized_values = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def get_calibration_value(line: str) -> int:
    digits = find_values_in_string(authorized_values.keys(), line)
    if len(digits) == 0:
        raise ValueError('No digits found in line')
    first_digit, last_digit = authorized_values.get(digits[0]), authorized_values.get(digits[-1])
    print(first_digit, last_digit)
    return int(first_digit + last_digit)

def find_values_in_string(values: list[str], string: str) -> list[tuple[str, int]]:
    return [value for value in values if value in string]
