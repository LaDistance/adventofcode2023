from dataclasses import dataclass


@dataclass
class Round:
    blue: int
    red: int
    green: int


@dataclass
class AcceptanceCriteria:
    blue: int
    red: int
    green: int


@dataclass
class ColorMinimum:
    blue: int
    red: int
    green: int
