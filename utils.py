import pygame

"""
Classe de utilitarios do codigo
"""


class Utils:
    colors = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255)
    }
    
    font = None
    
    def init_font(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def draw_font(self, screen, text, color=(0, 0, 0), pos = (0,0)):
        text_surface = self.font.render(str(text), False, color)
        screen.blit(text_surface, pos)
