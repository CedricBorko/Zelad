from __future__ import annotations
import datetime
import json
import pygame
from Level.player import Player
from Level.tile import Tile
from Logic.Math.vector2D import Vector2D
from debug import Debug

from settings import *

class Level:

    AUTHOR : str = ""
    CREATED: datetime.date = datetime.date.today()

    def __init__(self) -> None:

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites  = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.set_tiles()

    def set_tiles(self) -> None:

        for id_r, row in enumerate(LEVEL[0]):
            for id_c, column in enumerate(row):
                
                
                match column:

                    case "x":
                        Tile(Vector2D(id_c * TILESIZE, id_r * TILESIZE), "water-deep", [self.visible_sprites, self.obstacle_sprites])
                    case "w":
                        Tile(Vector2D(id_c * TILESIZE, id_r * TILESIZE), "water", [self.visible_sprites, self.obstacle_sprites])
                    case ".":
                        Tile(Vector2D(id_c * TILESIZE, id_r * TILESIZE), "grass", [self.visible_sprites])
                    case "b":
                        Tile(Vector2D(id_c * TILESIZE, id_r * TILESIZE), "bridge", [self.visible_sprites])
                    

        x, y = LEVEL[1]
        self.player = Player(Vector2D(x, y), self.obstacle_sprites, [self.visible_sprites])


    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        Debug.show_info("Speed", self.player.speed)
        Debug.show_info("Dir", self.player.status, 40)

    def update_surface(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites.display_surface = pygame.display.get_surface()
    
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(22 * TILESIZE, 14 * TILESIZE)
    
    def custom_draw(self, player: Player):

        self.offset.x = player.rect.x - self.display_surface.get_size()[0] // 2
        self.offset.y = player.rect.y - self.display_surface.get_size()[1] // 2


        for sprite in self.sprites():
            offset_rect = sprite.rect.topleft - self.offset
            if sprite == player:
                player.draw(self.display_surface, offset_rect)
            else:
                self.display_surface.blit(sprite.image, offset_rect)

