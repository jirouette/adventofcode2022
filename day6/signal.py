#!/usr/bin/python3
#coding: utf8

START_OF_PACKET_LENGHT = 4

def get_start_of_packet_index(sequence: str) -> int:
    """Get the index of the start-of-packet of a sequence."""
    for i in range(len(sequence)):
        begin = i
        end = i+START_OF_PACKET_LENGHT
        if len(set(sequence[begin:end])) == START_OF_PACKET_LENGHT:
            return end
    return 0

if __name__ == '__main__':
    with open("puzzle_input_example.txt") as f:
        print("Puzzle input example")
        for line in f:
            print("Part 1:", get_start_of_packet_index(line.strip()))
    with open("puzzle_input.txt") as f:
        print("Puzzle input")
        for line in f:
            print("Part 1:", get_start_of_packet_index(line.strip()))
