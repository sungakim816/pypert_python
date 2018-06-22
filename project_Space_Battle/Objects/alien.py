import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, game_settings, screen):
        """A class to represent aliens"""
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        # Load the ship image and get its rect
        self.image = pygame.image.load("C:/Users/Sunga/Documents/gitHubRepo/pypert_python/project_Space_Battle/Files/alien1.jpg")
        self.rect = self.image.get_rect()  # Get Alien  Rectangular Coordinates
        self.screen_rect = screen.get_rect()  # Get Screen Rectangular Coordinates

        # Start each new alien at the bottom center of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store Alien's Exact Position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move Alien Right"""
        self.x += (self.game_settings.alien_speed_factor * self.game_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if  alien is at edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
