from __future__ import annotations
import datetime
import json
import pygame


class Level:

    AUTHOR : str = ""
    CREATED: datetime.date = datetime.date.today()

    def __init__(self) -> None:

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites  = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        pass