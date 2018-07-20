class GameStats(object):

    def __init__(self, game_settings):
        """Initialize Statistics"""
        self.game_settings = game_settings
        self.game_active = False
        # High Score Should never be reset 
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ship_life = self.game_settings.ship_life
        self.score = 0
        self.level = 1
        self.game_settings.initialize_dynamic_settings()