from enum import Enum

class Utils:
    """
    classe de utilitarios gerais
    """
    class Colors(Enum):
        """
        RGB de cores padrão
        """
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0),
        GRAY = (155, 155, 155),
        RED = (255, 0, 0),
        GREEN = (0, 255, 0),
        BLUE = (0, 0, 255)

    class Image():
        def lca(image_path):
            """
            carrega uma imagem especifica e a retorna convertida para alpha
            """
            from pygame.image import load
            return load(image_path).convert_alpha()
        
        def lc(image_path):
            """
            carrega uma imagem especifica e a retorna convertida
            """
            from pygame.image import load
            return load(image_path).convert()

    class Text():
        def __init__(self, font):
            self.__font = font

        def render(self, text, color = (255, 255, 255)):
            return self.__font.render(text, False, color)
        
    class Entitiy():
        @staticmethod
        def draw_hitbox(surface, rect, color=(255,0,0), outline_size=1):
            from pygame.draw import rect
            rect(surface, color, rect, outline_size)

    class Chances():
        @staticmethod
        def random_chance(x: float):
            from random import random
            if random() < x:
                return True
            return False
             
