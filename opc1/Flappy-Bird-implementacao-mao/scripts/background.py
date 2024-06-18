import math

from config import Config
from pygame import Rect


class Background:
    def __init__(self):
        self.__config = Config()

        self.__screen = self.__config.get_screen()
        self.__surface = self.__screen["surface"]
        self.__screen_height = self.__screen["height"]
        self.__screen_width = self.__screen["width"]

        self.__ground = self.__config.get_ground()
        self.__ground_sprite = self.__ground["sprite"]
        self.__ground_width = self.__ground["width"]
        self.__ground_height = self.__ground["height"]
        self.__ground_y = self.__screen_height - self.__ground_height

        self.__wallpaper_sprite = self.__config.get_wallpaper()["sprite"]["scaled"]
        self.__wallpper_y = -self.__ground_height * 5

        self.__connected_grounds_size = math.ceil(
            self.__screen_width / self.__ground_width) * 2
        self.__ground_movement_x = 0

    def draw_ground(self):
        """
        O chao do jogo é formado por varios sprites de chao conectados;
        para que o chao nao resete repentinamente, a posicao inicial
        do chao é resetada sempre que chegar na metade do outro
        chao conectado a ele
        """

        if self.__ground_movement_x <= -self.__screen_width / 2:
            self.__ground_movement_x = 0

        """
        A quantidade de grounds conectados eh igual a tamanho da
        tela / 312 (largura do ground em pixels - a sobreposicao entre eles)
        arredondado para cima
        """
        loop_size = 0
        self.__ground_movement_x -= 20
        for _ in range(self.__connected_grounds_size):
            self.__surface.blit(
                self.__ground_sprite,
                (loop_size + self.__ground_movement_x, self.__ground_y)),
            loop_size = loop_size + self.__ground_width
            
    def draw_wallpaper(self):
        self.__surface.blit(self.__wallpaper_sprite, (0, self.__wallpper_y))
        self.__surface.blit(self.__wallpaper_sprite,
                            (self.__screen_height, self.__wallpper_y))
