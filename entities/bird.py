import time
import pygame


class Bird:
    def __init__(self, screen, sprites, ground_height):
        self.screen = screen
        self.screen_height = screen.get_height()
        self.screen_width = screen.get_width()
        self.ground_height = ground_height

        self.gravity_force = 4

        self.x = self.screen_width / 3
        self.y = (self.screen_height - self.ground_height) / 2

        self.sprites = sprites
        self.current_sprite_index = 0
        self.current_sprite_rect = self.sprites[self.current_sprite_index].get_rect(
        )
        self.last_sprite_change_time = time.time()
        self.sprite_change_delay = .15

        self.alive = True
        self.desired_height = None
        self.flap_height = -self.gravity_force * 2
        self.accelleration = 0

    def draw(self):
        rotation = 20 if self.desired_height else 0

        rotated_sprite = pygame.transform.rotate(
            self.sprites[self.current_sprite_index], rotation)

        self.screen.blit(
            rotated_sprite,
            (self.x, self.y)
        )

    def change_sprite(self):
        if not self.alive:
            return

        current_time = time.time()

        not_in_sprite_change_delay = current_time - \
            self.last_sprite_change_time >= self.sprite_change_delay

        if not_in_sprite_change_delay:
            self.current_sprite_index = (
                self.current_sprite_index + 1) % len(self.sprites)

            self.sprite = self.sprites[self.current_sprite_index]
            self.last_sprite_change_time = current_time

    def flap(self):
        if not self.alive:
            return

        if not self.desired_height:
            self.desired_height = self.y + self.flap_height * 1.5
            return

        self.desired_height += self.flap_height * 1.5

    def apply_gravity(self):
        if self.desired_height:               # se houver uma altura desejada
            if self.y > self.desired_height:  # e se ainda não estiver nela
                self.y += self.flap_height    # vai tentar alcanca-la
                return

            if self.y <= self.desired_height:  # caso ja estiver na altura desejada ou mais alto
                self.desired_height = None     # reseta a altura desejada
                return

        if not self.alive:
            return

        """
        checa se a (altura do passaro + a hitbox dele)
        está encostando no chao (ele vai morrer
        quando a ''barriga'' atingir no solo)
        """
        is_bird_in_death_condition = (
            self.y + self.current_sprite_rect.height > self.screen_height - self.ground_height)

        if is_bird_in_death_condition:
            self.alive = False
            return

        self.y += self.gravity_force
