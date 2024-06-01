import pygame

"""
classe de utilitarios gerais, como
gerador de texto e dicionario de cores
"""


class Utils:
    colors = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255)
    }

    @staticmethod
    def init_font():
        pygame.font.init()

    @staticmethod
    def draw_debbuger_font(screen, text, color=(0, 0, 0), pos=(0, 0)):
        font = pygame.font.SysFont('Arial', 30)
        text_surface = font.render(str(text), False, color)
        screen.blit(text_surface, pos)

    @staticmethod
    def draw_game_text_font(screen, text, size=30, color=(0, 0, 0), pos=(0, 0)):
        font = pygame.font.Font("./fonts/text.ttf", size)
        text_surface = font.render(str(text), False, color)
        screen.blit(text_surface, pos)
