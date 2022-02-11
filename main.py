# Github https://github.com/CedricBorko/Zelad

import sys
from tkinter import W
import pygame
from Logic.Math.vector2D import Vector2D
from UI.button import Button
from debug import Debug
import os

from settings import *
from Level.level import Level

cursor = pygame.image.load("Resources/Graphics/sword.png")
pygame.mouse.set_visible(False)
cursor_img_rect = cursor.get_rect()

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
        pygame.display.set_caption("Zelad")
        
        self.img = pygame.image.load("Resources/Graphics/Zelad.png")
        pygame.display.set_icon(self.img)

        self.level = Level()

        self.buttons = pygame.sprite.Group()
        self.btn_exit = Button(x=1225, y=5, width=50, height=30, offset_x=5, offset_y=5, callback=self.quit_game)
        self.buttons.add(self.btn_exit)

    def quit_game(self):
        pygame.quit()
        sys.exit()
        
    def run(self) -> None:
        while True:
            self.dt = self.clock.tick(FPS) / 1000
            self.handle_events()
            self.run_logic()
            self.draw()
            pygame.display.update()

            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                self.handle_keys(event)
            
            for button in self.buttons:
                button.handle_event(event)       

    def run_logic(self):
        self.level.run()
        self.buttons.update(self.dt)

    
    def draw(self):
        self.screen.fill('#3f48cc')
        self.level.run()
        self.buttons.draw(self.screen)
        cursor_img_rect.center = pygame.mouse.get_pos()
        self.screen.blit(cursor, cursor_img_rect)

    def handle_keys(self, event):
        if event.key == pygame.K_F1:
            Debug.INFO_VISIBLE = not Debug.INFO_VISIBLE

        if event.key == pygame.K_F2:
            self.s_width, self.s_height = pygame.display.Info().current_w, pygame.display.Info().current_h
            pygame.display.quit()
          
            w = 1980 if self.s_width == 1280 else 1280
            h = 1080 if self.s_height == 720 else 720
          
          
            pygame.display.init()
            self.screen = pygame.display.set_mode((w, h), pygame.NOFRAME)              
            self.level.display_surface = pygame.display.get_surface()
            self.level.visible_sprites.display_surface = pygame.display.get_surface()
            for button in self.buttons:
                button.adjust(w, h)


if __name__ == "__main__":
    game = Game()
    game.run()