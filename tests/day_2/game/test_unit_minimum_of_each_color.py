from src.util.day_2.classes.game import Game
from src.util.day_2.types import ColorMinimum, Round
import pytest


@pytest.mark.parametrize(
    "rounds, expected",
    [
        (
            [
                Round(red=1, blue=2, green=3),
                Round(red=0, blue=2, green=3),
                Round(red=0, blue=0, green=3),
            ],
            ColorMinimum(red=1, blue=2, green=3),
        ),
        (
            [
                Round(red=10, blue=2, green=3),
                Round(red=0, blue=21, green=3),
                Round(red=0, blue=0, green=31),
            ],
            ColorMinimum(red=10, blue=21, green=31),
        ),
        (
            [
                Round(red=0, blue=0, green=0),
            ],
            ColorMinimum(red=0, blue=0, green=0),
        ),
    ],
)
def test_basic_case(rounds, expected):
    game = Game(id=1, rounds=rounds)
    assert game.minimum_of_each_color() == expected
