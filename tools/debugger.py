from tools.utils import Utils
from config import Config

"""
classe que mostra e gerencia a interface
de debug
"""


class Debugger:
    def __init__(self, bird):
        self.__bird = bird
        self.__config = Config()

        self.__game_screen = self.__config.get_screen()
        self.__surface = self.__game_screen["surface"]
        self.__screen_width = self.__game_screen["width"]
        self.__screen_height = self.__game_screen["height"]

    def draw_debug(self, pipe_array):
        x, y = self.__bird.get_position()
        configs = {
            "Passaro": {
                "aceleracao": "{:.2f}".format(self.__bird.get_acceleration()),
                "posicao": f"{"{:.0f}".format(y)}x {"{:.0f}".format(x)}y",
            },
            "Tela": {
                "dimensoes": f"{self.__screen_height} x {self.__screen_width}",
                "quantidade de canos": len(pipe_array),
                "fps": "{:.0f}".format(self.__config.get_fps())
            },
        }

        distance = 0
        for label in list(configs):
            Utils.draw_font(
                self.__surface,
                f"{label}",
                pos=(0, distance)
            )
            distance += 30

            for value in list(configs[label]):
                Utils.draw_font(
                    self.__surface,
                    f"{value}: {configs[label][value]}",
                    pos=(20, distance)
                )
                distance += 30
