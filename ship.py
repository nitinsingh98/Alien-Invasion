import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_game):
        # Initialize the ship and set its starting position.
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('ship.bmp')
        # self.image = pygame.transform.scale(self.image, (50, 50)) #Resize to 50x50 pixels.
        self.rect = self.image.get_rect()
        self.speed = ai_game.settings.ship_speed

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # Movement flag, starts with when object not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > self.screen_rect.left: # or left > 0
            self.x -= self.speed
        # Update rect object from self.x.
        self.rect.x = self.x
    
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image,self.rect)