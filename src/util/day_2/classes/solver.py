from typing import List, Optional

from src.util.day_2.classes.game import Game
from src.util.day_2.types import AcceptanceCriteria


class Solver:
    def __init__(
        self,
        games: List[Game],
        criteria: Optional[AcceptanceCriteria] = AcceptanceCriteria(
            red=0, blue=0, green=0
        ),
    ):
        self.games = games
        self.criteria = criteria

    def solve_first_puzzle(self) -> int:
        sum = 0
        for game in self.games:
            if game.is_valid(self.criteria):
                sum += game.id

        return sum
