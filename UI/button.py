from typing import Callable
import pygame
from pygame import gfxdraw
pygame.init()
BUTTON_FONT = pygame.font.SysFont("Arial", 12)

class Button(pygame.sprite.Sprite):
    def __init__(
        self,
        x       : int,
        y       : int,
        width   : int,
        height  : int,
        callback: Callable,
        font    : pygame.font.Font = BUTTON_FONT,
        text    : str = "",
        offset_l: int = 0,
        offset_t: int = 0,
        offset_r: int = 0,
        offset_b: int = 0,
        cursor  : pygame.Surface = None
) -> None:
        super().__init__()

        self.x        = x
        self.y        = y
        self.width    = width
        self.height   = height

        self.offset_l = offset_l
        self.offset_t = offset_t
        self.offset_r = offset_r
        self.offset_b = offset_b

        self.callback = callback        

        self.font = font
        self.text = text

        self.image_normal = pygame.image.load("exit.png")
        self.image_hover  = pygame.image.load("exit_hover.png")
        self.image        = self.image_normal
        self.rect         = self.image.get_rect(topleft=(self.x, self.y))

        # self.rect = pygame.Rect(x, y, width, height)
        self.button_down = False
    
    def adjust(self, s_width: int, s_height: int):
        self.x    = s_width - self.width - self.offset_r
        self.y    = self.offset_t
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def handle_event(self, event) -> None:

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.button_down = True
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos) and self.button_down:
                self.callback()
                self.image = self.image_hover
            self.button_down = False

        elif event.type == pygame.MOUSEMOTION:
            collided = self.rect.collidepoint(event.pos)
            if collided and not self.button_down:
                self.image = self.image_hover

            elif not collided:
                self.image = self.image_normal




class IconButton:
    def __init__(self, image: pygame.Surface, x: int, y: int, width: int, height: int) -> None:

        self.screen      = pygame.display.get_surface()
        self.image       = image
        self.image_hover = image
        self.x           = x
        self.y           = y
        self.width       = width
        self.height      = height
        self.rect        = pygame.rect.Rect(x, y, width, height)

        self.hover = False
        self.click = None

        self.bg = (242, 242, 242)
        self.bg_hover = (255, 25, 86)

    def run(self, events) -> None:
            m_x, m_y   = pygame.mouse.get_pos()
            
            self.hover = self.rect.collidepoint(m_x, m_y)

            self.draw()

            if self.hover and self.click is not None:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.click()

    def draw(self) -> None:

        x = self.rect.x + self.width // 2 - self.image.get_width() // 2
        y = self.rect.y + self.height // 2 - self.image.get_height() // 2

        if self.hover:
            gfxdraw.box(self.screen, self.rect, self.bg_hover) 
            self.screen.blit(self.image_hover, (x, y))
        else:
            gfxdraw.box(self.screen, self.rect, self.bg) 
            self.screen.blit(self.image, (x, y))

        

        