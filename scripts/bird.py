from time import time
import pygame

from config import Config


class Bird:
    def __init__(self):
        self.__config = Config()
        self.__surface = self.__config.get_screen()["surface"]
        self.__ground = self.__config.get_ground()
        self.__user_screen = self.__config.get_monitor()

        self.__ground_height = self.__ground["height"]
        self.__gravity_force = 4

        self.__x = self.__user_screen["width"] / 3
        self.__total_ground_height = self.__user_screen["height"] - \
            self.__ground_height
        self.__y = self.__total_ground_height / 2

        self.__bird_sprites = self.__config.get_bird()["sprites"]
        self.__sprites = [
            self.__bird_sprites["downflap"],
            self.__bird_sprites["midflap"],
            self.__bird_sprites["upflap"],
        ]

        self.__current_sprite_index = 0
        self.__current_sprite_rect = self.__sprites[self.__current_sprite_index].get_rect(center=(self.__x, self.__y))

        self.__last_sprite_change_time = time()
        self.__sprite_change_delay = .05

        self.__last_flap_time = time()
        self.__flap_delay = .15

        self.__alive = True
        self.__desired_height = None
        self.__flap_height = -self.__gravity_force * 2.5
        self.__acceleration = 0

    def get_acceleration(self): return self.__acceleration
    def get_position(self): return (self.__current_sprite_rect.x, self.__current_sprite_rect.y)
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
            rotation = self.__acceleration * 3

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
        in_sprite_change_delay = current_time - self.__last_sprite_change_time < self.__sprite_change_delay

        if not in_sprite_change_delay:
            self.__current_sprite_index = (self.__current_sprite_index + 1) % len(self.__sprites)
            self.sprite = self.__sprites[self.__current_sprite_index]
            self.__last_sprite_change_time = current_time

    def flap(self):
        if not self.__alive:
            return

        is_bird_in_game_max_height = (
            self.__current_sprite_rect.top <= 0
        )

        if is_bird_in_game_max_height:
            return

        current_time = time()
        not_in_flap_delay = current_time - self.__last_flap_time >= self.__flap_delay

        if not_in_flap_delay:
            self.__last_flap_time = current_time
            self.__acceleration += .5
            if not self.__desired_height:
                self.__desired_height = self.__current_sprite_rect.centery + self.__flap_height * 6
                return

            self.__desired_height += self.__flap_height * 6

    def apply_gravity(self):
        if not self.__alive:
            return

        if self.__desired_height:
            if self.__current_sprite_rect.centery > self.__desired_height:
                is_bird_in_game_max_height = (
                    self.__current_sprite_rect.top <= 0
                )

                if is_bird_in_game_max_height:
                    self.__desired_height = None
                    return

                self.__current_sprite_rect = self.__current_sprite_rect.move(0, self.__flap_height / 1.5)
                self.__acceleration += .1
                return

            if self.__current_sprite_rect.centery <= self.__desired_height:
                self.__desired_height = None
                self.__acceleration += .1
                return

        is_bird_in_death_condition = (
            self.__current_sprite_rect.bottom > self.__total_ground_height
        )

        if is_bird_in_death_condition:
            self.die()
            return

        self.__acceleration -= .1
        self.__current_sprite_rect = self.__current_sprite_rect.move(0, self.__gravity_force)
