import math


class Background:
    def __init__(self, screen, bg_sprite, ground_sprite):
        self.screen = screen
        self.screen_height = screen.get_height()
        self.screen_width = screen.get_width()

        self.bg_sprite = bg_sprite

        self.ground_sprite = ground_sprite
        self.ground_rect = self.ground_sprite.get_rect()
        self.ground_width = self.ground_rect.width
        self.ground_x = self.screen_height - self.ground_rect.height

        self.ground_movement_x = 0

        self.ground_movement_x = 0

    def draw(self):
        self.screen.blit(self.bg_sprite, (0, -self.ground_x))
        self.screen.blit(self.bg_sprite, (self.screen_height, -self.ground_x))

        """ 
        o sprite do chao reseta ao chegar na metade do outro
        chao conectado a ele, de forma que ele nao acabe
        repentinamente
        """
        if self.ground_movement_x <= -self.screen_width:
            self.ground_movement_x = 0

        """
        quantidade de grounds conectados eh igual a tamanho da
        tela / 312 (largura do ground em pixels - a sobreposicao entre eles)
        arredondado para cima
        """
        # o sprite do chao reseta ao chegar na metade do outro
        # chao conectado a ele, de forma que ele nao acabe
        # repentinamente
        if self.ground_movement_x <= -self.screen_width:
            self.ground_movement_x = 0

        loop_size = 0
        for _ in range(math.ceil(self.screen_width / 312) * 2 * 2):
            self.ground_movement_x -= .5
            self.ground_movement_x -= .5
            self.screen.blit(self.ground_sprite, (loop_size + self.ground_movement_x +
                             self.ground_movement_x, self.ground_x))
            loop_size = loop_size + self.ground_width
