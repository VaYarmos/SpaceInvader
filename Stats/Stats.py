import pygame
import json
import os


class Stats:
    """"""

    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('Score/high_score.json', 'r') as file:
            self.high_score = json.load(file)["High Score"]

    def reset_stats(self):
        self.guns_left = 2
        self.score = 0


if __name__ == "__main__":
    pass
