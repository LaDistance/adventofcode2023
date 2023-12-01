from src.util.day_1.common import get_calibration_value

authorized_values = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solve(input_path: str, output_path: str) -> int:
    # Read the input file as lines
    with open(input_path, "r") as f:
        lines = f.readlines()
        if len(lines) == 0:
            raise ValueError("Input file is empty")
        calibration_values = [
            get_calibration_value(authorized_values, line) for line in lines
        ]
        solution = str(sum(calibration_values))

    with open(output_path, "w") as f:
        f.write(solution)
