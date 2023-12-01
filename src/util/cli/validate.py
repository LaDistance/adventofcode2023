def validate_input(day: int, puzzle_number: int):
    if(day < 1 or day > 25):
        raise ValueError('Day must be between 1 and 25')
    if(puzzle_number not in (1,2)):
        raise ValueError('Sub-puzzle must be 1 or 2')

    return day, puzzle_number