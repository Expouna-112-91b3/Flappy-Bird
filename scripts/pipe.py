from random import randint

from config import Config

from scripts.score import Score

from pygame.rect import Rect


class Pipe:
    def __init__(self):
        self.__config = Config()
        self.__score = Score()

        self.__screen = self.__config.get_screen()
        self.__surface = self.__screen["surface"]
        self.__screen_width = self.__screen["width"]

        self.__bird = self.__config.get_bird()
        self.__bird_height = self.__bird["height"]

        self.__pipe = self.__config.get_pipe()
        self.__sprite = self.__pipe["sprite"]["default"]
        self.__rotated_sprite = self.__pipe["sprite"]["rotated"]

        self.__space_between_pipes = self.__bird_height * -5

        self.__offset = randint(-90, 0)
        self.__top_pipe_y = self.__offset
        self.__bottom_pipe_y = self.__offset + \
            self.__pipe["height"] - self.__space_between_pipes

        self.__x_pos = self.__screen_width
        self.__speed = -7.5

        self.__top_pipe_rect: Rect = self.__rotated_sprite.get_rect(
            topleft=(self.__x_pos, self.__top_pipe_y))

        self.__bottom_pipe_rect: Rect = self.__sprite.get_rect(
            topleft=(self.__x_pos, self.__bottom_pipe_y))

        self.__offscreen = False
        self.__bird_flew_past = False

        self.__score = Score()

    def check_collision(self, bird):
        bird_rect = bird.get_current_sprite_rect()

        has_collided_top = Rect.colliderect(self.__top_pipe_rect, bird_rect)
        has_collided_bottom = Rect.colliderect(self.__bottom_pipe_rect, bird_rect)

        if has_collided_top or has_collided_bottom:
            return True
    
    def check_flew_past(self, bird):
        bird_x = bird.get_position()[0]
        if bird_x > self.__top_pipe_rect.x:
            if not self.__bird_flew_past:
                self.__bird_flew_past = True
                return True

    def draw(self):
        self.__top_pipe_rect = self.__top_pipe_rect.move(self.__speed, 0)
        self.__bottom_pipe_rect = self.__bottom_pipe_rect.move(self.__speed, 0)

        if self.__top_pipe_rect.right < 0:
            self.__offscreen = True

        self.__surface.blit(self.__rotated_sprite, self.__top_pipe_rect)
        self.__surface.blit(self.__sprite, self.__bottom_pipe_rect)

    def get_offscreen(self):
        return self.__offscreen
