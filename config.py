"""
classe das configuracoes gerais do jogo,
como tamanho de tela, importacao de sprites, etc
"""

from screeninfo import get_monitors
import pygame
from pygame.image import load

from scenes.scenes import Scenes

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
            self.__surface = None
            
            # game status
            self.__paused = False
            self.__running = True
            self.__current_scene = Scenes.MENU.value
            self.__scores = []

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

    def get_paused(self):
        return self.__paused

    def toggle_paused(self):
        self.__paused = not self.__paused
        return self.__paused
    
    def pause(self):
        self.__paused = True
    
    def get_running(self):
        return self.__running
    
    def close_game(self):
        self.__running = False

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
        self.__surface = pygame.display.set_mode((
            self.__monitor_width,
            self.__monitor_height,
        ))

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
