import pygame

from scenes.singleplayer import Singleplayer
from config import Config

from scenes.scenes import Scenes

from scenes.menu import Menu

from scenes.score_board import ScoreBoard

from tools.utils import Utils

config = Config()
config.start_screen()
config.setup_images()
Utils.init_font()

MENU = Menu()
SINGLEPLAYER = Singleplayer()
SCORE_BOARD = ScoreBoard()

config.set_scene(Scenes.SCORE_BOARD.value)

running, paused = config.get_running(), config.get_paused()
while running:
    if not config.get_running():
        running = False

    if config.get_paused():
        continue

    match config.get_current_scene():
        case Scenes.MENU.value:
            MENU.run()
        case Scenes.SINGLEPLAYER.value:
            SINGLEPLAYER.run()
        case Scenes.SCORE_BOARD.value:
            SCORE_BOARD.run()
        case __:
            break

    pygame.display.flip()
    config.clock_tick(60)

pygame.quit()
