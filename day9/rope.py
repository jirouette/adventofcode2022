#!/usr/bin/python3
#coding: utf8

from dataclasses import dataclass
from enum import Enum
import math

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
        
        prev_knot = head
        last_knot_pos: BasicPosition = (knots[-1].x, knots[-1].y)
        for knot in knots:
            if is_knot_far_beyond(prev_knot, knot):
                update_knot(prev_knot, knot)
            prev_knot = knot
            last_knot_pos = (knot.x, knot.y)
        tail_pos.append(last_knot_pos)
        #print(direction, steps+1, head, tail)
    return tail_pos

def part1(data: str, nb_knots: int = 2) -> int:
    nb_moves = []
    knots = [Position(0, 0) for _ in range(nb_knots)]
    nb_moves = [pos for move in parse_moves(data) for pos in apply_move(knots, move)]
    return len(set(nb_moves))

def part2(data: str) -> int:
    return part1(data, nb_knots=10)

def is_knot_far_beyond(knot1: Position, knot2: Position) -> bool:
    return abs(knot1.x - knot2.x) > 1 or abs(knot1.y - knot2.y) > 1

def update_knot(knot1: Position, knot2: Position):
    if knot2.x == knot1.x:
        knot2.y += knot1.y > knot2.y
        knot2.y -= knot1.y < knot2.y
    elif knot2.y == knot1.y:
        knot2.x += knot1.x > knot2.x
        knot2.x -= knot1.x < knot2.x
    else:
        knot2.x += knot1.x > knot2.x
        knot2.x -= knot1.x < knot2.x
        knot2.y += knot1.y > knot2.y
        knot2.y -= knot1.y < knot2.y

if __name__ == '__main__':
    with open('day9/puzzle_input_example.txt') as f:
        print("Puzzle input example")
        data = f.read()
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
    with open('day9/puzzle_input.txt') as f:
        print("Puzzle input")
        data = f.read()
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
