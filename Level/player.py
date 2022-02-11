import pygame

from pygame.sprite import AbstractGroup
from Logic.Math.vector2D import Vector2D
from settings import TILESIZE


class Player(pygame.sprite.Sprite):
    def __init__(self, position: Vector2D, obstacles: AbstractGroup, *groups: AbstractGroup) -> None:
        super().__init__(*groups)

        self.image = pygame.image.load("Resources/Graphics/Zelad.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = (position * TILESIZE).to_tuple())
        self.hitbox = self.image.get_rect(topleft = (position * TILESIZE).to_tuple()).inflate(-16, 0)

        self.obstacles = obstacles

        self.direction = Vector2D(0, 0)
        self.speed = 5
    
    def get_input(self) -> None:

        keys = pygame.key.get_pressed()

        self.direction = Vector2D(0, 0)
        self.speed = 5

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1   

        if keys[pygame.K_LSHIFT]: self.speed = 10
    
    def move(self, speed: float) -> None:
        if self.direction.magnitude != 0:
            self.direction = self.direction.normalize()
   
        self.hitbox.centerx += self.direction.x * speed
        self.check_collision(0)
        self.hitbox.centery += self.direction.y * speed
        self.check_collision(1)
        self.rect.center = self.hitbox.center
    
    def check_collision(self, direction: int):

        for sprite in self.obstacles:
            if direction == 0:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    else:
                        self.hitbox.left = sprite.hitbox.right

            else:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    else:
                        self.hitbox.top =  sprite.hitbox.bottom



    def update(self) -> None:
        self.get_input()
        self.move(self.speed)

