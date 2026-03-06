import pygame as pg
import webbrowser
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
        link_color = (0, 0, 0)

        title_list = ["Click Here for all the latest Temple U news!"]
    
        s = random.choice(title_list)
   

        super().draw()
        
        rect = self.screen.blit(
        pg.font.Font(None, 36).render(s, True, link_color, "white"),
        (10, 10)
        )

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = event.pos
                if rect.collidepoint(pos):
                    webbrowser.open("https://temple-news.com/")
            if rect.collidepoint(pg.mouse.get_pos()):
                link_color = (70, 29, 219)
            else:
                link_color = (0, 0, 0)

        self.screen.blit(
            pg.font.Font(None, 36).render("Press 'Enter' to start", True, "black"),
            (self.screen.get_width() / 2, self.screen.get_height() - 100)
        )
        self.screen.blit(self.title_logo, (170, 150))

   
