from pygame import transform


class Pipe:
    def __init__(self, screen, ground_height, bird_height, sprite):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        self.bird_height = bird_height
        self.ground_height = ground_height

        self.sprite = sprite
        self.rotated_sprite = transform.rotate(
            self.sprite,
            180,
        )
        self.sprite_rect = self.sprite.get_rect()

        self.x = self.sprite_rect.width
        self.is_in_screen_limit = False


    def draw(self):
        if (self.x - self.sprite_rect.width * 2 > self.screen_width):
            self.is_in_screen_limit = True

        pipe_base_x_position = self.screen_height - self.sprite_rect.height
        pipe_base_y_position = self.screen_width - self.x + self.sprite_rect.width
        self.x += 4

        self.screen.blit(
            self.sprite,
            (pipe_base_y_position, pipe_base_x_position - self.ground_height),
        )
        self.screen.blit(
            self.rotated_sprite,
            # o espaco entre os canos eh igual ao tamanho do passaro 
            # vezes o multiplicador especificado (negativo)
            (pipe_base_y_position, self.bird_height * -5),
        )
        
