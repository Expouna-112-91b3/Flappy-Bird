from random import randint

import math

from config import Config

import pygame


class Pipe:
    def __init__(self):
        self.__config = Config()

        self.__game_screen = self.__config.get_screen()
        self.__screen = self.__game_screen["surface"]
        self.__screen_width = self.__game_screen["width"]
        self.__screen_height = self.__game_screen["height"]

        self.__bird = self.__config.get_bird()
        self.__bird_height = self.__bird["height"]
        self.__bird_width = self.__bird["width"]

        self.__pipe = self.__config.get_pipe()
        self.__sprite = self.__pipe["sprite"]["default"]
        self.__rotated_sprite = self.__pipe["sprite"]["rotated"]
        self.__sprite_rect = self.__sprite.get_rect()

        self.__space_between_pipes = self.__bird_height * -6

        self.__x_pos = 0
        self.__x = self.__sprite_rect.width
        self.__is_in_screen_limit = False

        self.__offset = randint(-self.__screen_height +
                                self.__pipe["height"] - self.__space_between_pipes, 0)
        self.__top_pipe_y = self.__offset
        self.__bottom_pipe_y = self.__offset + \
            self.__pipe["height"] - self.__space_between_pipes

        """
        por algum motivo o -10 e +2 são necessarios 
        para calcular a posição da ponta dos canos
        """
        self.__hitbox = (
            self.__top_pipe_y - 10 + self.__pipe["height"],
            self.__bottom_pipe_y + 2
        )

    def check_collision(self, bird):
        pygame.draw.rect(
            self.__screen,
            (0, 255, 0),
            pygame.Rect(
                self.__x_pos,
                self.__hitbox[0],
                self.__pipe["width"],
                10), 1)

        pygame.draw.rect(
            self.__screen,
            (255, 0, 0),
            pygame.Rect(
                self.__x_pos,
                self.__hitbox[1],
                self.__pipe["width"],
                10), 1)

        bird_y_pos = bird.get_position()[0]
        bird_x_pos = bird.get_position()[1]
       
        # se o passaro estiver na mesma linha vertical dos canos
        bird_inline_with_pipes = bird_y_pos >= self.__x_pos - self.__bird_width

        print(bird_inline_with_pipes)

        if bird_inline_with_pipes:
            """
            e se ele estiver mais alto que a ponta do cano superior
            ou mais baixo que a ponta do cano inferior ele morre 
            """
            if (bird_x_pos <= self.__hitbox[0] or bird_x_pos >= self.__hitbox[1]):
                bird.die()

    def draw(self):
        # checa se o cano está fora da tela
        if not self.__is_in_screen_limit:
            if (self.__x - self.__sprite_rect.width * 2 > self.__screen_width):
                self.__is_in_screen_limit = True

        # posicao inicial dos canos, um pouco antes do inicio da tela
        self.__x_pos = self.__screen_width - self.__x + self.__sprite_rect.width

        self.__x += 5

        self.__screen.blit(
            self.__rotated_sprite,
            (self.__x_pos, self.__top_pipe_y),
        )
        self.__screen.blit(
            self.__sprite,
            (self.__x_pos, self.__bottom_pipe_y),
        )
