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

        self.__ground = self.__config.get_ground()
        self.__ground_height = self.__ground["height"]

        self.__pipe = self.__config.get_pipe()
        self.__sprite = self.__pipe["sprite"]["default"]
        self.__rotated_sprite = self.__pipe["sprite"]["rotated"]
        self.__sprite_rect = self.__sprite.get_rect()

        self.__space_between_pipes = self.__bird_height * -5
        self.__top_pipe_y = self.__screen_height - \
            self.__sprite_rect.height - self.__ground_height
        self.__x = self.__sprite_rect.width
        self.__is_in_screen_limit = False

    def check_collision(self, bird):
        """
        se a hitbox do passaro encostar na hitbox do cano,
        horizontalmente ou verticalmente, ele morre
        """
        bird_has_collided = (1)

    def draw(self):
        # checa se o cano está fora da tela
        if not self.__is_in_screen_limit:
            if (self.__x - self.__sprite_rect.width * 2 > self.__screen_width):
                self.__is_in_screen_limit = True

        # posicao inicial dos canos, um pouco antes do inicio da tela
        x_pos = self.__screen_width - self.__x + self.__sprite_rect.width

        self.__x += 5

        self.__screen.blit(
            self.__sprite,
            (x_pos, self.__top_pipe_y),
        )
        self.__screen.blit(
            self.__rotated_sprite,
            (x_pos, self.__space_between_pipes),
        )
