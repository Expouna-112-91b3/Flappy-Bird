from time import time
import pygame

from config import Config


class Bird:
    def __init__(self):
        self.__config = Config()
        self.__surface = self.__config.get_screen()["surface"]
        self.__user_screen = self.__config.get_monitor()


        self.__x = self.__user_screen["width"] / 3

        self.__y = 400
        self.__y = 400

        self.__bird_sprites = self.__config.get_bird()["sprites"]
        self.__sprites = [
            self.__bird_sprites["downflap"],
            self.__bird_sprites["midflap"],
            self.__bird_sprites["upflap"],
        ]

        self.__current_sprite_index = 0
        self.__current_sprite_rect = self.__sprites[self.__current_sprite_index].get_rect(
            center=(self.__x, self.__y))

        self.__last_sprite_change_time = time()
        self.__sprite_change_delay = .05

        self.__alive = True
        self.__acceleration = 0

    def get_acceleration(self): return self.__acceleration
    def get_position(self): return (
        self.__current_sprite_rect.x, self.__current_sprite_rect.y)

    def get_is_alive(self): return self.__alive

    def get_current_sprite_rect(self):
        return self.__current_sprite_rect

    def die(self): self.__alive = False

    def draw(self):
        """
        O passaro ficara virado pra baixo ao morrer,
        ele tem rotacao conforme a aceleracao atual
        """
        rotation = 0
        if not self.__alive:
            rotation = 180
        else:
            rotation = self.__acceleration * 0.5

        rotated_sprite = pygame.transform.rotate(
            self.__sprites[self.__current_sprite_index],
            rotation,
        )

        self.__surface.blit(
            rotated_sprite,
            self.__current_sprite_rect.topleft,
        )

    def change_sprite(self):
        if not self.__alive:
            return

        current_time = time()
        in_sprite_change_delay = current_time - \
            self.__last_sprite_change_time < self.__sprite_change_delay

        if not in_sprite_change_delay:
            self.__current_sprite_index = (
                self.__current_sprite_index + 1) % len(self.__sprites)
            self.sprite = self.__sprites[self.__current_sprite_index]
            self.__last_sprite_change_time = current_time

    def hand_movement(self, direction):
        pos = (0, direction / 9)
        self.__current_sprite_rect = self.__current_sprite_rect.move(pos)