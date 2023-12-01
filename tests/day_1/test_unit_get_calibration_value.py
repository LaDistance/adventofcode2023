from src.util.day_1.common import get_calibration_value
import pytest


@pytest.mark.parametrize(
    "authorized_values, line, expected",
    [
        (
            {
                "1": "1",
                "2": "2",
                "3": "3",
            },
            "abcde1",
            11,
        ),
        (
            {
                "1": "1",
                "2": "2",
                "3": "3",
            },
            "1abcde1",
            11,
        ),
        (
            {
                "1": "1",
                "2": "2",
                "3": "3",
                "4": "4",
                "5": "5",
                "6": "6",
                "7": "7",
                "8": "8",
                "9": "9",
            },
            "abcde9",
            99,
        ),
        (
            {
                "1": "1",
                "2": "2",
                "3": "3",
                "4": "4",
                "5": "5",
                "6": "6",
                "7": "7",
                "8": "8",
                "9": "9",
            },
            "abc8def9",
            89,
        ),
        (
            {
                "1": "1",
                "2": "2",
                "3": "3",
                "4": "4",
                "5": "5",
                "6": "6",
                "7": "7",
                "8": "8",
                "9": "9",
            },
            "999999",
            99,
        ),
        (
            {
                "one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9",
            },
            "eightwo",
            82,
        ),
    ],
)
def test_get_calibration_value(authorized_values, line, expected):
    assert get_calibration_value(authorized_values, line) == expected
