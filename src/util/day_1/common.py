def get_calibration_value(authorized_values: dict[str, str], line: str) -> int:
    first_digit = find_first_value_in_string(authorized_values, line)
    last_digit = find_first_value_in_string(authorized_values, line, reversed=True)
    return int(first_digit + last_digit)


def find_first_value_in_string(
    authorized_values: dict[str, str], string: str, reversed: bool = False
) -> str:
    temp = ""
    if reversed:
        string = string[::-1]
    for char in string:
        if reversed:
            temp = char + temp
        else:
            temp += char

        for key, value in authorized_values.items():
            if key in temp:
                return value
