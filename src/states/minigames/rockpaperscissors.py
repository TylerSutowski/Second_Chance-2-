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
            "The goal of this minigame is to beat the computer at Rock, Paper, Scissors. \n"
            "Choose your move and the computer will randomly choose its move. \n"
            "Are you ready?"
        )


        img = "rps.jpg"
        super().__init__(
            instructions,
            img=os.path.join("minigames", img)
            )

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

    def determine_winner(self):
        # if tie, return and let player choose again
        if self.player_choice == self.computer_choice:
            self.results = f"It's a tie! Try again."
            self.player_choice = None
            return
        
        # new comparison statements for RPS
        elif (self.player_choice == "rock" and self.computer_choice == "scissors") or \
             (self.player_choice == "paper" and self.computer_choice == "rock") or \
             (self.player_choice == "scissors" and self.computer_choice == "paper"):
            self.results = f"You won! The computer chose {self.computer_choice}."
            self.won = True

        else:
            self.results = f"You lost!"
            self.won = False
        
        self.finished = True
        # result stay on screen for debugging gotta make sure it works
        self.result_timer = Timer(5000)

    # update function displays the results of the game
    def update(self, events):
        super().update(events)

        self.result_surface = self.get_text_surface(self.results, "white", 36)


    # put user results in green text and enemy results in red text (add pics if done before 8 idk tho)
    def draw(self):
        super().draw()

        # display instructions
        instructions = self.get_text_surface(
            "Press R for Rock, P for Paper, S for Scissors", "white", 24)
        self.screen.blit(instructions, (250, 100))

        if self.player_choice:
            player_text = self.get_text_surface(f"You chose {self.player_choice}", "green", 24)

            self.screen.blit(player_text, (250, 300))

            if self.computer_choice:
                computer_text = self.get_text_surface(f"Computer chose {self.computer_choice}", "red", 24)

                self.screen.blit(computer_text, (250, 450))

        # self.screen.blit(self.result_surface, (250, 200))
        """A minigame to play RPS with the computer"""
