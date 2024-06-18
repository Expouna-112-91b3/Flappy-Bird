import pygame

from config import Config

from scripts.score import Score
from scripts.background import Background

from scenes.scenes import Scenes

from tools.utils import Utils


class ScoreBoard():
    def __init__(self):
        self.__config = Config()
        self.__background = Background()
        self.__score = Score()

        self.__screen = self.__config.get_screen()
        self.__screen_height = self.__screen["height"] / 2
        self.__surface: pygame.Surface = self.__screen['surface']
        self.__screen_rect = self.__screen['rect']

        self.__board = pygame.Surface((540, 700))
        self.__board.set_alpha(190)
        self.__board.fill((0, 0, 0))
        self.__board_rect = self.__board.get_rect(center=self.__screen_rect.center)
        self.__board_pos = (self.__board_rect.x, self.__board_rect.y - 50)
        
        self.__padding = 25

        self.__title_font = pygame.font.Font("./fonts/default.ttf", 40)
        self.__title_text = Utils.Text(self.__title_font)

        self.__score_font = pygame.font.Font("./fonts/default.ttf", 35)
        self.__score_text = Utils.Text(self.__score_font)

        self.__title = self.__title_text.render("MELHORES PONTUACOES")
        self.__title_rect = self.__title.get_rect(center=self.__screen_rect.center)
        self.__title_pos = (self.__title_rect.x, self.__board_pos[1] + self.__padding)

    def run(self):
        KEYS = pygame.key.get_pressed()

        for _ in pygame.event.get():
            if KEYS[pygame.K_p]:
                self.__config.toggle_debug()

            if KEYS[pygame.K_ESCAPE]:
                self.__config.close_game()

            if KEYS[pygame.K_r]:
                self.__config.set_scene(Scenes.MENU.value)

        self.__background.draw_wallpaper()
        self.__background.draw_ground()

        self.__surface.blit(self.__board, self.__board_pos)

        score_distance = 0
        for i, (player, score) in enumerate(self.__score.get_scores()):
            score = self.__score_text.render(f"{i + 1}. {player} {score} pts")
            score_rect = score.get_rect(center=self.__screen_rect.center)
            score_pos = (score_rect.x, self.__board_pos[1])

            posy = self.__screen_height - 300 + score_distance
            self.__surface.blit(self.__title, self.__title_pos)
            self.__surface.blit(score, (score_pos[0], posy))

            score_distance += 70
