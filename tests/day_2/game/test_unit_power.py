from src.util.day_2.classes.game import Game
from src.util.day_2.types import Round


def test_basic_case():
    game = Game(
        id=1,
        rounds=[
            Round(red=1, blue=2, green=3),
            Round(red=0, blue=2, green=3),
            Round(red=0, blue=0, green=3),
        ],
    )

    assert game.power() == 6
