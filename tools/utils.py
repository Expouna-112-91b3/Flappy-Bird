from enum import Enum

from pygame.image import load

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
            return load(image_path).convert_alpha()
        
        def lc(image_path):
            """
            carrega uma imagem especifica e a retorna convertida
            """
            return load(image_path).convert()
             
