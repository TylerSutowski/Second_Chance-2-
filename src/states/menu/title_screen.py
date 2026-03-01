import pygame as pg
import requests
import random
import src.states.menu.menus as menus
from .menus import StartMenu
from .menus import UsernamePrompt
from ..state import State


class TitleScreen(State):
    """State for the title screen."""

    def __init__(self):
        super().__init__("background.png")

        self.title_logo = pg.image.load("assets/backgrounds/title_logo.png")
        self.title_logo = pg.transform.scale(self.title_logo, (450, 250))
        # Load background music
        pg.mixer.music.load('assets/music/titlescreenmusic.mp3')
        # Set initial volume
        self.volume = menus.volume  # Initial volume level (between 0 and 1)
        pg.mixer.music.set_volume(menus.volume)
        pg.mixer.music.play(-1)  # Start playing background music on a loop

    def handle_events(self, events: list[pg.event.Event]):
        for event in events:
            if event.type != pg.KEYDOWN:
                return
            if event.key == pg.K_RETURN:
                if self.game.username == "":
                    self.manager.set_state(UsernamePrompt)
                else:
                    self.manager.set_state(StartMenu)

    def draw(self):
        title_list = ["New in Temple News: Owls announce full "
        "schedule for 2026 season", 
                      "New in Temple News: Senior student activist "
                      "faces federal charges",
                      "New in Temple News: Student acts as ambassador "
                      "for Urban Outfitters",
                      "New in Temple News: Kenyatta focuses on "
                      "affordability ahead of election", 
                      "New in Temple News: High costs of living strain "
                      "student lunch spending", 
                      "New in Temple News: Philly style owner builds "
                      "community through music"]
        s = "hello"
        super().draw()
        self.screen.blit(
            pg.font.Font(None, 36).render("Press 'Enter' to start", True, "black"),
            (self.screen.get_width() / 2, self.screen.get_height() - 100)
        )
        self.screen.blit(
        pg.font.Font(None, 36).render(random.choice(title_list), True, "black"),
        (self.screen.get_width() / 20, self.screen.get_height() - 600)
        )
        self.screen.blit(self.title_logo, (170, 150))

   
