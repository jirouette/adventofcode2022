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

class Strategy(Enum):
    """Outcome we want to get for a game."""
    LOSS = "X"
    DRAW = "Y"
    WIN = "Z"

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

def strategy_win(opponent_play: OpponentPlay) -> PlayerPlay:
    """Best play from an opponent play."""
    match opponent_play:
        case OpponentPlay.ROCK:
            return PlayerPlay.PAPER
        case OpponentPlay.PAPER:
            return PlayerPlay.SCISSORS
        case OpponentPlay.SCISSORS:
            return PlayerPlay.ROCK
    return PlayerPlay.ROCK # should not happen

def strategy_draw(opponent_play: OpponentPlay) -> PlayerPlay:
    """Play from an opponent play to get a draw."""
    match opponent_play:
        case OpponentPlay.ROCK:
            return PlayerPlay.ROCK
        case OpponentPlay.PAPER:
            return PlayerPlay.PAPER
        case OpponentPlay.SCISSORS:
            return PlayerPlay.SCISSORS
    return PlayerPlay.PAPER # should not happen

def strategy_loss(opponent_play: OpponentPlay) -> PlayerPlay:
    """Worst play from an opponent play."""
    match opponent_play:
        case OpponentPlay.ROCK:
            return PlayerPlay.SCISSORS
        case OpponentPlay.PAPER:
            return PlayerPlay.ROCK
        case OpponentPlay.SCISSORS:
            return PlayerPlay.PAPER
    return PlayerPlay.SCISSORS # should not happen

def compute_score(play: PlayerPlay, outcome: Outcome):
    """Get the total score earned of a game."""
    return play_score(play) + outcome.value

def part1_parse_game(line: str) -> int:
    """Part 1 : Parse a game, play it, and returns its earned score."""
    opponent_play, player_play = line.strip().split() # Supposing format is "A Z"
    opponent_play = OpponentPlay(opponent_play)
    player_play = PlayerPlay(player_play)
    outcome = compute_outcome(player_play, opponent_play)
    return compute_score(player_play, outcome)

def part2_parse_game(line: str) -> int:
    """Part 2 : Parse a game, play it, and returns its earned score."""
    opponent_play, strategy = line.strip().split() # Supposing format is "A Z"
    opponent_play = OpponentPlay(opponent_play)
    strategy = Strategy(strategy)
    score = 0
    match strategy:
        case Strategy.WIN:
            player_play = strategy_win(opponent_play)
            score = Outcome.WIN.value
        case Strategy.DRAW:
            player_play = strategy_draw(opponent_play)
            score = Outcome.DRAW.value
        case Strategy.LOSS:
            player_play = strategy_loss(opponent_play)
            score = Outcome.LOSS.value
    return score + play_score(player_play)

if __name__ == '__main__':
    with open('puzzle_input_example.txt') as f:
        lines = f.read().split("\n")
        score_part1 = sum(map(lambda line: part1_parse_game(line), lines))
        score_part2 = sum(map(lambda line: part2_parse_game(line), lines))
        print("Puzzle input example")
        print("Part 1:", score_part1)
        print("Part 2:", score_part2)
    with open('puzzle_input.txt') as f:
        lines = f.read().split("\n")
        score_part1 = sum(map(lambda line: part1_parse_game(line), lines))
        score_part2 = sum(map(lambda line: part2_parse_game(line), lines))
        print("Puzzle input")
        print("Part 1:", score_part1)
        print("Part 2:", score_part2)
