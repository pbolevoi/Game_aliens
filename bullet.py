import pygame
from pygame.sprite import Group


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun) -> None:
        """пуля в позиции пушки"""

        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 12)
        self.color = 49, 255, 0
        self.speed = 1.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self) -> None:
        """перемещение пули вверх"""

        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
