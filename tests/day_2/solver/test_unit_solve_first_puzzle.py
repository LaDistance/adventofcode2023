from src.util.day_2.classes.game import Game
from src.util.day_2.classes.solver import Solver
from src.util.day_2.types import AcceptanceCriteria
from unittest.mock import Mock


def test_every_game_valid():
    # Mock the Game class
    mock_game = Mock(spec=Game)
    mock_game.is_valid.return_value = True
    mock_game.id = 5

    mock_criteria = Mock(spec=AcceptanceCriteria)
    mock_criteria.blue = 1
    mock_criteria.red = 2
    mock_criteria.green = 3

    solver = Solver(
        games=[mock_game, mock_game, mock_game, mock_game, mock_game],
        criteria=mock_criteria,
    )

    assert solver.solve_first_puzzle() == 25
