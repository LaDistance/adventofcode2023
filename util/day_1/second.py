from typing import Tuple

digit_mapper = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
}

def get_calibration_value(line: str) -> int:
    line = line.strip()
    first_digit, index = get_first_digit(line)
    last_digit = get_last_digit(line[index:])
    return int(first_digit + last_digit)


def get_first_digit(line: str) -> Tuple[str, int]:
    string = ""
    for index, char in enumerate(line):
        try:
            first_digit = str(int(char))
            return first_digit, index
        except ValueError:
            string += char
            if is_one_of_value_list_in_string(
                [
                    "one",
                    "two",
                    "three",
                    "four",
                    "five",
                    "six",
                    "seven",
                    "eight",
                    "nine",
                ],
                string,
            ):
                return digit_mapper[string], index
            continue

def get_last_digit(line: str) -> str:
    string = ''
    for char in reversed(line):
        print(char)
        try:
            last_digit = str(int(char))
            return last_digit
        except ValueError:
            string = char + string
            if is_one_of_value_list_in_string(
                [
                    "one",
                    "two",
                    "three",
                    "four",
                    "five",
                    "six",
                    "seven",
                    "eight",
                    "nine",
                ],
                string,
            ):
                return digit_mapper[string]
            continue

def is_one_of_value_list_in_string(value_list: list[str], string: str) -> bool:
    for value in value_list:
        if value in string:
            return True

    return False
