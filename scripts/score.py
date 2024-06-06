from pygame.font import Font
from pygame.surface import Surface

from config import Config

class Score:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True

            self.__config = Config()
            self.__surface: Surface = self.__config.get_screen()["surface"]
            self.__pos = (self.__surface.get_width() / 2, 50)
            self.__score = 0
            self.__font = Font("./fonts/default.ttf", 30)

            self.__current_score = 0
            self.__scores = []
        

    def draw(self):
        text_surface = self.__font.render(str(self.__current_score), False, (0, 0, 0))
        self.__surface.blit(text_surface, self.__pos)

    def increase(self):
        self.__current_score += 1

    def get_scores(self):
        return self.__scores
    
    def get_score(self):
        return self.__score
    
    def sort_score(self):
        self.__scores.sort(key=lambda x: x[1], reverse=True)
        if len(self.__scores) > 10:
            self.__scores.pop()

    def push_score(self, player_name):
        self.__scores.append([player_name, self.__current_score])
        self.sort_score()
    
    def reset_score(self):
        self.__current_score = 0