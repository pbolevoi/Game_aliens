from typing import Any
import pygame
from pygame.sprite import Group


class Alien(pygame.sprite.Sprite):
    """создание пришельца"""

    def __init__(self, screen) -> None:
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('img/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        """position aliens to bottom"""
        self.y += 0.04
        self.rect.y = self.y
