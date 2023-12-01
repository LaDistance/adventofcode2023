from typing_extensions import Annotated
import typer
from importlib import import_module
from rich import print
from src.util.cli.validate import validate_input

app = typer.Typer()

puzzle_number_mapper = {1: "first", 2: "second"}


@app.command()
def solve_puzzle(
    day: Annotated[int, typer.Option()], puzzle_number: Annotated[int, typer.Option()]
):
    day, puzzle_number = validate_input(day, puzzle_number)

    module_to_import = puzzle_number_mapper[puzzle_number]

    module = import_module(f"src.day_{day}.{module_to_import}")

    input_path, output_path = (
        f"inputs/day_{day}.txt",
        f"outputs/day_{day}_{puzzle_number}.txt",
    )

    module.solve(input_path, output_path)

    print("Done ! You can now find the solution in the outputs folder.")


if __name__ == "__main__":
    app()
