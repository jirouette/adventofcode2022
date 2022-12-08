#!/usr/bin/python3
#coding: utf8

from dataclasses import dataclass
from enum import Enum

@dataclass
class Grid:
    rows: list[list[int]]

    @property
    def width(self):
        try:
            return len(self.rows[0])
        except IndexError:
            return 0
    
    @property
    def height(self):
        return len(self.rows)
    
    def __getitem__(self, key: int) -> list[int]:
        return self.rows[key]

class Direction(Enum):
    ROW = 1
    COLUMN = 2

def parse_grid(data: str) -> Grid:
    """Parse data into a 2D list grid[y][x]."""
    return Grid([[int(tree) for tree in row] for row in data.split("\n")])

def is_a_tree_visible(grid: Grid, x: int, y: int) -> bool:
    tree = grid[y][x]

    ranges = [
        (Direction.ROW, range(x)),
        (Direction.ROW, range(x+1, grid.width)),
        (Direction.COLUMN, range(y)),
        (Direction.COLUMN, range(y+1, grid.height))
    ]
    for direction, grid_range in ranges:
        for pos in grid_range:
            if direction == Direction.ROW and grid[y][pos] >= tree:
                break
            if direction == Direction.COLUMN and grid[pos][x] >= tree:
                break
        else:
            return True
    return False

def get_tree_scenic_score(grid: Grid, x: int, y: int) -> int:
    final_score = 1
    tree = grid[y][x]

    ranges = [
        (Direction.ROW, range(x-1, -1, -1)),
        (Direction.ROW, range(x+1, grid.width)),
        (Direction.COLUMN, range(y-1, -1, -1)),
        (Direction.COLUMN, range(y+1, grid.height))
    ]
    for direction, grid_range in ranges:
        current_score = 0
        for pos in grid_range:
            current_score += 1
            if direction == Direction.ROW and grid[y][pos] >= tree:
                break
            if direction == Direction.COLUMN and grid[pos][x] >= tree:
                break
        final_score *= current_score
        if final_score == 0:
            return 0 # no need to continue this
    return final_score

def visible_trees(grid: Grid) -> int:
    return sum([is_a_tree_visible(grid, x, y) for y in range(grid.height) for x in range(grid.width)])

def get_max_scenic_score(grid: Grid) -> int:
    return max([get_tree_scenic_score(grid, x, y) for y in range(grid.height) for x in range(grid.width)])

if __name__ == '__main__':
    with open('day8/puzzle_input_example.txt') as f:
        grid = parse_grid(f.read().strip())
        print("Puzzle input example")
        print("Part 1:", visible_trees(grid))
        print("Part 2:", get_max_scenic_score(grid))
    with open('day8/puzzle_input.txt') as f:
        grid = parse_grid(f.read().strip())
        print("Puzzle input")
        print("Part 1:", visible_trees(grid))
        print("Part 2:", get_max_scenic_score(grid))
