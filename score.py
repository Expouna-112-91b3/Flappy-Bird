from config import Config
from tools.utils import Utils

class Score:
    def __init__(self):
        self.__config = Config()

        self.__game_screen = self.__config.get_screen()
        self.__screen = self.__game_screen["surface"]


        self.__score = 0

    def draw(self, pos=(0, 0)):
        Utils.draw_game_text_font(
            screen=self.__screen,
            text=str(self.__score),
            pos=(10, 10)
        )

    def get(self):
        return self.__score
    
    def increase(self):
        self.__score += 1
