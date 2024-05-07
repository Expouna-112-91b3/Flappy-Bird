import math

from config import Config


class Background:
    def __init__(self):
        self.__config = Config()

        self.__game_screen = self.__config.get_screen()
        self.__surface = self.__game_screen["surface"]
        self.__screen_height = self.__game_screen["height"]
        self.__screen_width = self.__game_screen["width"]

        self.__wallpaper_sprite = self.__config.get_wallpaper()[
            "sprite"]["scaled"]

        self.__ground = self.__config.get_ground()
        self.__ground_sprite = self.__ground["sprite"]
        self.__ground_width = self.__ground["width"]
        self.y = self.__screen_height - self.__ground["height"]

        self.__connected_grounds_size = math.ceil(
            self.__screen_width / 312) * 2
        self.__ground_movement_x = 0

    def draw_ground(self):
        """reseta
        o movimento do chao ao chegar na metade do outro
        chao conectado a ele, de forma que os sprites nao
        acabem repentinamente
        """
        if self.__ground_movement_x <= -self.__screen_width / 2:
            self.__ground_movement_x = -8

        """quantidade 
        de grounds conectados eh igual a tamanho da
        tela / 312 (largura do ground em pixels - a sobreposicao entre eles)
        arredondado para cima
        """
        loop_size = 0
        self.__ground_movement_x -= 3
        for _ in range(self.__connected_grounds_size):
            self.__surface.blit(
                self.__ground_sprite,
                (loop_size + self.__ground_movement_x, self.y),
            )
            loop_size = loop_size + self.__ground_width

    def draw_wallpaper(self):
        self.__surface.blit(self.__wallpaper_sprite, (0, -self.y))
        self.__surface.blit(self.__wallpaper_sprite,
                            (self.__screen_height, -self.y))
