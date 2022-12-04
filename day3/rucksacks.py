#!/usr/bin/python3
#coding: utf8

Rucksack = tuple[str, str]

def get_compartments_from_line(line: str) -> Rucksack:
    """Parse the two compartments of a rucksack from a string line."""
    line = line.strip()
    return line[len(line)//2:], line[:len(line)//2]

def get_duplicate_char(compartments: Rucksack) -> str:
    """Get the duplicate item of a Rucksack."""
    # We suppose there is only one duplicate item
    try:
        return list(set(compartments[0]) & set(compartments[1]))[0]
    except:
        print("Rucksack is not compliant")
        import sys; sys.exit(1)

def get_priority_from_char(char: str) -> int:
    """Compute the priority of a duplicate item from a Rucksack."""
    if ord(char) >= ord('a') and ord(char) <= ord('z'):
        return 1 + ord(char) - ord('a')
    elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
        return 27 + ord(char) - ord('A')
    return 0

def compute_priority_of_all_rucksacks(rucksacks: list[Rucksack]) -> int:
    """Compute the total priority of all rucksacks."""
    return sum(map(lambda rucksack: get_priority_from_char(get_duplicate_char(rucksack)), rucksacks))

if __name__ == '__main__':
    with open('puzzle_input_example.txt') as f:
        rucksacks: list[Rucksack] = list(map(lambda line: get_compartments_from_line(line), f.read().split("\n")))
        print("Puzzle input example")
        print("Part 1:", compute_priority_of_all_rucksacks(rucksacks))
    with open('puzzle_input.txt') as f:
        rucksacks: list[Rucksack] = list(map(lambda line: get_compartments_from_line(line), f.read().split("\n")))
        print("Puzzle input")
        print("Part 1:", compute_priority_of_all_rucksacks(rucksacks))
