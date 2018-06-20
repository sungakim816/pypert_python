class Settings(object):
    """A class to store all settings for Battle Spacer"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 640
        self.bg_color = (255, 255, 255)
        # Ship Settings
        self.ship_speed_factor = 0
        self.ship_life = 3
        # Bullet Settings
        self.bullet_speed_factor = 0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        # Alien Settings
        self.alien_speed_factor = 0
        self.fleet_drop_speed = 0
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 0
        self.speedup_scale = 1.1
        self.alien_points = 10
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        self.alien_points += 5