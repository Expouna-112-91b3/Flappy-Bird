import pygame

from config import Config

from scripts.background import Background

from scenes.scenes import Scenes

class Menu():
    def __init__(self):
        self.__config = Config()

        self.__screen = self.__config.get_screen()
        self.__surface: pygame.Surface = self.__screen['surface']
        self.__screen_height = self.__screen['height'] / 2
        self.__screen_width = self.__screen['width'] / 2

        self.__background = Background()

        self.__font = pygame.font.Font("./fonts/default.ttf", 120)
        self.__outline_font = pygame.font.Font("./fonts/default.ttf", 120)

        self.__play_button_font = pygame.font.Font("./fonts/default.ttf", 32)
        self.__play_button_color = 220
        self.__color_direction = .5
    
    def run(self):
        KEYS = pygame.key.get_pressed()

        for _ in pygame.event.get():
            if KEYS[pygame.K_SPACE]:
                self.__config.set_scene(Scenes.SINGLEPLAYER.value)

        self.__play_button_color += self.__color_direction
        if self.__play_button_color in (220, 255):
            self.__color_direction *= -1

        self.__background.draw_wallpaper()
        self.__background.draw_ground()

        text_surface = self.__outline_font.render("Flappy Bird", False, (0, 0, 0))
        self.__surface.blit(text_surface, (self.__screen_width - text_surface.get_width() / 2 + 8, self.__screen_height - 140))

        text_surface = self.__font.render("Flappy Bird", False, (255, 255, 255))
        self.__surface.blit(text_surface, (self.__screen_width - text_surface.get_width() / 2, self.__screen_height - 150))

        text_surface = self.__play_button_font.render("Pressione [botao] para jogar", False, (self.__play_button_color, self.__play_button_color, self.__play_button_color))
        self.__surface.blit(text_surface, (self.__screen_width - text_surface.get_width() / 2, self.__screen_height + 100))