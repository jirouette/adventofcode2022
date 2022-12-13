#!/usr/bin/python3
#coding: utf8

import json

Packet = list[int|list]
Pair = tuple[Packet, Packet]

def parse_pairs(filename: str) -> list[Pair]:
    data = open(filename).read().strip()
    return [tuple([json.loads(l) for l in pair.split("\n")]) for pair in data.split("\n\n")]

def check_pair(p1: Pair, p2: Pair) -> bool:
    if not p1 and p2:
        return True
    if p1 and not p2:
        return False
    if not p1 and not p2:
        return None
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

def count_right_orders(pairs: list[Pair]) -> int:
    return sum([i+1 for i in range(len(pairs)) if check_pair(*pairs[i]) != False])

if __name__ == '__main__':
    print("Puzzle input example")
    filename = "day13/puzzle_input_example.txt"
    pairs = parse_pairs(filename)
    print(count_right_orders(pairs))

    print("Puzzle input")
    filename = "day13/puzzle_input.txt"
    pairs = parse_pairs(filename)
    print(count_right_orders(pairs))
