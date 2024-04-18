import pygame

class Bird:
    def __init__(self, screen, sprite, ground_height):
        self.gravity_force, self.y = 10, 0
        self.screen = screen
        self.screen_height = screen.get_height()
        self.sprite = sprite
        self.sprite_rect = sprite.get_rect()
        self.ground_height = ground_height

    def draw(self):
        self.screen.blit(self.sprite, self.sprite_rect)

    def apply_gravity(self):
        # mover isso para alguma função de morte
        if self.y + self.sprite_rect.height > self.screen_height - self.ground_height: return
        self.y += self.gravity_force
        self.sprite_rect.y = self.y