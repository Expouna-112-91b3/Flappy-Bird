from pygame.font import Font
from pygame.surface import Surface

class Score:
    def __init__(self, game_screen):
        self.__surface: Surface = game_screen
        
        self.__pos = (self.__surface.get_width() / 2, 50)
        
        self.__score = 0
        
        self.__font = Font("./fonts/numbers.ttf", 30)
        

    def draw(self):
        text_surface = self.__font.render(str(self.__score), False, (0, 0, 0))
        self.__surface.blit(text_surface, self.__pos)
    
    def increase(self):
        self.__score += 1
