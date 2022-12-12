#!/usr/bin/python3
#coding: utf8

from dataclasses import dataclass
import math
from typing import TypedDict

import yaml

MonkeyDict = TypedDict("MonkeyDict", {
    "Starting items": str,
    "Operation": str,
    "Test": str,
    "If true": str,
    "If false": str
})

class MonkeyHasNoItemException(Exception):
    pass

@dataclass
class Monkey:
    items: list[int]
    test: int # always "divisible by" this value
    operation: list[str] # operand1 operator operand2
    target_if_true: int # monkey targeted if true
    target_if_false: int # monkey target if false
    thrown_item: int = 0
    nb_times_inspection: int = 0

    def add_item(self, item: int):
        self.items.append(item)
    
    def inspect(self, relief: bool = True, max_item: int = 0) -> int:
        if not self.items:
            raise MonkeyHasNoItemException()
        self.nb_times_inspection += 1
        item = self.items.pop(0)
        match self.operation:
            case "old", "*", "old":
                item *= item
            case "old", "+", "old":
                item += item
            case "old", "+", operand:
                item += int(operand)
            case "old", "*", operand:
                item *= int(operand)
            case operand, "+", "old":
                item += int(operand)
            case operand, "*", "old":
                item *= int(operand)

        self.thrown_item = item
        if relief:
            self.thrown_item = math.floor(item / 3)
        if max_item:
            self.thrown_item %= max_item
        return self.thrown_item
    
    def throw(self) -> int:
        return self.target_if_true if self.thrown_item % self.test == 0 else self.target_if_false

def parse_monkey(data: MonkeyDict) -> Monkey:
    ...
    return Monkey(
        items=[int(i) for i in str(data["Starting items"]).split(", ")],
        test=int(data["Test"].replace("divisible by ", "")),
        operation=data["Operation"].replace("new = ", "").split(),
        target_if_true=int(data["If true"].replace("throw to monkey ", "")),
        target_if_false=int(data["If false"].replace("throw to monkey ", ""))
    )

def parse_config(filename: str) -> list[Monkey]:
    document = open(filename).read().replace("  If", "If")
    data = yaml.load(document, Loader=yaml.SafeLoader)
    return [parse_monkey(data[f"Monkey {i}"]) for i in range(len(data))] # make sure it is correctly sorted

def round(monkeys: list[Monkey], relief: bool = True):
    lcm = math.lcm(*[monkey.test for monkey in monkeys])
    for monkey in monkeys:
        try:
            while True:
                monkey.inspect(relief=relief, max_item=lcm)
                monkeys[monkey.throw()].add_item(monkey.thrown_item)
        except MonkeyHasNoItemException:
            continue

def compute_monkey_business_level(filename: str, nb_rounds: int = 20, relief: bool = True) -> int:
    monkeys = parse_config(filename)
    for _ in range(nb_rounds):
        round(monkeys, relief=relief)
    return math.prod(sorted(map(lambda monkey: monkey.nb_times_inspection, monkeys))[-2:])

if __name__ == '__main__':
    print("Puzzle input example")
    filename = "day11/puzzle_input_example.txt"
    print("Part 1:", compute_monkey_business_level(filename))
    print("Part 2:", compute_monkey_business_level(filename, nb_rounds=10_000, relief=False))
    print("Puzzle input")
    filename = "day11/puzzle_input.txt"
    print("Part 1:", compute_monkey_business_level(filename))
    print("Part 2:", compute_monkey_business_level(filename, nb_rounds=10_000, relief=False))
    