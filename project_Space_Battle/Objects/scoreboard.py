import pygame
import pygame.sysfont


class Scoreboard(object):
    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        self.text_color = (30, 30 ,30)
        self.font = pygame.sysfont.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)