import pytest
from src.util.day_2.common import parse_round


@pytest.mark.parametrize(
    "round_string, red, blue, green",
    [
        (
            "1 red, 2 blue, 3 green",
            1,
            2,
            3,
        ),
        (
            "1 red, 2 green",
            1,
            0,
            2,
        ),
        (
            "1 red, 2 blue",
            1,
            2,
            0,
        ),
        (
            "1 red",
            1,
            0,
            0,
        ),
        (
            "2 blue, 3 green",
            0,
            2,
            3,
        ),
        (
            "2 blue",
            0,
            2,
            0,
        ),
        (
            "3 green",
            0,
            0,
            3,
        ),
    ],
)
def test_basic_case(round_string, red, blue, green):
    round = parse_round(round_string)
    assert round.red == red
    assert round.blue == blue
    assert round.green == green
