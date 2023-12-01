import typer
from importlib import import_module
from rich import print
from util.cli.validate import validate_input
app = typer.Typer()

puzzle_number_mapper = {
    1: 'first',
    2: 'second'
}

@app.command()
def solve_puzzle(day: int, puzzle_number: int):
    day, puzzle_number = validate_input(day, puzzle_number)

    module_to_import = puzzle_number_mapper[puzzle_number]

    module = import_module(f'solutions.day_{day}.{module_to_import}')

    input_path, output_path = f'inputs/day_{day}.txt', f'outputs/day_{day}_{puzzle_number}.txt'

    module.solve(input_path, output_path)

    print("Done ! You can now find the solution in the outputs folder.")

if __name__ == "__main__":
    app()