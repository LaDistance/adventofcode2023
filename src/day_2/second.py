from src.util.day_2.common import parse_game
from src.util.day_2.types import AcceptanceCriteria
from src.util.day_2.classes.game import Game
from src.util.day_2.classes.solver import Solver


def solve(input_path: str, output_path: str):
    # Read the input file as lines
    with open(input_path, "r") as f:
        lines = f.readlines()
        if len(lines) == 0:
            raise ValueError("Input file is empty")

        games = []
        for line in lines:
            game_id, rounds = parse_game(line)
            games.append(Game(game_id, rounds))

        solver = Solver(games)
        solution = sum([game.power() for game in solver.games])

    with open(output_path, "w") as f:
        f.write(str(solution))
