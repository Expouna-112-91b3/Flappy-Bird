import math
from config import Config


class Background:
    def __init__(self):
        self.config = Config()
        
        self.game_screen = self.config.get_screen()
        self.surface = self.game_screen["surface"]
        self.screen_height = self.game_screen["height"]
        self.screen_width = self.game_screen["width"]

        self.user_screen = self.config.get_monitor()

        self.wallpaper_sprite = self.config.get_wallpaper()["sprite"]["scaled"]

        self.ground = self.config.get_ground()
        self.ground_sprite = self.ground["sprite"]
        self.ground_width = self.ground["width"]
        self.y = self.screen_height - self.ground["height"]

        self.connected_grounds_size = math.ceil(self.screen_width / 312) * 2
        self.ground_movement_x = 0

    def get_ground_x(self):
        return self.ground_movement_x

    def draw_ground(self):
        """reseta
        o movimento do chao ao chegar na metade do outro
        chao conectado a ele, de forma que os sprites nao
        acabem repentinamente
        """
        if self.ground_movement_x <= -self.screen_width / 2:
            self.ground_movement_x = -8

        """quantidade 
        de grounds conectados eh igual a tamanho da
        tela / 312 (largura do ground em pixels - a sobreposicao entre eles)
        arredondado para cima
        """
        loop_size = 0
        self.ground_movement_x -= 3
        for _ in range(self.connected_grounds_size):
            self.surface.blit(
                self.ground_sprite,
                (loop_size + self.ground_movement_x, self.y),
            )
            loop_size = loop_size + self.ground_width

    def draw_wallpaper(self):
        self.surface.blit(self.wallpaper_sprite, (0, -self.y))
        self.surface.blit(self.wallpaper_sprite, (self.screen_height, -self.y))
