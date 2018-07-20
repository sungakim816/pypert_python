import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, game_settings, screen, ship):
        """Create bullet objects at ship's current position"""
        super().__init__()  # Initialize Parent Class 'Sprite'
        self.screen = screen
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.bullet_y = float(self.rect.y)
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        self.bullet_y -= self.speed_factor
        # Update Bullet Position
        self.rect.y = self.bullet_y

    def draw_bullet(self):
        """Render the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
