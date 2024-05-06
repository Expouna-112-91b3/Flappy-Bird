from screeninfo import get_monitors
import pygame


class Config:
    def __init__(self):
        # monitor
        self.__user_screen = get_monitors()[0]
        self.__screen_width = self.__user_screen.width
        self.__screen_height = self.__user_screen.height
        
        # fps
        self.__clock = pygame.time.Clock()
        self.__max_fps = 60

        # wallpaper
        self.__wallpaper_sprite = pygame.image.load('./sprites/scenario/background.bmp')
        
        # ground
        self.__ground_sprite = pygame.image.load('./sprites/scenario/ground.bmp')
        self.__ground_sprite_rect = self.__ground_sprite.get_rect()
       
        # pipe
        self.__pipe_sprite = pygame.image.load('./sprites/pipe/pipe.png')
        self.__pipe_sprite_rect = self.__pipe_sprite.get_rect()

        # bird
        self.__bird_downflap_sprite = pygame.image.load('./sprites/bird/downflap.bmp')
        self.__bird_midflap_sprite = pygame.image.load('./sprites/bird/midflap.bmp')
        self.__bird_upflap_sprite = pygame.image.load('./sprites/bird/upflap.bmp')
        self.__bird_rect = self.__bird_midflap_sprite.get_rect()

    def get_user_screen(self):
        return {
            "width": self.__screen_width,
            "height": self.__screen_height,
        }

    def get_wallpaper(self):
        return {
            "sprite": self.__wallpaper_sprite,
        }        

    def get_ground(self): 
        return {
            "sprite": self.__ground_sprite,
            "rect": {
                "width": self.__ground_sprite_rect.width,
                "height": self.__ground_sprite_rect.height,
            }
        }
        
    def get_pipe(self):
        return {
            "sprite": self.__pipe_sprite,
            "rect": {
                "width": self.__pipe_sprite_rect.width,
                "height": self.__pipe_sprite_rect.height,
            }
        }
    
    def get_bird(self):
        return {
            "sprites": {
                "downflap": self.__bird_downflap_sprite,
                "midflap": self.__bird_midflap_sprite,
                "upflap": self.__bird_upflap_sprite,
            },
            "rect": {
                "width": self.__bird_rect.width,
                "height": self.__bird_rect.height
            }
        }

    def start_screen(self):
        return pygame.display.set_mode((
            self.__screen_width,
            self.__screen_height,
        ))
        
    def clock_tick(self, framerate):
        return self.__clock.tick(framerate)

    def get_max_fps(self):
        return self.__max_fps
    
    def get_fps(self):
        return self.__clock.get_fps()
