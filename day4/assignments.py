#!/usr/bin/python3
#coding: utf8

AssignmentPair = tuple[set, set]

def parse_pair(line: str) -> AssignmentPair:
    """Parse a assignments pair from an input line."""
    first_elf, second_elf = line.strip().split(",")
    first_elf_range = [int(assignement) for assignement in first_elf.split("-")]
    second_elf_range = [int(assignement) for assignement in second_elf.split("-")]
    return set(range(first_elf_range[0], first_elf_range[1]+1)), set(range(second_elf_range[0], second_elf_range[1]+1))

def does_an_assignment_contain_another(pair: AssignmentPair) -> bool:
    """Check whether an assignement fully contains another within a pair."""
    intersection = pair[0] & pair[1]
    return pair[0] == intersection or pair[1] == intersection

def part1_how_many_assignments_contain_another(lines: list[str]) -> int:
    """Compute how many assignements contain another within a pair per input file."""
    return sum(map(lambda line: does_an_assignment_contain_another(parse_pair(line)), lines))

if __name__ == '__main__':
    with open('puzzle_input_example.txt') as f:
        lines = f.read().strip().split("\n")
        print("Puzzle input example")
        print("Part 1:", part1_how_many_assignments_contain_another(lines))
    with open('puzzle_input.txt') as f:
        lines = f.read().strip().split("\n")
        print("Puzzle input")
        print("Part 1:", part1_how_many_assignments_contain_another(lines))
