#!/usr/bin/python3
#coding: utf8

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Directory:
    parent: Optional["Directory"] = field(default=None)
    directories: dict[str, "Directory"] = field(default_factory=lambda: dict())
    files: dict[str, int] = field(default_factory=lambda: dict())

    @property
    def size(self) -> int:
        """Get the size of a directory (including its sub-directories)."""
        return sum(self.files.values()) + sum(map(lambda dir: dir.size, self.directories.values()))
    
    def add_directory(self, name: str, directory: "Directory"):
        """Add a subdirectory"""
        self.directories[name] = directory
    
    def add_file(self, name: str, size: int):
        """Add a file"""
        self.files[name] = size
    
    def get_directories(self) -> list["Directory"]:
        dirs = list(self.directories.values())
        subdirs = [d for dir in dirs for d in dir.get_directories()]
        return dirs+subdirs
    
def parse_terminal_output(data: str) -> Directory:
    root = Directory()
    working_directory = root
    for line in data.split("\n"):
        line = line.strip().split()
        match line[0]:
            case "$":
                if line[1] != "cd":
                    continue # ignoring ls
                match line[2]:
                    case "/":
                        working_directory = root
                    case "..":
                        working_directory = working_directory.parent
                    case dirname:
                        working_directory = working_directory.directories[dirname]
            case "dir":
                # Create a new Directory
                working_directory.add_directory(line[1], Directory(working_directory))
            case size:
                # Create a new file with its size
                working_directory.add_file(line[1], int(size))
    return root

def part1_get_sum_of_directories_of_a_size(dir: Directory, size: int = 100_000) -> int:
    dir_size = dir.size
    if dir_size > size:
        dir_size = 0
    return dir_size + sum(map(lambda dir: part1_get_sum_of_directories_of_a_size(dir, size), dir.directories.values()))

def part2_find_smallest_directory_to_remove(root: Directory, total_disk_space: int = 70_000_000, free_space_needed: int = 30_000_000) -> int:
    smallest_size_needed = free_space_needed - (total_disk_space - root.size)
    if smallest_size_needed <= 0:
        return 0
    directories = root.get_directories()
    directories.sort(key=lambda dir: dir.size)
    for dir in directories:
        size = dir.size
        if size >= smallest_size_needed:
            return size
    return root.size

if __name__ == '__main__':
    with open('day7/puzzle_input_example.txt') as f:
        term_output = f.read().strip()
        root = parse_terminal_output(term_output)
        print("Puzzle input example")
        print("Part 1:", part1_get_sum_of_directories_of_a_size(root))
        print("Part 2:", part2_find_smallest_directory_to_remove(root))
    with open('day7/puzzle_input.txt') as f:
        term_output = f.read().strip()
        root = parse_terminal_output(term_output)
        print("Puzzle input example")
        print("Part 1:", part1_get_sum_of_directories_of_a_size(root))
        print("Part 2:", part2_find_smallest_directory_to_remove(root))

# Well, a lot of optimisation is possible (caching dir size for example)