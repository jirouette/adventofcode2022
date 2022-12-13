#!/usr/bin/python3
#coding: utf8

from dataclasses import dataclass

Position = int

@dataclass
class Map:
    tiles: str
    width: int
    height: int

    def get_starting_position(self) -> Position:
        return self.tiles.index("S")
    
    def get_ending_position(self) -> Position:
        return self.tiles.index("E")
    
    def get_tile(self, pos: Position) -> Position:
        if pos < 0:
            return ""
        return self.tiles[pos]
    
    def get_top_position_of(self, pos: Position) -> Position:
        if pos < self.width:
            return -1
        return pos - self.width
    
    def get_bottom_position_of(self, pos: Position) -> Position:
        if pos > self.width*self.height:
            return -1
        return pos + self.width
    
    def get_left_position_of(self, pos: Position) -> Position:
        if pos % self.width == 0:
            return -1
        return pos - 1
    
    def get_right_position_of(self, pos: Position) -> Position:
        if (pos % self.width) == (self.width-1):
            return -1
        return pos + 1
    
    def display(self):
        for i in range(self.height):
            print(self.tiles[i*self.width:(i*self.width)+self.width])
    
    def is_reachable(self, origin: Position, target: Position) -> bool:
        try:
            return (ord(self.tiles[target].replace("E", "z")) - ord(self.tiles[origin].replace("S", "a"))) <= 1
        except IndexError:
            return False

def parse_map(filename: str) -> Map:
    data = open(filename).read().strip()
    return Map(data.replace("\n", ""), data.index("\n"), len(data.split("\n")))

def get_fewest_steps(map: Map) -> int:
    adjacents = [(map.get_starting_position(), 0)]
    reached_positions = list()
    while adjacents:
        position, score = adjacents.pop(0)
        if position in reached_positions:
            continue
        reached_positions.append(position)
        if position == map.get_ending_position():
            return score
        adjacents_positions = [
            map.get_top_position_of(position),
            map.get_bottom_position_of(position),
            map.get_left_position_of(position),
            map.get_right_position_of(position)
        ]
        adjacents += [(p, score+1) for p in adjacents_positions if p >= 0 and map.is_reachable(position, p)]
    return 0

if __name__ == '__main__':
    print("Puzzle input example")
    filename = "day12/puzzle_input_example.txt"
    map = parse_map(filename)
    print(get_fewest_steps(map))

    print("Puzzle input")
    filename = "day12/puzzle_input.txt"
    map = parse_map(filename)
    print(get_fewest_steps(map))