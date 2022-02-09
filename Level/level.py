from __future__ import annotations
import datetime
import json
import os
import pygame


class Level:

    AUTHOR : str = "Cedric"
    CREATED: datetime.date = datetime.date.today()
    NAME   : str = "Level2"

    def __init__(self) -> None:

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites  = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        pass

    def save_level(self, file_path: str):

        if os.path.exists(file_path):
            if input("Override?").upper() == "N":
                print("Canceled")
                return

        with open(file_path, "w", encoding="utf-8") as l_file:
            json.dump({"author": self.AUTHOR, "created": self.CREATED.strftime("%Y-%m-%d"), "name": self.NAME}, l_file)