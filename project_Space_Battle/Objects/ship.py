import pygame


class Ship(object):

    def __init__(self, screen, game_options):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.game_options = game_options
        # Load the ship image and get its rect
        self.image = pygame.image.load("Files/rocket1.jpg")
        self.rect = self.image.get_rect()  # Rectangular Coordinates of the ship
        self.screen_rect = screen.get_rect()  # Rectangular Coordinates of the Screen

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.ship_x = float(self.rect.centerx)
        self.ship_y = float(self.rect.bottom)
        # Movement Flag
        self.is_moving_right = self.is_moving_left = self.is_moving_down = self.is_moving_up = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        if self.is_moving_right and self.rect.right <= self.screen_rect.right:
            self.ship_x += self.game_options.ship_speed_factor
        elif self.is_moving_left and self.rect.left >= self.screen_rect.left:
            self.ship_x -= self.game_options.ship_speed_factor
        elif self.is_moving_up and self.rect.top != self.screen_rect.centery:
            self.ship_y -= self.game_options.ship_speed_factor
        elif self.is_moving_down and self.rect.bottom != self.screen_rect.bottom:
            self.ship_y += self.game_options.ship_speed_factor
        else:
            return

        self.rect.centerx = self.ship_x
        self.rect.bottom = self.ship_y

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx