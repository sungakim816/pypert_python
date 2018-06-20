class GameStats(object):
    def __init__(self, game_settings):
        """Initialize Statistics"""
        self.game_settings = game_settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ship_life = self.game_settings.ship_life
        self.score = 0


