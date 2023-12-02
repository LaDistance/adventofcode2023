from src.util.day_2.common import parse_game
from src.util.day_2.types import Round
import pytest


@pytest.mark.parametrize(
    "game_string, game_id, rounds",
    [
        (
            "Game 1: 1 red, 2 blue, 3 green; 2 blue, 3 green; 3 green",
            1,
            [
                Round(red=1, blue=2, green=3),
                Round(red=0, blue=2, green=3),
                Round(red=0, blue=0, green=3),
            ],
        ),
        (
            "Game 99999: 1 red, 2 blue, 3 green; 2 blue, 3 green; 3 green",
            99999,
            [
                Round(red=1, blue=2, green=3),
                Round(red=0, blue=2, green=3),
                Round(red=0, blue=0, green=3),
            ],
        ),
        (
            "Game 1234: 1 red",
            1234,
            [
                Round(red=1, blue=0, green=0),
            ],
        ),
    ],
)
def test_basic_case(game_string, game_id, rounds):
    game_id, rounds = parse_game(game_string)
    assert game_id == game_id
    assert rounds == rounds
