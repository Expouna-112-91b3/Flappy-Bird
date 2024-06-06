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
        self.__screen_height = self.__screen["height"]

        self.__bird = self.__config.get_bird()
        self.__bird_height = self.__bird["height"]
        self.__bird_width = self.__bird["width"]

        self.__pipe = self.__config.get_pipe()
        self.__sprite = self.__pipe["sprite"]["default"]
        self.__rotated_sprite = self.__pipe["sprite"]["rotated"]

        self.__space_between_pipes = self.__bird_height * -5

        """
        implementa um ruído para aumentar a variabildade de altura dos gaps
        entre canos, sendo o valor de variabilidade entre x e 0
        onde x < 0
        
        tem randint(0, n) de chance, sendo n a unidade de porcentagem
        ex: randint(0, 6) == 60%
        onde x > 0
        """
        self.__noise = 0 if randint(0, 6) == 0 else randint(-300, 0)
        self.__offset_calc = -self.__screen_height + self.__pipe["height"] - self.__space_between_pipes - self.__noise
        self.__offset = randint(self.__offset_calc, 0)

        self.__top_pipe_y = self.__offset
        self.__bottom_pipe_y = self.__offset + \
            self.__pipe["height"] - self.__space_between_pipes

        self.__x_pos = self.__screen_width
        self.__speed = -7.5

        self.__top_pipe_rect: Rect = self.__rotated_sprite.get_rect(
            topleft=(self.__x_pos, self.__top_pipe_y))

        self.__bottom_pipe_rect: Rect = self.__sprite.get_rect(
            topleft=(self.__x_pos, self.__bottom_pipe_y))

        self.__hitbox = (
            self.__top_pipe_y + self.__pipe["height"],
            self.__bottom_pipe_y - 10
        )

        self.__is_offscreen = False

        self.__bird_flew_past = False

        self.__score = Score()

    def check_collision(self, bird):
        # hitboxes
        # pygame.draw.rect(self.__screen, (255, 0, 0), self.__top_pipe_rect, 1)
        # pygame.draw.rect(self.__screen, (255, 0, 0), self.__bottom_pipe_rect, 1)

        bird_y_pos, bird_x_pos = bird.get_position()

        # se o passaro estiver na mesma linha vertical dos canos
        pipe_start = self.__top_pipe_rect.left - self.__bird_width
        pipe_end = self.__top_pipe_rect.right + 6
        bird_inline_with_pipes = pipe_start <= bird_y_pos <= pipe_end

        if bird_inline_with_pipes:
            # se ele estiver mais alto que a ponta do cano superior ou mais baixo que a ponta do cano inferior, ele morre
            if (bird_x_pos <= self.__hitbox[0] or bird_x_pos >= self.__hitbox[1]):
                bird.die()
            else:
                if not self.__bird_flew_past:
                    self.__bird_flew_past = True
                    self.__score.increase()

    def draw(self):
        self.__top_pipe_rect = self.__top_pipe_rect.move(self.__speed, 0)
        self.__bottom_pipe_rect = self.__bottom_pipe_rect.move(self.__speed, 0)

        # checa se o cano está fora da tela
        if self.__top_pipe_rect.right < 0:
            self.__is_offscreen = True

        self.__surface.blit(self.__rotated_sprite, self.__top_pipe_rect)
        self.__surface.blit(self.__sprite, self.__bottom_pipe_rect)

    def get_is_offscreen(self):
        return self.__is_offscreen
