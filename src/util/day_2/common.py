from typing import List, Tuple

from src.util.day_2.types import Round


def parse_game(line: str) -> Tuple[int, List[Round]]:
    introduction, rounds = line.split(":")
    game_id = int(introduction.split(" ")[1])

    rounds_strings = rounds.split(";")
    rounds = [parse_round(round_string) for round_string in rounds_strings]

    return game_id, rounds


def parse_round(round: str) -> Round:
    round = round.strip()
    round_parts = round.split(",")
    red, blue, green = 0, 0, 0
    for part in round_parts:
        amount, color = part.strip().split(" ")
        if color == "blue":
            blue = amount
        elif color == "red":
            red = amount
        elif color == "green":
            green = amount

    return Round(blue=int(blue), red=int(red), green=int(green))
