import pygame

from config import Config

from scripts.score import Score
from scripts.background import Background

from scenes.scenes import Scenes


class ScoreBoard():
    def __init__(self):
        self.__config = Config()
        self.__background = Background()
        self.__score = Score()

        self.__screen = self.__config.get_screen()
        self.__scren_width = self.__screen["width"] / 2
        self.__screen_height = self.__screen["height"] / 2
        self.__surface: pygame.Surface = self.__screen['surface']
        self.__screen_rect = self.__screen['rect']

        self.__board = pygame.Surface((550, 750))
        self.__board.set_alpha(190)
        self.__board.fill((0, 0, 0))
        self.__board_pos = self.__board.get_rect(center=self.__screen_rect.center)
        self.__board_pos = (self.__board_pos.x, self.__board_pos.y - 50)

        self.__font = pygame.font.Font("./fonts/default.ttf", 40)

    def run(self):
        KEYS = pygame.key.get_pressed()

        for _ in pygame.event.get():
            if KEYS[pygame.K_p]:
                self.__config.toggle_debug()

            if KEYS[pygame.K_ESCAPE]:
                self.__config.close_game()

            if KEYS[pygame.K_r]:
                self.__config.set_scene(Scenes.SINGLEPLAYER.value)

        self.__background.draw_wallpaper()
        self.__background.draw_ground()

        self.__surface.blit(self.__board, self.__board_pos)

        score_distance = 0
        for i, (player, score) in enumerate(self.__score.get_scores()):
            text_surface = self.__font.render(
                f"{i + 1}. {player} - {score}", False, (255, 255, 255))

            posx = self.__scren_width - text_surface.get_width() / 2
            posy = self.__screen_height - 390 + score_distance

            self.__surface.blit(text_surface, (posx, posy))
            score_distance += 70
