#!/usr/bin/python3
#coding: utf8

Grid = list[list[int]] # Grid[y][x]

def parse_grid(data: str) -> Grid:
    """Parse data into a 2D list grid[y][x]."""
    return [[int(tree) for tree in row] for row in data.split("\n")]

def is_a_tree_visible(grid: Grid, x: int, y: int) -> bool:
    height = len(grid)
    width = len(grid[0])
    tree = grid[y][x]
    if x in [0, width-1] or y in [0, height-1]:
        return True
    
    for row_grid_range in [range(x), range(x+1, width)]:
        for i in row_grid_range:
            if grid[y][i] >= tree:
                break
        else:
            return True # is visible from the left or the right

    for column_grid_range in [range(y), range(y+1, height)]:
        for j in column_grid_range:
            if grid[j][x] >= tree:
                break
        else:
            return True # is visible from the top or the bottom

    return False # is not visible


def visible_trees(grid: Grid) -> int:
    height = len(grid)
    width = len(grid[0])
    trees = 0
    for x in range(width):
        for y in range(height):
            if is_a_tree_visible(grid, x, y):
                trees += 1
    return trees            

if __name__ == '__main__':
    with open('day8/puzzle_input_example.txt') as f:
        grid = parse_grid(f.read().strip())
        print("Puzzle input example")
        print("Part 1:", visible_trees(grid))
    with open('day8/puzzle_input.txt') as f:
        grid = parse_grid(f.read().strip())
        print("Puzzle input")
        print("Part 1:", visible_trees(grid))