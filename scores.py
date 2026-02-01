import pygame.font


class Scores():
    """return score game"""

    def __init__(self, screen, stats) -> None:
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (178, 178, 178)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()

    def image_score(self):
        """return text score to imaging"""

        self.score_imaging = self.font.render(
            str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_imaging.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        """преобразование рекорда в изображение"""
        self.high_score_image = self.font.render(
            str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def show_score(self):
        self.screen.blit(self.score_imaging, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
