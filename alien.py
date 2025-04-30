import pygame
from settings import Settings
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edge(self):
        """Return True if alien is at edge of screen."""
        edge = self.screen.get_rect()
        return (self.rect.right >= edge.right) or (self.rect.left <= edge.left)

    def update(self):
        """Move the alien to the right."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x 