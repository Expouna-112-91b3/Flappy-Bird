from config import Config
from time import time

from pygame import draw
from pygame import Rect
from scripts.score import Score

from random import randint

class Coin():
    def __init__(self, screen_offset=0):
        self.__screen_offset = screen_offset

        self.__config = Config()
        
        self.__screen = self.__config.get_screen()
        self.__surface = self.__screen["surface"]
        self.__screen_width = self.__screen["width"]
        self.__screen_height = self.__screen["height"]

        self.__ground_height = self.__config.get_ground()["height"]

        self.__current_sprite_index = 0

        self.__last_sprite_change_time = time()
        self.__sprite_change_delay = .15

        self.__coin_sprites = self.__config.get_coin()["sprites"]
        self.__height = self.__config.get_coin()["height"]
        self.__sprites = [
            self.__coin_sprites["front"],
            self.__coin_sprites["side"],
            self.__coin_sprites["25deg"],
            self.__coin_sprites["75deg"],
        ]

        self.__speed = -600

        self.__rect = self.__sprites[self.__current_sprite_index].get_rect(
            topleft=(self.__screen_width + self.__screen_offset, randint(0, self.__screen_height - self.__height - self.__ground_height))
        )

        self.__collected = False

    def get_collected(self): return self.__collected
    def set_collected(self): self.__collected = True

    def draw(self):
        self.__rect = self.__rect.move(self.__speed * self.__config.get_dt(), 0)

        self.__surface.blit(
            self.__sprites[self.__current_sprite_index], self.__rect)

    def check_colision(self, bird_rect):
        has_collide = Rect.colliderect(self.__rect, bird_rect)
        
        if has_collide:
            return True

    def change_sprite(self):
        current_time = time()
        in_sprite_change_delay = current_time - \
            self.__last_sprite_change_time < self.__sprite_change_delay

        if not in_sprite_change_delay:
            self.__current_sprite_index = (self.__current_sprite_index + 1) % \
                len(self.__sprites)

            self.sprite = self.__sprites[self.__current_sprite_index]
            self.__last_sprite_change_time = current_time
