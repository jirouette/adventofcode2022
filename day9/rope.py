#!/usr/bin/python3
#coding: utf8

from dataclasses import dataclass
from enum import Enum

@dataclass
class Position:
    x: int = 0
    y: int = 0

BasicPosition = tuple[int, int] # x,y

class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"

Move = tuple[Direction, int]

def parse_moves(data: str) -> list[Move]:
    data: list[str] = data.split()
    return [(Direction(direction), int(steps)) for direction, steps in zip(data[::2], data[1::2])]

def apply_move(knots: list[Position], move: Move) -> list[BasicPosition]:
    """Apply a move to the head knot of a rope, then check and update the following knots and finally return all the tail's BasicPositions it went through."""
    direction, steps = move
    tail_pos = []
    head, knots = knots[0], knots[1:]
    while steps:
        steps -= 1
        match direction:
            case Direction.UP:
                head.y += 1
            case Direction.DOWN:
                head.y -= 1
            case Direction.LEFT:
                head.x -= 1
            case Direction.RIGHT:
                head.x += 1
        tail_pos.append(check_and_update_knots(head, knots))
    return tail_pos

def check_and_update_knots(prev_knot: Position, knots: list[Position]) -> BasicPosition:
    """Check and update all the knots, and returns its tail's BasicPosition."""
    for knot in knots:
        if is_knot_far_beyond(prev_knot, knot):
            update_knot(prev_knot, knot)
        prev_knot = knot
    return knots[-1].x, knots[-1].y

def build_rope_and_move(data: str, nb_knots: int = 2) -> int:
    """Define an rope and move according to the puzzle input."""
    knots = [Position(0, 0) for _ in range(nb_knots)]
    moves = [pos for move in parse_moves(data) for pos in apply_move(knots, move)]
    return len(set(moves))

def is_knot_far_beyond(knot1: Position, knot2: Position) -> bool:
    """Check whether a knot should move or not."""
    return abs(knot1.x - knot2.x) > 1 or abs(knot1.y - knot2.y) > 1

def update_knot(knot1: Position, knot2: Position):
    """Update a knot according to the position of the previous knot."""
    knot2.y += knot1.y > knot2.y
    knot2.y -= knot1.y < knot2.y
    knot2.x += knot1.x > knot2.x
    knot2.x -= knot1.x < knot2.x

if __name__ == '__main__':
    with open('day9/puzzle_input_example.txt') as f:
        print("Puzzle input example")
        data = f.read()
        print("Part 1:", build_rope_and_move(data))
        print("Part 2:", build_rope_and_move(data, nb_knots=10))
    with open('day9/puzzle_input.txt') as f:
        print("Puzzle input")
        data = f.read()
        print("Part 1:", build_rope_and_move(data))
        print("Part 2:", build_rope_and_move(data, nb_knots=10))
