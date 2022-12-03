#!/usr/bin/python3
#coding: utf8

Inventory = list[int]

def list_inventories_from_input(puzzle_input: str) -> list[Inventory]:
    """Build a list of elfes' inventories from puzzle input"""
    return [[int(x) for x in inventory.split("\n")] for inventory in puzzle_input.split("\n\n")]

def get_most_calories_held_by_a_single_elf(inventories: list[Inventory]) -> int:
    """Get the max calories held by a single elf from a list of elfes' inventories."""
    return max(map(lambda inventory: sum(inventory), inventories))

def get_total_calories_held_by_top_three_elfes(inventories: list[Inventory]) -> int:
    """Get the total calories held by the top three elfes from a list of elfes' inventories."""
    total_calories = list(map(lambda inventory: sum(inventory), inventories))
    total_calories.sort()
    return sum(total_calories[-3:])

def puzzle_part1(puzzle_input: str) -> int:
    """Solve the part 1 day1 puzzle."""
    inventories = list_inventories_from_input(puzzle_input)
    return get_most_calories_held_by_a_single_elf(inventories)

def puzzle_part2(puzzle_input: str) -> int:
    """Solve the part 2 day1 puzzle."""
    inventories = list_inventories_from_input(puzzle_input)
    return get_total_calories_held_by_top_three_elfes(inventories)

if __name__ == '__main__':
    with open("puzzle_input_example.txt") as f:
        # Day 1 example sample
        input_day1 = f.read()
        print("Puzzle input example")
        print("Part 1:", puzzle_part1(input_day1))
        print("Part 2:", puzzle_part2(input_day1))
    with open("puzzle_input.txt") as f:
        # Actual day 1 input
        input_day1 = f.read()
        print("Puzzle input")
        print("Part 1:", puzzle_part1(input_day1))
        print("Part 2:", puzzle_part2(input_day1))
