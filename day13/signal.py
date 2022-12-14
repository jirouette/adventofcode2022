#!/usr/bin/python3
#coding: utf8

import json
from functools import cmp_to_key

Packet = int|list["Packet"]

def parse_packets(filename: str) -> list[Packet]:
    data = open(filename).read().strip()
    return [json.loads(l) for l in data.replace("\n\n", "\n").split("\n")]

def check_pair(p1: Packet, p2: Packet) -> None|bool:
    if not p1 and p2:
        return True
    if p1 and not p2:
        return False
    if not p1 and not p2:
        return None
    p1 = p1.copy()
    p2 = p2.copy()
    left = p1.pop(0)
    right = p2.pop(0)
    if type(left) is int and type(right) is int:
        if left == right:
            return check_pair(p1, p2)
        return left < right
    if type(left) is int:
        left = [left]
    if type(right) is int:
        right = [right]
    result = check_pair(left, right)
    if result is not None:
        return result
    return check_pair(p1, p2)

def count_right_orders(pairs: list[tuple[Packet, Packet]]) -> int:
    return sum([i+1 for i in range(len(pairs)) if check_pair(*pairs[i]) != False])

def sort_packets(packets: list[Packet]) -> list[Packet]:
    return sorted(packets, key=cmp_to_key(lambda p1, p2: {True: -1, None: 0, False: 1}[check_pair(p1, p2)]))

def decoder_key(packets: list[Packet], p1: Packet, p2: Packet) -> int:
    return (packets.index(p1)+1) * (packets.index(p2)+1)

DIVIDER_PACKET: list[Packet] = [[[2]], [[6]]]

if __name__ == '__main__':
    print("Puzzle input example")
    filename = "day13/puzzle_input_example.txt"
    pairs = parse_packets(filename)
    print(count_right_orders([(p1, p2) for p1, p2 in zip(pairs[::2], pairs[1::2])]))
    print(decoder_key(sort_packets(pairs+DIVIDER_PACKET), *DIVIDER_PACKET))

    print("Puzzle input")
    filename = "day13/puzzle_input.txt"
    pairs = parse_packets(filename)
    print(count_right_orders([(p1, p2) for p1, p2 in zip(pairs[::2], pairs[1::2])]))
    print(decoder_key(sort_packets(pairs+DIVIDER_PACKET), *DIVIDER_PACKET))
