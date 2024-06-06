from tools.utils import Utils
from config import Config

from pygame.font import SysFont

class Debugger:
    """
    classe que mostra e gerencia a interface
    de debug
    """
    def __init__(self, bird):
        self.__bird = bird
        self.__config = Config()

        self.__screen = self.__config.get_screen()
        self.__surface = self.__screen["surface"]
        self.__screen_width = self.__screen["width"]
        self.__screen_height = self.__screen["height"]

        self.__font = SysFont('Arial', 30)

    def draw_debug(self, pipe_array=None):
        x, y = self.__bird.get_position()
        configs = {
            "Passaro": {
                "aceleracao": "{:.2f}".format(self.__bird.get_acceleration()),
                "posicao": f"{"{:.0f}".format(y)}x {"{:.0f}".format(x)}y",
            },
            "Tela": {
                "dimensoes": f"{self.__screen_height} x {self.__screen_width}",
                "quantidade de canos": len(pipe_array) if pipe_array else 0,
                "fps": "{:.0f}".format(self.__config.get_fps())
            },
        }

        distance = 0
        for label in list(configs):
            text_surface = self.__font.render(
                f"{label}",
                False,
                Utils.Colors.BLACK.value)
            self.__surface.blit(text_surface, (0, distance))
            distance += 30

            for value in list(configs[label]):
                text_surface = self.__font.render(
                    f"{value}: {configs[label][value]}",
                    False,
                    Utils.Colors.BLACK.value)
                self.__surface.blit(text_surface, (20, distance))
                distance += 30
