from pygame import transform
from config import Config


class Pipe:
    def __init__(self):
        self.config = Config()
        
        self.game_screen = self.config.get_screen()
        self.screen = self.game_screen["surface"]
        self.screen_width = self.game_screen["width"]
        self.screen_height = self.game_screen["height"]

        self.bird = self.config.get_bird()
        self.bird_height = self.bird["height"]
        
        self.ground = self.config.get_ground()
        self.ground_height = self.ground["height"]

        self.pipe = self.config.get_pipe()
        self.sprite = self.pipe["sprite"]["default"]
        self.rotated_sprite = self.pipe["sprite"]["rotated"]
        self.sprite_rect = self.sprite.get_rect()

        self.space_between_pipes = self.bird_height * -5
        self.top_pipe_y = self.screen_height - self.sprite_rect.height - self.ground_height
        self.x = self.sprite_rect.width
        self.is_in_screen_limit = False
    
    def draw(self):
        if (self.x - self.sprite_rect.width * 2 > self.screen_width):
            self.is_in_screen_limit = True

        base_x_pos = self.screen_width - self.x + self.sprite_rect.width
        self.x += 4

        self.screen.blit(
            self.sprite,
            (base_x_pos, self.top_pipe_y),
        )
        self.screen.blit(
            self.rotated_sprite,
            (base_x_pos, self.space_between_pipes),
        )
