"""
classe das configuracoes gerais do jogo,
como tamanho de tela, importacao de sprites, etc
"""

from screeninfo import get_monitors
import pygame
from pygame.image import load


class Config:

    """
    as variaveis _instance, _initialized e o metodo __new__
    configuram a classe como um singleton
    """
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True

            # debug
            self.__debug_mode = True

            # monitor
            self.__user_screen = get_monitors()[0]
            self.__monitor_width = self.__user_screen.width
            self.__monitor_height = self.__user_screen.height

            # fps
            self.__clock = pygame.time.Clock()
            self.__max_fps = 60

            # wallpaper
            self.__wallpaper_sprite = None
            self.__scaled_wallper_sprite = None

            # ground
            self.__ground_sprite = None
            self.__ground_sprite_rect = None

            # pipe
            self.__pipe_sprite = None
            self.__pipe_sprite_rect = None

            # bird
            self.__bird_downflap_sprite = None
            self.__bird_midflap_sprite = None
            self.__bird_upflap_sprite = None
            self.__bird_rect = None

            # GAME screen
            self.__game_screen = None

    def setup_images(self):
        # wallpaper
        self.__wallpaper_sprite = load(
            './sprites/scenario/background.bmp').convert_alpha()

        self.__scaled_wallper_sprite = pygame.transform.scale(
            self.__wallpaper_sprite,
            (self.__monitor_height, self.__monitor_width)
        )

        # ground
        self.__ground_sprite = load(
            './sprites/scenario/ground.bmp').convert_alpha()
        self.__ground_sprite_rect = self.__ground_sprite.get_rect()

        # pipe
        self.__pipe_sprite = load('./sprites/pipe/pipe.png').convert_alpha()
        self.__pipe_sprite_rect = self.__pipe_sprite.get_rect()

        # bird
        self.__bird_downflap_sprite = load(
            './sprites/bird/downflap.bmp').convert_alpha()
        self.__bird_midflap_sprite = load(
            './sprites/bird/midflap.bmp').convert_alpha()
        self.__bird_upflap_sprite = load(
            './sprites/bird/upflap.bmp').convert_alpha()

        self.__bird_rect = self.__bird_midflap_sprite.get_rect()

    def get_monitor(self):
        return {
            "width": self.__monitor_width,
            "height": self.__monitor_height,
        }

    def get_wallpaper(self):
        return {
            "sprite": {
                "default": self.__wallpaper_sprite,
                "scaled": self.__scaled_wallper_sprite,
            },
        }

    def get_ground(self):
        return {
            "sprite": self.__ground_sprite,
            "width": self.__ground_sprite_rect.width,
            "height": self.__ground_sprite_rect.height,
        }

    def get_pipe(self):
        return {
            "sprite": {
                "default": self.__pipe_sprite,
                "rotated": pygame.transform.rotate(
                    self.__pipe_sprite,
                    180,
                ),
            },
            "width": self.__pipe_sprite_rect.width,
            "height": self.__pipe_sprite_rect.height,
        }

    def get_bird(self):
        return {
            "sprites": {
                "downflap": self.__bird_downflap_sprite,
                "midflap": self.__bird_midflap_sprite,
                "upflap": self.__bird_upflap_sprite,
            },
            "width": self.__bird_rect.width,
            "height": self.__bird_rect.height
        }

    def start_screen(self):
        self.__game_screen = pygame.display.set_mode((
            self.__monitor_width,
            self.__monitor_height,
        ))

    def get_screen(self):
        return {
            "surface": self.__game_screen,
            "width": self.__game_screen.get_width(),
            "height": self.__game_screen.get_height()
        }

    def clock_tick(self, framerate):
        return self.__clock.tick(framerate)

    def get_max_fps(self):
        return self.__max_fps

    def get_fps(self):
        return self.__clock.get_fps()

    def get_is_debugging(self):
        return self.__debug_mode

    def toggle_debug(self):
        self.__debug_mode = not self.__debug_mode
