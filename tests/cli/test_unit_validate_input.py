from src.util.cli.validate import validate_input
import pytest


@pytest.mark.parametrize(
    "day, puzzle_number, expected",
    [
        (1, 1, (1, 1)),
        (1, 2, (1, 2)),
        (25, 1, (25, 1)),
        (25, 2, (25, 2)),
    ],
)
def test_validate_input(day, puzzle_number, expected):
    assert validate_input(day, puzzle_number) == expected


def test_wrong_day():
    with pytest.raises(ValueError):
        validate_input(0, 1)


def test_wrong_puzzle_number():
    with pytest.raises(ValueError):
        validate_input(1, 3)


def test_wrong_both():
    with pytest.raises(ValueError):
        validate_input(0, 3)
