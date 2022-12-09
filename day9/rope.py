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

def apply_move(head: Position, tail: Position, move: Move) -> list[BasicPosition]:
    direction, steps = move
    tail_pos = []
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
        if is_tail_far_beyond(head, tail):
            tail_pos.append(update_tail(head, tail))
    return tail_pos

def part1(data: str) -> int:
    nb_moves = []
    head = Position(0, 0)
    tail = Position(0, 0)
    nb_moves = [pos for move in parse_moves(data) for pos in apply_move(head, tail, move)]
    return len(set(nb_moves)) + 1 # not forgetting the starting position

def is_tail_far_beyond(head: Position, tail: Position) -> bool:
    return abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1

def update_tail(head: Position, tail: Position) -> BasicPosition:
    if tail.x == head.x:
        tail.y += head.y > tail.y
        tail.y -= head.y < tail.y
    elif tail.y == head.y:
        tail.x += head.x > tail.x
        tail.x -= head.x < tail.x
    else:
        tail.x += head.x > tail.x
        tail.x -= head.x < tail.x
        tail.y += head.y > tail.y
        tail.y -= head.y < tail.y
    return tail.x, tail.y

if __name__ == '__main__':
    with open('day9/puzzle_input_example.txt') as f:
        print("Puzzle input example")
        print("Part 1:", part1(f.read()))
    with open('day9/puzzle_input.txt') as f:
        print("Puzzle input")
        print("Part 1:", part1(f.read()))
