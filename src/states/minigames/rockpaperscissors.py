import collections
import os
import random

import pygame as pg

import src.utils.spritesheet as spritesheet
from src.states.minigames.minigame import Minigame
from src.states.state import State
from src.utils.timer import Timer

pg.mixer.init()

class RPS(Minigame):
    """A minigame to play RPS with the computer"""

    def __init__(self):
        instructions = (
            "The goal of this minigame is to beat the computer at RPS. \n"
            "The computer will secretly choose Rock, Paper, or Scissors, your goal is to win at RPS"
        )


        super().__init__(
            instructions,
            img=None)

        self.options = ["rock", "paper", "scissors"]
        self.player_choice = None
        self.computer_choice = None

        self.results = ""
        self.result_surface = pg.Surface((0, 0))

        self.finished = False

    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and not self.finished:
                if event.key == pg.K_r:
                    self.player_choice = "rock"
                elif event.key == pg.K_p:
                    self.player_choice = "paper"
                elif event.key == pg.K_s:
                    self.player_choice = "scissors"

                if self.player_choice is not None:
                    self.computer_choice = random.choice(self.options)
                    self.determine_winner()
                    self.finished = True

    def determine_winner(self):
        if self.player_choice == self.computer_choice:
            self.results = f"It's a tie! Try again."
            self.player_choice = None
            return
        
        # new comparison statements for RPS
        elif (self.player_choice == "rock" and self.computer_choice == "scissors") or \
             (self.player_choice == "paper" and self.computer_choice == "rock") or \
             (self.player_choice == "scissors" and self.computer_choice == "paper"):
            print("You won!")

        else:
            self.results = f"You lost!"