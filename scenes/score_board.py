from config import Config

from scripts.background import Background

import pygame

class ScoreBoard():
    def __init__(self):
        self.__config = Config()
        self.__background = Background()

        self.__screen = self.__config.get_screen()
        self.__surface: pygame.Surface = self.__screen['surface']
        self.__screen_rect = self.__screen['rect']

        self.__board = pygame.Surface((1050, 650))
        self.__board.set_alpha(190)
        self.__board.fill((0,0,0))

        self.__board_pos = self.__board.get_rect(center = self.__screen_rect.center)
        self.__font = pygame.font.Font("./fonts/numbers.ttf", 50)

        self.__title = self.__font.render("Joao Antonio - 50pts", False, (255, 255, 255))
        self.__title_pos = self.__title.get_rect(center = self.__screen_rect.center)


    def run(self):
        self.__background.draw_wallpaper()
        self.__background.draw_ground()

        self.__surface.blit(self.__board, self.__board_pos)
        self.__surface.blit(self.__title, self.__title_pos)