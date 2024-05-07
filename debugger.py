from utils import Utils
from config import Config

class Debugger:
    def __init__(self, bird):    
        self.bird = bird
        self.config = Config()
        
        self.game_screen = self.config.get_screen()
        self.surface = self.game_screen["surface"]
        self.screen_width = self.game_screen["width"]
        self.screen_height = self.game_screen["height"]
        
    def draw_debug(self, pipe_array):
        x, y = self.bird.get_position()
        configs = {
            "Passaro": {
                "aceleracao": "{:.2f}".format(self.bird.get_acceleration()),
                "posicao": f"{"{:.0f}".format(y)}x {"{:.0f}".format(x)}y",
            },
            "Tela": {
                "dimensoes": f"{self.screen_height} x {self.screen_width}",
                "quantidade de canos": len(pipe_array),
                "fps": "{:.0f}".format(self.config.get_fps())
            },
        }
        
        distance = 0
        for label in list(configs):
            Utils.draw_font(
                self.surface,
                f"{label}",
                pos=(0, distance)
            )
            distance += 30

            for value in list(configs[label]):
                Utils.draw_font(
                    self.surface,
                    f"{value}: {configs[label][value]}",
                    pos=(20, distance)
                )
                distance += 30