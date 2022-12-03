#!/usr/bin/python3
#coding: utf8

from enum import Enum

class OpponentPlay(Enum):
    """Play an opponent may do."""
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

class PlayerPlay(Enum):
    """Play a player may do."""
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"

class Outcome(Enum):
    """Outcome of a game associated with their score."""
    LOSS = 0
    DRAW = 3
    WIN = 6

def play_score(play: PlayerPlay) -> int:
    """Get the score of a play."""
    match play:
        case PlayerPlay.ROCK:
            return 1
        case PlayerPlay.PAPER:
            return 2
        case PlayerPlay.SCISSORS:
            return 3
    return 0

def compute_outcome(play: PlayerPlay, opponent_play: OpponentPlay) -> Outcome:
    """Decide the outcome of a game."""
    match play:
        case PlayerPlay.ROCK:
            match opponent_play:
                case OpponentPlay.ROCK:
                    return Outcome.DRAW
                case OpponentPlay.PAPER:
                    return Outcome.LOSS
                case OpponentPlay.SCISSORS:
                    return Outcome.WIN
        case PlayerPlay.PAPER:
            match opponent_play:
                case OpponentPlay.ROCK:
                    return Outcome.WIN
                case OpponentPlay.PAPER:
                    return Outcome.DRAW
                case OpponentPlay.SCISSORS:
                    return Outcome.LOSS
        case PlayerPlay.SCISSORS:
            match opponent_play:
                case OpponentPlay.ROCK:
                    return Outcome.LOSS
                case OpponentPlay.PAPER:
                    return Outcome.WIN
                case OpponentPlay.SCISSORS:
                    return Outcome.DRAW
    return Outcome.DRAW

def compute_score(play: PlayerPlay, outcome: Outcome):
    """Get the total score earned of a game."""
    return play_score(play) + outcome.value

def parse_game(line: str) -> int:
    """Parse a game, play it, and returns its earned score."""
    opponent_play, player_play = line.strip().split() # Supposing format is "A Z"
    opponent_play = OpponentPlay(opponent_play)
    player_play = PlayerPlay(player_play)
    outcome = compute_outcome(player_play, opponent_play)
    return compute_score(player_play, outcome)

if __name__ == '__main__':
    with open('puzzle_input_example.txt') as f:
        score = sum(map(lambda line: parse_game(line), f))
        print("Puzzle input example")
        print("Part 1:", score)
    with open('puzzle_input.txt') as f:
        score = sum(map(lambda line: parse_game(line), f))
        print("Puzzle input")
        print("Part 1:", score)
