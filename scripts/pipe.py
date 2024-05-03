import math
import pygame


class Pipe:
    def __init__(self, screen, sprite):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        self.sprite = sprite
        self.rotated_sprite = pygame.transform.rotate(
            self.sprite,
            180,
        )
        self.sprite_rect = self.sprite.get_rect()

        self.generation_delay = 1

    def draw(self):
        self.screen.blit(
            self.sprite,
            (self.screen_width / 2, self.screen_height - self.sprite_rect.height),
        )
        self.screen.blit(
            self.rotated_sprite,
            (self.screen_width / 2, 0),
        )
