#!/usr/bin/python3
#coding: utf8

from dataclasses import dataclass
from enum import Enum
from typing import Callable


class Instruction(Enum):
    NOOP = "noop"
    ADDX = "addx"

Args = list[str]
InstructionList = list[tuple[Instruction, Args]]
Observer = Callable[[int, int], None]

@dataclass
class CPU:
    instructions: InstructionList
    observer: Observer
    X: int = 1
    cycle: int = 0

    def execute(self):
        for instruction, args in self.instructions:
            self.cycle += 1
            self.observer(self.cycle, self.X)
            match instruction:
                case Instruction.ADDX:
                    self.addx(int(args[0]))
    
    def addx(self, amount: int):
        # take whole 2 cycle to execute, so increment the cycle and call the observer
        self.cycle += 1
        self.observer(self.cycle, self.X)
        self.X += amount

def parse_instructions_from_file(filename: str) -> InstructionList:
    instruction_list: InstructionList = list()
    with open(filename) as f:
        for line in f:
            command = line.split()
            instruction_list.append((Instruction(command[0]), command[1:]))
    return instruction_list

class Part1Observer:
    signal_strength: int = 0

    def observer(self, cycle: int, X: int):
        if cycle not in [20, 60, 100, 140, 180, 220]:
            return
        self.signal_strength += cycle * X
    
    def get_signal_strength(self) -> int:
        return self.signal_strength

def part1(filename: str):
    instructions = parse_instructions_from_file(filename)
    observer = Part1Observer()
    cpu = CPU(instructions, observer.observer)
    cpu.execute()
    print("Part 1", observer.get_signal_strength())

if __name__ == '__main__':
    print("Puzzle input example")
    part1("day10/puzzle_input_example.txt")
    print("Puzzle input")
    part1("day10/puzzle_input.txt")

