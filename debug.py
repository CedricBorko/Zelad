import pygame
pygame.init()

class Debugger:

    INFO_VISIBLE = False
    FONT         = pygame.font.Font(None, 24)
    FONT_COLOR   = "White"
    FRAME_BG     = pygame.SRCALPHA

    def toggle_hitboxes(self):
        """Toggle Player and Obstacle / Enemy hitboxes."""
        pass

    def show_info(self, info: str, position: tuple[int, int] = (10, 10)):
        """Display of live variable changes in the window."""

        if not self.INFO_VISIBLE:
            return
        
        screen       = pygame.display.get_surface()
        debug_text   = self.FONT.render(str(info), True, self.FONT_COLOR)
        debug_frame  = debug_text.get_rect(topleft = position)

        pygame.draw.rect(screen, self.FRAME_BG, debug_frame)
        screen.blit(debug_text, debug_frame)



Debug = Debugger()