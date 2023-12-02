from typing import List

from src.util.day_2.types import AcceptanceCriteria, ColorMinimum, Round


class Game:
    def __init__(
        self,
        id: int,
        rounds: List[Round],
    ):
        self.rounds = rounds
        self.id = id

    def is_valid(self, criteria: AcceptanceCriteria) -> bool:
        for round in self.rounds:
            if (
                round.blue > criteria.blue
                or round.red > criteria.red
                or round.green > criteria.green
            ):
                return False

        return True

    def minimum_of_each_color(self) -> ColorMinimum:
        return ColorMinimum(
            blue=max([round.blue for round in self.rounds]),
            red=max([round.red for round in self.rounds]),
            green=max([round.green for round in self.rounds]),
        )

    def power(self) -> int:
        minimum_of_each_color = self.minimum_of_each_color()
        return (
            minimum_of_each_color.blue
            * minimum_of_each_color.red
            * minimum_of_each_color.green
        )
