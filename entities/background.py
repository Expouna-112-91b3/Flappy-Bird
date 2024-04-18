import pygame
import math

class Background:
    ground_width = 0
    ground_x = 0
    
    def __init__(self, screen, bg_sprite, ground_sprite):
        self.screen = screen
        self.screen_height = screen.get_height()
        self.screen_width = screen.get_width()
        
        self.bg_sprite = bg_sprite
        self.ground_sprite = ground_sprite
        
        self.ground_rect = self.ground_sprite.get_rect()
        self.ground_width = self.ground_rect.width
        self.ground_x = self.screen_height - self.ground_rect.height
    
    def draw(self):
        self.screen.blit(self.bg_sprite, (0, 0))
        self.screen.blit(self.bg_sprite, (self.screen_height, 0))
        
        loop_size = 0
        # A QUANTIDADE DE GROUNDS CONECTADOS =
        # tamanho da tela / 312 (largura do ground em pixels - a sobreposição entre eles)
        # (arredondado para cima)
        for _ in range(math.ceil(self.screen_width / 312)):
            self.screen.blit(self.ground_sprite, (loop_size, self.ground_x))
            loop_size = loop_size + self.ground_width