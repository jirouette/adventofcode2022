#!/usr/bin/python3
#coding: utf8

START_OF_PACKET_LENGTH = 4
START_OF_MESSAGE_LENGTH = 14

def get_packet_index(sequence: str, packet_size: int = START_OF_PACKET_LENGTH) -> int:
    """Get the index of a packet of a sequence given the size of the packet."""
    for i in range(len(sequence)):
        begin = i
        end = i+packet_size
        if len(set(sequence[begin:end])) == packet_size:
            return end
    return 0

if __name__ == '__main__':
    with open("puzzle_input_example.txt") as f:
        print("Puzzle input example")
        for line in f:
            print("Part 1:", get_packet_index(line.strip()))
            print("Part 2:", get_packet_index(line.strip(), START_OF_MESSAGE_LENGTH))
    with open("puzzle_input.txt") as f:
        print("Puzzle input")
        for line in f:
            print("Part 1:", get_packet_index(line.strip()))
            print("Part 2:", get_packet_index(line.strip(), START_OF_MESSAGE_LENGTH))
