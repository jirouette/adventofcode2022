#!/usr/bin/python3
#coding: utf8

from dataclasses import dataclass


Crate = list[str]
BLANK = " "*5

@dataclass
class Order:
    origin_stack: int = 0
    target_stack: int = 0
    number_of_moves: int = 0

def parse_initial_stacks(data: str) -> list[Crate]:
    """Parse the initial stacks from the input."""
    lines = data.split("\n")
    crates = [list() for _ in range(int(lines[-1].split()[-1]))]
    for line in lines[::-1][1:]:
        line = f" {line} " # adding spaces to detect blanks in the beginning and in the end
        while BLANK in line:
            line = line.replace(BLANK, " [-] ", 1)
        supplies = line.split()
        for i in range(len(crates)):
            try:
                supply = supplies[i].replace("[", "").replace("]", "")
                if supply == "-":
                    continue # no supply
                crates[i].insert(0, supply)
            except IndexError:
                continue # no supply
    return crates

def parse_orders(data: str) -> list[Order]:
    """Parse the orders to modify the stacks from the input."""
    lines = data.strip().split("\n")
    orders = list()
    for line in lines:
        line = [int(x) for x in line.replace("move", "").replace("from", "").replace("to", "").split()]
        orders.append(Order(origin_stack=line[1], target_stack=line[2], number_of_moves=line[0]))
    return orders

def apply_orders(stacks: list[Crate], orders: list[Order]) -> list[Crate]:
    """Apply a list of orders to a list of crates."""
    for order in orders:
        for _ in range(order.number_of_moves):
            supply = stacks[order.origin_stack - 1].pop(0)
            stacks[order.target_stack - 1].insert(0, supply)
    return stacks

def get_final_top_word(stacks: list[Crate]) -> str:
    """Get the final word from a list of crates."""
    return "".join([crate.pop(0) for crate in stacks])

def part1(data: str) -> str:
    stacks_data, orders_data = data.split("\n\n")
    stacks: list[Crate] = parse_initial_stacks(stacks_data)
    orders: list[Order] = parse_orders(orders_data)
    orders = apply_orders(stacks, orders)
    return get_final_top_word(stacks)

if __name__ == '__main__':
    with open("day5/puzzle_input_example.txt") as f:
        data = f.read()
        print("Puzzle input example")
        print("Part 1:", part1(data))
    with open("day5/puzzle_input.txt") as f:
        data = f.read()
        print("Puzzle input")
        print("Part 1:", part1(data))