# Github https://github.com/CedricBorko/Zelad

import sys
import pygame

from settings import *
from Level.level import Level

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Zelad")
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load("Resources/Graphics/Zelad.png")
        self.img2 = pygame.image.load("Resources/Graphics/bow.png")
        self.img = pygame.transform.scale(self.img, (64, 64))
        pygame.display.set_icon(self.img)

        self.level = Level()
        self.level.save_level("level.json")
        self.x = 100
        self.y = 100

    def run(self) -> None:
        while True:
            keys=pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if keys[pygame.K_LEFT]:
                    self.x -= 10
                if keys[pygame.K_RIGHT]:
                    self.x += 10
                if keys[pygame.K_UP]:
                    self.y -= 10
                if keys[pygame.K_DOWN]:
                    self.y += 10
     

            self.screen.fill('black')
            self.screen.blit(self.img, (self.x, self.y))
            self.screen.blit(self.img2, (self.x + 25, self.y))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)



if __name__ == "__main__":
    game = Game()
    game.run()