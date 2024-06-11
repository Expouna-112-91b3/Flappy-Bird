import pygame

from scenes.singleplayer import Singleplayer
from scenes.scenes import Scenes
from scenes.menu import Menu
from scenes.score_board import ScoreBoard

from config import Config

CONFIG = Config()
CONFIG.start_screen()
CONFIG.setup_images()
pygame.font.init()

MENU = Menu()
SINGLEPLAYER = Singleplayer()
SCORE_BOARD = ScoreBoard()

CONFIG.set_scene(Scenes.MENU.value)

running = CONFIG.get_running()
while running:
    if not CONFIG.get_running():
        running = False

    match CONFIG.get_current_scene():
        case Scenes.MENU.value:
            MENU.run()
        case Scenes.SINGLEPLAYER.value:
            SINGLEPLAYER.run()
        case Scenes.SCORE_BOARD.value:
            SCORE_BOARD.run()
        case __:
            break

    pygame.display.flip()
    dt = CONFIG.clock_tick(30) / 1000
    CONFIG.set_dt(dt)

pygame.quit()
