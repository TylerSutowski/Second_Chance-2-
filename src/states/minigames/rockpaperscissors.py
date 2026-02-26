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
            "The goal of this minigame is to beat the computer at RPS. "
            "The computer will secretly choose 1, 2 or 3, your goal is to win at RPS"
        )


        img = "RPSbg.jpg"


        super().__init__(
            instructions,
            img=os.path.join("minigames", img)
        )
