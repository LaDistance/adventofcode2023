from src.util.day_2.classes.game import Game
from src.util.day_2.types import AcceptanceCriteria, Round
import pytest


@pytest.mark.parametrize(
    "rounds, criteria, expected",
    [
        (  # Under -> True
            [
                Round(red=1, blue=2, green=3),
                Round(red=0, blue=2, green=3),
                Round(red=0, blue=0, green=3),
            ],
            AcceptanceCriteria(red=10, blue=10, green=10),
            True,
        ),
        (  # Under or equal -> True
            [
                Round(red=1, blue=2, green=3),
                Round(red=0, blue=2, green=3),
                Round(red=0, blue=0, green=3),
            ],
            AcceptanceCriteria(red=1, blue=2, green=3),
            True,
        ),
        (  # Everything is equal -> True
            [
                Round(red=1, blue=2, green=3),
                Round(red=0, blue=2, green=3),
                Round(red=0, blue=0, green=3),
            ],
            AcceptanceCriteria(red=1, blue=2, green=3),
            True,
        ),
        (
            # Only one round over -> False
            [
                Round(red=1, blue=2, green=2),
                Round(red=0, blue=2, green=2),
                Round(red=2, blue=3, green=3),
            ],
            AcceptanceCriteria(red=1, blue=2, green=2),
            False,
        ),
        (
            # Every round over -> False
            [
                Round(red=10, blue=15, green=13),
                Round(red=10, blue=15, green=13),
                Round(red=10, blue=15, green=13),
            ],
            AcceptanceCriteria(red=10, blue=15, green=1),
            False,
        ),
        (
            # Every color of every round over -> False
            [
                Round(red=10, blue=15, green=13),
                Round(red=10, blue=15, green=13),
                Round(red=10, blue=15, green=13),
            ],
            AcceptanceCriteria(red=1, blue=1, green=1),
            False,
        ),
    ],
)
def test_game_is_valid(rounds, criteria, expected):
    game = Game(id=1, rounds=rounds)

    assert game.is_valid(criteria) == expected
