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
    observers: list[Observer]
    X: int = 1
    cycle: int = 0

    def execute(self):
        for instruction, args in self.instructions:
            self.new_cycle()
            match instruction:
                case Instruction.ADDX:
                    self.addx(int(args[0]))
    
    def new_cycle(self, nb_cycle = 1):
        for _ in range(nb_cycle):
            self.cycle += 1
            for observer in self.observers:
                observer(self.cycle, self.X)
    
    def addx(self, amount: int):
        # take whole 2 cycle to execute, so increment the cycle and call the observer
        self.new_cycle()
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

    def observe(self, cycle: int, X: int):
        if cycle not in [20, 60, 100, 140, 180, 220]:
            return
        self.signal_strength += cycle * X
    
    def get_signal_strength(self) -> int:
        return self.signal_strength

SCREEN_ROW_WIDTH = 40
class CRT:
    pos = 0
    screen = ""
    current_sprite_position = 0

    def observe(self, _: int, X: int):
        self.current_sprite_position = X
        self.draw()
    
    def has_to_draw(self) -> bool:
        return self.pos >= self.current_sprite_position-1 and self.pos <= self.current_sprite_position+1
    
    def check_screen_position(self):
        if self.pos < SCREEN_ROW_WIDTH:
            return
        self.pos = 0
        self.screen += "\n"

    def draw(self):
        self.check_screen_position()
        self.screen += "#" if self.has_to_draw() else "."
        self.pos += 1
    
    def display(self):
        print(self.screen)

def puzzle(filename: str):
    instructions = parse_instructions_from_file(filename)
    part1 = Part1Observer()
    part2 = CRT()
    cpu = CPU(instructions, observers=[part1.observe, part2.observe])
    cpu.execute()
    print("Part 1", part1.get_signal_strength())
    print("Part 2")
    part2.display()

if __name__ == '__main__':
    print("Puzzle input example")
    puzzle("day10/puzzle_input_example.txt")

    print("Puzzle input")
    puzzle("day10/puzzle_input.txt")
