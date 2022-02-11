from enum import Flag
import pygame
from PySide6.QtCore import Qt

Qt.AlignCenter
from pygame.sprite import AbstractGroup
from Logic.Math.vector2D import Vector2D
from settings import TILESIZE

class Direction(Flag):

    Idle  = 0x1

    Left  = 0x2
    Right = 0x4
    Up    = 0x8  
    Down  = 0x10

    Left_Idle  = Left | Idle
    Right_Idle = Right | Idle
    Up_Idle    = Up | Idle
    Down_Idle  = Down | Idle

    def __str__(self) -> str:
        return f"{self.name}" if "_" not in self.name else f"{' & '.join(self.name.split('_'))}"

class Player(pygame.sprite.Sprite):
    def __init__(self, position: Vector2D, obstacles: AbstractGroup, *groups: AbstractGroup) -> None:
        super().__init__(*groups)

        # self.coords = {
        #     "Down & Idle" : (0, 0),
        #     "Up & Idle"   : (16, 0),
        #     "Left & Idle" : (32, 0),
        #     "Right & Idle": (48, 0),
        #     "Down"        : [( 0, 0), ( 0, 16), ( 0, 32), ( 0, 48)],
        #     "Up"          : [(16, 0), (16, 16), (16, 32), (16, 48)],
        #     "Left"        : [(32, 0), (32, 16), (32, 32), (32, 48)],
        #     "Right"       : [(48, 0), (48, 16), (48, 32), (48, 48)],
        # }

        # self.load_assets()

        # self.image = pygame.image.load("NinjaAdventure/Actor/Characters/OldMan/SpriteSheet.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))

        self.image_down_idle  = pygame.image.load("Resources/Graphics/Player/idle_down.png").convert_alpha()
        self.image_up_idle    = pygame.image.load("Resources/Graphics/Player/idle_up.png").convert_alpha()
        self.image_left_idle  = pygame.image.load("Resources/Graphics/Player/idle_left.png").convert_alpha()
        self.image_right_idle = pygame.image.load("Resources/Graphics/Player/idle_right.png").convert_alpha()
        self.image            = self.image_down_idle
        
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))


        # self.image_left  = pygame.image.load("").convert_alpha()
        # self.image_front = pygame.image.load("").convert_alpha()
        # self.image_right = pygame.image.load("").convert_alpha()
        # self.image_back  = pygame.image.load("").convert_alpha()
        
        self.status = Direction.Down | Direction.Idle

        self.rect   = self.image.get_rect(topleft = (position * TILESIZE).to_tuple())
        self.hitbox = self.image.get_rect(topleft = (position * TILESIZE).to_tuple()).inflate(-16, 0)

        self.obstacles = obstacles

        self.direction = Vector2D(0, 0)
        self.speed = 3

        self.animation_index = 0
        
        
    def set_status(self) -> None:
        
        match self.direction.to_tuple():

            case  0,  0: self.status = self.status | Direction.Idle
            case -1,  0: self.status = Direction.Left          
            case  1,  0: self.status = Direction.Right
            case  0, -1: self.status = Direction.Up
            case  0,  1: self.status = Direction.Down
        


    def get_input(self) -> None:

        keys = pygame.key.get_pressed()

        self.direction = Vector2D(0, 0)
        self.speed = 3

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1   

        if keys[pygame.K_LSHIFT]:
            self.speed = 6

        self.set_status()
    
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

    def draw(self, surf: pygame.Surface, offset: pygame.rect.Rect):

        match self.status:
            case Direction.Left_Idle | Direction.Left:
                self.image = self.image_left_idle
            case Direction.Right_Idle | Direction.Right:
                self.image = self.image_right_idle
            case Direction.Up_Idle | Direction.Up:
                self.image = self.image_up_idle
            case Direction.Down_Idle | Direction.Down:
                self.image = self.image_down_idle


  
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))      
  
        surf.blit(self.image, offset)
