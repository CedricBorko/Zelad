import pygame
from Logic.Math.vector2D import Vector2D
from settings import *
from pygame.sprite import AbstractGroup

class Tile(pygame.sprite.Sprite):
    def __init__(self, position: Vector2D, sprite: str, groups: AbstractGroup) -> None:
        super().__init__(groups)

        self.image = pygame.image.load(f"Resources/Graphics/{sprite}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position.to_tuple())