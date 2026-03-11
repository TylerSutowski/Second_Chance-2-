import os
import random

import pygame as pg

from src.states.minigames.minigame import Minigame


class Memory(Minigame):
    """A minigame to test your memory."""

    def __init__(self):
        instructions = (
            "The goal of this minigame is to memorize the 5-character "
            "string. The characters of the string will appear one by one and then disappear after 1 second each. "
            "A text box will pop up and you will have to enter a 5-character "
            "string into it. You win the game if the 5-character "
            "string you entered matches the 5-character string that appeared "
            "on the screen."
        )

        img = "minigame2.jpg"

        super().__init__(
            instructions,
            img=os.path.join("minigames", img)
        )

        # Minigame specific attributes
        self.generated_string = ""
        self.input_string = ""
        self.input_rect = pg.Rect(200, 282, 200, 36)  # Adjusted position to center vertically
        self.input_active = False
        self.font = pg.font.SysFont(None, 36)
        self.display_time = 10  # Time to display the generated string in seconds
        self.display_timer = 0  # Timer to track the display time
        self.is_string_currently_displayed = False
        self.was_string_displayed_yet = False
        self.clock = pg.time.Clock()
        self.char_positions = []
        self.chars_shown = 0
        self.char_timer = 0

    def handle_events(self, events):
        super().handle_events(events)  # To enable pause menu access
        for event in events:
            if event.type == pg.KEYDOWN and self.input_active:
                if event.key == pg.K_RETURN:
                    self.check_win_condition()
                elif event.key == pg.K_BACKSPACE:
                    self.input_string = self.input_string[:-1]
                else:
                    self.input_string += event.unicode

    def update(self, events):
        super().update(events)
        if not self.was_string_displayed_yet and self.countdown_over:
            self.generated_string = self.generate_random_string()
            self.was_string_displayed_yet = True
            self.is_string_currently_displayed = True
            #generate a random position for each character
            self.char_positions = [
                (random.randint(50, self.screen.get_width() - 50),
                random.randint(50, self.screen.get_height() - 50))
                for i in range(5)
            ]
            self.chars_shown = -1
            self.next_char_time = pg.time.get_ticks() + 1000 #1 second for each character

        elif self.is_string_currently_displayed:
            if pg.time.get_ticks() >= self.next_char_time:
                self.chars_shown += 1
                self.next_char_time = pg.time.get_ticks() + 1000
                if self.chars_shown >= 5:
                    self.is_string_currently_displayed = False
                    self.input_active = True

    def draw(self):
        super().draw()  # Draw minigame background

        # Render and display generated string characters one by one
        if self.is_string_currently_displayed and 0 <= self.chars_shown < 5:
            char_surf = self.font.render(self.generated_string[self.chars_shown], True, (255, 255, 255))
            self.screen.blit(char_surf, self.char_positions[self.chars_shown])

        # Draw input box if the generated string has disappeared
        if not self.is_string_currently_displayed and self.was_string_displayed_yet:
            pg.draw.rect(self.screen, (255, 255, 255), self.input_rect, 2)
            input_text_surf = self.font.render(self.input_string, True, (255, 255, 255))
            self.screen.blit(input_text_surf, (self.input_rect.x + 5, self.input_rect.y + 5))

    def generate_random_string(self):
        """Generates a random 5-character string."""
        characters = "abcdefghijklmnopqrstuvwxyz0123456789"
        return ''.join(random.choice(characters) for _ in range(5))

    def check_win_condition(self):
        """Checks if the input string matches the generated string."""
        if self.input_string == self.generated_string:
            self.won = True
            self.win_text = "You remembered the string!"
        else:
            self.won = False