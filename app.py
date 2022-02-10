# Github https://github.com/CedricBorko/Zelad

import sys
import pygame
from Logic.Math.vector2D import Vector2D
from debug import Debug

from settings import *
from Level.level import Level


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Zelad")
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load("Resources/Graphics/Zelad.png")
        pygame.display.set_icon(self.img)

        self.level = Level()
        

    def run(self) -> None:
        while True:
            keys=pygame.key.get_pressed()
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        Debug.INFO_VISIBLE = not Debug.INFO_VISIBLE


            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)



if __name__ == "__main__":
    game = Game()
    game.run()