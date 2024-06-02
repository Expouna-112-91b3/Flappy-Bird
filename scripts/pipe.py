from random import randint

from config import Config


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

        self.__space_between_pipes = self.__bird_height * -6

        self.__offset = randint(-self.__screen_height +
                                self.__pipe["height"] - self.__space_between_pipes, 0)
        self.__top_pipe_y = self.__offset
        self.__bottom_pipe_y = self.__offset + \
            self.__pipe["height"] - self.__space_between_pipes

        self.__x_pos = self.__screen_width
        self.__speed = -5

        self.__top_pipe_rect = self.__rotated_sprite.get_rect(
            topleft=(self.__x_pos, self.__top_pipe_y))
        self.__bottom_pipe_rect = self.__sprite.get_rect(
            topleft=(self.__x_pos, self.__bottom_pipe_y))

        self.__hitbox = (
            self.__top_pipe_y + self.__pipe["height"],
            self.__bottom_pipe_y - 10
        )

        self.__is_offscreen = False
        
        self.__bird_flew_past = False

    def check_collision(self, bird, score):
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

        if not self.__bird_flew_past:
            if bird_x_pos >= self.__top_pipe_rect.centerx:
                self.__bird_flew_past = True
                score.increase()

    def draw(self):
        move_distance = self.__speed
        self.__top_pipe_rect = self.__top_pipe_rect.move(move_distance, 0)
        self.__bottom_pipe_rect = self.__bottom_pipe_rect.move(
            move_distance, 0)

        # checa se o cano está fora da tela
        if self.__top_pipe_rect.right < 0:
            self.__is_offscreen = True

        self.__screen.blit(self.__rotated_sprite, self.__top_pipe_rect)
        self.__screen.blit(self.__sprite, self.__bottom_pipe_rect)

    def get_is_offscreen(self):
        return self.__is_offscreen
