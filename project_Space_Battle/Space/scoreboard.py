from pygame import sysfont
from Space.ship import Ship
from pygame.sprite import Group


class Scoreboard(object):

    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        self.text_color = (30, 30 ,30)
        self.font = sysfont.SysFont(None, 40)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        high_score = self.stats.high_score
        self.high_score_image = self.font.render('Top score: {}'.format(high_score), True, self.text_color, self.game_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        self.level_image = self.font.render('Level: {}'.format(self.stats.level), True, self.text_color, self.game_settings.bg_color)
        # Position below the Score
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number  in range(self.stats.ship_life):
            ship = Ship(self.screen, self.game_settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)