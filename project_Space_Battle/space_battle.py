import pygame
from pygame.sprite import Group
from Objects.settings import Settings
from Objects.ship import Ship
from Objects.game_stats import GameStats
from Objects.button import Button
from Objects.scoreboard import Scoreboard
import Objects.game_functions as space_event


def run_game():
    """Initialize game and created a screen object"""
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption('Space Battle')
    # Create Play Button
    play_button = Button(game_settings, screen, msg="Start")
    # Create an instance to store game statistics
    stats = GameStats(game_settings)
    score = Scoreboard(game_settings, screen, stats)
    # Make a ship
    ship = Ship(screen, game_settings)
    # Make a group to store all the bullets in
    bullets = Group()  # Group of bullet objects
    # Make an alien fleet
    aliens = Group()
    space_event.create_alien_fleet(game_settings, screen, ship, aliens)
    # Start the main loop for the game..
    while True:
        # Watch for keyboard and mousse events.
        space_event.check_events(game_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update_position()
            space_event.update_bullets(game_settings, stats, score, screen, ship, aliens, bullets)
            space_event.update_aliens(game_settings, stats, screen, ship, aliens, bullets)

        space_event.update_screen(game_settings, stats, score, screen, ship, aliens, bullets, play_button)

        
if __name__ == "__main__":
    run_game()
