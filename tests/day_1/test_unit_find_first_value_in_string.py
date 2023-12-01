import pytest
from src.util.day_1.common import find_first_value_in_string


# Use parametrize to test multiple values in one test
@pytest.mark.parametrize(
    "string,expected",
    [
        ("1", "1"),
        ("0", None),
        ("21", "2"),
    ],
)
def test_values_in_string_day_one(day_one_authorized_values, string, expected):
    assert find_first_value_in_string(day_one_authorized_values, string) == expected


@pytest.mark.parametrize(
    "string,expected",
    [
        ("1", "1"),
        ("0", None),
        ("321", "1"),
    ],
)
def test_values_in_string_reversed_day_one(day_one_authorized_values, string, expected):
    assert (
        find_first_value_in_string(day_one_authorized_values, string, reversed=True)
        == expected
    )


@pytest.mark.parametrize(
    "string,expected",
    [
        ("one", "1"),
        ("on", None),
        ("eightwo", "8"),
    ],
)
def test_values_in_string_day_two(day_two_authorized_values, string, expected):
    assert find_first_value_in_string(day_two_authorized_values, string) == expected


@pytest.mark.parametrize(
    "string,expected",
    [("one", "1"), ("on", None), ("eightwo", "2"), ("owte", None), ("tw1o", "1")],
)
def test_values_in_string_reversed_day_two(day_two_authorized_values, string, expected):
    assert (
        find_first_value_in_string(day_two_authorized_values, string, reversed=True)
        == expected
    )
