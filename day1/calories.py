#!/usr/bin/python3
#coding: utf8

Inventory = list[int]

def list_inventories_from_input(puzzle_input: str) -> list[Inventory]:
    """Build a list of elfes' inventories from puzzle input"""
    return [[int(x) for x in inventory.split("\n")] for inventory in puzzle_input.split("\n\n")]

def get_most_calories_held_by_a_single_elf(inventories: list[Inventory]) -> int:
    """Get the max calories held by a single elf from a list of elfes' inventories."""
    return max(map(lambda inventory: sum(inventory), inventories))

def puzzle(puzzle_input: str) -> int:
    """Solve the puzzle day1."""
    inventories = list_inventories_from_input(puzzle_input)
    return get_most_calories_held_by_a_single_elf(inventories)

if __name__ == '__main__':
    with open("puzzle_input_example.txt") as f:
        # Day 1 example sample
        print("Puzzle input example:", puzzle(f.read()))
    with open("puzzle_input.txt") as f:
        # Actual day 1 input
        print("Puzzle input:", puzzle(f.read()))
