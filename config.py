"""
classe das configuracoes gerais do jogo,
como tamanho de tela, importacao de sprites, etc
"""

from screeninfo import get_monitors
import pygame
from pygame.image import load

from tools.utils import Utils

from scenes.scenes import Scenes


class Config:
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

            # coin
            self.__front_sprite = None
            self.__side_sprite = None
            self.__25deg_sprite = None
            self.__76deg_sprite = None

            # GAME screen
            self.__surface = None

            # game status
            self.__running = True
            self.__current_scene = Scenes.MENU.value
            self.__scores = []
            self.dt = 0

    def get_scores(self):
        return self.__scores

    def push_score(self, score):
        for i, user_score in enumerate(self.__scores):
            if score[1] >= user_score[1]:
                continue
            else:
                self.__scores.insert(i, score)

    def get_current_scene(self):
        return self.__current_scene

    def set_scene(self, scene: int):
        self.__current_scene = scene

    def get_running(self):
        return self.__running

    def close_game(self):
        self.__running = False

    def lc(self, image_path):
        return load(image_path).convert_alpha()

    def setup_images(self):
        LCA = Utils.Image.lca

        # wallpaper
        self.__wallpaper_sprite = LCA('./sprites/scenario/background.bmp')
        self.__scaled_wallper_sprite = pygame.transform.scale(
            self.__wallpaper_sprite,
            (self.__monitor_height, self.__monitor_width)
        )

        # ground
        self.__ground_sprite = LCA('./sprites/scenario/ground.bmp')
        self.__ground_sprite_rect = self.__ground_sprite.get_rect()

        # pipe
        self.__pipe_sprite = LCA('./sprites/pipe/pipe.png')
        self.__pipe_sprite_rect = self.__pipe_sprite.get_rect()

        # bird
        self.__bird_downflap_sprite = LCA('./sprites/bird/downflap.bmp')
        self.__bird_midflap_sprite = LCA('./sprites/bird/midflap.bmp')
        self.__bird_upflap_sprite = LCA('./sprites/bird/upflap.bmp')
        self.__bird_rect = self.__bird_midflap_sprite.get_rect()

        # coin
        self.__front_sprite = LCA("./sprites/coin/front.png")
        self.__side_sprite = LCA("./sprites/coin/side.png")
        self.__25deg_sprite = LCA("./sprites/coin/25deg.png")
        self.__76deg_sprite = LCA("./sprites/coin/75deg.png")
        self.__coin_rect = self.__front_sprite.get_rect()

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

    def get_coin(self):
        return {
            "sprites": {
                "front": self.__front_sprite,
                "side": self.__side_sprite,
                "25deg": self.__25deg_sprite,
                "75deg": self.__76deg_sprite
            },
            "width": self.__coin_rect.width,
            "height": self.__coin_rect.height
        }

    def start_screen(self):
        self.__surface = pygame.display.set_mode((
            self.__monitor_width,
            self.__monitor_height,
        ), vsync=1)

    def get_screen(self):
        return {
            "surface": self.__surface,
            "width": self.__surface.get_width(),
            "height": self.__surface.get_height(),
            "rect": self.__surface.get_rect()
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

    def set_dt(self, x):
        self.dt = x

    def get_dt(self):
        return self.dt
