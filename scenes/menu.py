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

        self.__input_font = pygame.font.Font("./fonts/default.ttf", 60)

        self.__play_button_font = pygame.font.Font("./fonts/default.ttf", 32)
        self.__play_button_color = 220
        self.__color_direction = .5

        self.__playername = self.__config.get_playername()

    def run(self):
        KEYS = pygame.key.get_pressed()

        for event in pygame.event.get():
            if KEYS[pygame.K_SPACE]:
                if len(self.__playername) == 6:
                    self.__config.set_playername(self.__playername)
                    self.__config.set_scene(Scenes.SINGLEPLAYER.value)

            if KEYS[pygame.K_ESCAPE]:
                self.__config.close_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.__playername = self.__playername[:-1]
                else:
                    if len(self.__playername) < 6:
                        self.__playername += event.unicode

        self.__play_button_color += self.__color_direction
        if self.__play_button_color in (220, 255):
            self.__color_direction *= -1

        self.__background.draw_wallpaper()
        self.__background.draw_ground()

        text_surface = self.__outline_font.render(
            "Flappy Bird", False, (0, 0, 0))
        title_pos = self.__screen_width - text_surface.get_width() / 2
        self.__surface.blit(text_surface, (title_pos + 8,
                            self.__screen_height - 140))

        text_surface = self.__font.render(
            "Flappy Bird", False, (255, 255, 255))
        self.__surface.blit(
            text_surface, (title_pos, self.__screen_height - 150))

        input_pos = (self.__screen_width / 2 + 230, self.__screen_height + 150)

        ### NAME INPUT ###
        pygame.draw.rect(
            self.__surface, (0, 0, 0),
            pygame.Rect(input_pos[0] - 3, input_pos[1] - 3, 236, 106))

        input_rect = pygame.draw.rect(
            self.__surface, (255, 255, 255),
            pygame.Rect(input_pos[0], input_pos[1], 230, 100))
        ##################

        text_surface = self.__input_font.render(self.__playername,
                                                False, (0, 0, 0))

        centralized_text_surface = text_surface.get_rect(
            center=input_rect.center)
        
        text_surface_pos = (centralized_text_surface.x,
                            centralized_text_surface.y)
        
        self.__surface.blit(text_surface, text_surface_pos)

        rgb = (self.__play_button_color,
               self.__play_button_color,
               self.__play_button_color)

        text_surface = self.__play_button_font.render(
            "Pressione [botao] para jogar", False, rgb)

        self.__surface.blit(text_surface,
                            (self.__screen_width - text_surface.get_width() / 2,
                             self.__screen_height + 100))
