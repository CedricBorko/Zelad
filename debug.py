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

    def show_info(self, name: str, info: str, y: int = 10):
        """Display of live variable changes in the window."""

        if not self.INFO_VISIBLE:
            return
        
        screen       = pygame.display.get_surface()
        debug_text   = self.FONT.render(f"{name}: {info}", True, self.FONT_COLOR)
        debug_frame  = debug_text.get_rect(topleft = (10, y))

        debug_frame.width  = max(200, debug_frame.width)
        debug_frame.height = 30

        pygame.draw.rect(screen, self.FRAME_BG, debug_frame)

        x = debug_frame.x + 5
        y = debug_frame.y + debug_frame.height // 2 - debug_text.get_rect().height // 2

        screen.blit(debug_text, (x, y))



Debug = Debugger()