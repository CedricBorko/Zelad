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
        self.img = pygame.image.load("Resources/Graphics/bow.png")

        self.level = Level()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            self.screen.blit(self.img, (100, 100))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)



if __name__ == "__main__":
    game = Game()
    game.run()