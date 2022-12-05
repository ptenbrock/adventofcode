import argparse
from pathlib import Path
from typing import List


class RPSAction:
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    @staticmethod
    def evaluate_action(action):
        if action == RPSAction.ROCK:
            return 1
        elif action == RPSAction.PAPER:
            return 2
        elif action == RPSAction.SCISSORS:
            return 3


class RPSResult:
    WIN = "win"
    DRAW = "draw"
    LOSS = "loss"

    @staticmethod
    def evaluate_result(result):
        if result == RPSResult.WIN:
            return 6
        elif result == RPSResult.DRAW:
            return 3
        elif result == RPSResult.LOSS:
            return 0


class RPSRound:
    opponent_action_converter = {
        "A": RPSAction.ROCK,
        "B": RPSAction.PAPER,
        "C": RPSAction.SCISSORS,
    }
    own_action_converter = {
        "X": RPSAction.ROCK,
        "Y": RPSAction.PAPER,
        "Z": RPSAction.SCISSORS,
    }

    def __init__(self, chosen_actions: str):
        self.chosen_actions = chosen_actions

    @staticmethod
    def determine_result(opponent_action, own_action):
        if opponent_action == own_action:
            return RPSResult.DRAW
        elif opponent_action == RPSAction.ROCK:
            if own_action == RPSAction.PAPER:
                return RPSResult.WIN
            elif own_action == RPSAction.SCISSORS:
                return RPSResult.LOSS
        elif opponent_action == RPSAction.PAPER:
            if own_action == RPSAction.ROCK:
                return RPSResult.LOSS
            elif own_action == RPSAction.SCISSORS:
                return RPSResult.WIN
        elif opponent_action == RPSAction.SCISSORS:
            if own_action == RPSAction.ROCK:
                return RPSResult.WIN
            elif own_action == RPSAction.PAPER:
                return RPSResult.LOSS

    @property
    def score(self):
        chosen_action_texts = self.chosen_actions.split()
        opponent_action = self.opponent_action_converter[chosen_action_texts[0]]
        own_action = self.own_action_converter[chosen_action_texts[1]]
        result = self.determine_result(opponent_action, own_action)
        score = RPSAction.evaluate_action(own_action) + RPSResult.evaluate_result(
            result
        )
        return score

    def __str__(self):
        return self.chosen_actions


def parse_input_file(input_filename: str) -> List[RPSRound]:
    input_filepath = Path(__file__).parent / input_filename
    with input_filepath.open("r") as f:
        input_text = f.read()
        input_text_per_round = input_text.split("\n")
        rps_rounds = [
            RPSRound(chosen_action_text) for chosen_action_text in input_text_per_round
        ]
        return rps_rounds


def main():
    parser = argparse.ArgumentParser(
        description="Calculate the total score for the rock paper scissors game"
    )
    parser.add_argument(
        "-i",
        "--input_filename",
        type=str,
        default="sample_input.txt",
        help="File name containing the strategy guide (located in same folder as day2.py)",
    )
    args = parser.parse_args()

    rps_rounds = parse_input_file(args.input_filename)
    score_per_round = [round.score for round in rps_rounds]
    total_score = sum(score_per_round)
    print(score_per_round)
    print(f"Total score for all rounds = {total_score}")


if __name__ == "__main__":
    main()
