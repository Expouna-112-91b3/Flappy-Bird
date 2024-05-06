import pygame

from math import floor
from time import time

from scripts.bird import Bird
from scripts.background import Background
from scripts.pipe import Pipe
from utils import Utils
from config import Config

""" ESPECIFICAÇÕES DOS SPRITES
passaro     34x24
background  288x512
chao        366x112
cano        x
"""
config = Config()

pygame.init()
SCREEN = config.start_screen()
USER_SCREEN = config.get_user_screen()
WALLPAPER = config.get_wallpaper()
GROUND = config.get_ground()

SCALED_BG_IMAGE = pygame.transform.scale(
    WALLPAPER["sprite"],
    (USER_SCREEN["height"], USER_SCREEN["width"]),
)

BACKGROUND = Background(
    SCREEN,
    SCALED_BG_IMAGE,
    GROUND["sprite"],
)

BIRD = config.get_bird()
BIRD_SPRITES = BIRD["sprites"]

GROUND_HEIGHT = GROUND["rect"]["height"]
BIRD = Bird(
    SCREEN,
    [
        BIRD_SPRITES["downflap"],
        BIRD_SPRITES["midflap"],
        BIRD_SPRITES["upflap"],
    ],
    GROUND_HEIGHT,
)

pipe_sprite = pygame.image.load('./sprites/pipe/pipe.png')

"""geracao
de pipes funciona da seguinte forma: a cada segundo especificado em
generation_delay, um novo pipe é adicionado ao array de pipes;
dentro do loop do jogo, um for itera esses pipes e desenha cada um
"""
PIPE = config.get_pipe()
last_generation_time = time()
generation_delay = 1.5
pipes = []

utils = Utils()
utils.init_font()
running, paused = True, False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    KEYS = pygame.key.get_pressed()
    if KEYS[pygame.K_ESCAPE]:
        running = False

    if KEYS[pygame.K_PAUSE]:
        paused = not paused

    if KEYS[pygame.K_p]:
        config.toggle_debug()

    if not paused:
        if KEYS[pygame.K_w]:
            BIRD.flap()

        BACKGROUND.draw_wallpaper()

        current_time = time()
        not_in_generation_delay = current_time - \
            last_generation_time >= generation_delay

        if not_in_generation_delay:
            last_generation_time = current_time
            PIPE = Pipe(
                SCREEN,
                GROUND_HEIGHT,
                BIRD_SPRITES["midflap"].get_rect().height,
                pipe_sprite
            )
            pipes.append(PIPE)

        for pipe in pipes:
            pipe.draw()

        BACKGROUND.draw_ground()
        BIRD.draw()
        if not BIRD.alive:
            paused = True
        BIRD.change_sprite()
        BIRD.apply_gravity()

        if config.get_is_debugging():
            x, y = BIRD.get_position()
            utils.draw_font(SCREEN, f"Passaro:")
            utils.draw_font(
                SCREEN,
                f"Aceleracao: {"{:.2f}".format(BIRD.get_acceleration())}",
                pos=(20, 30),
            )
            utils.draw_font(SCREEN, f"Posicao: {floor(x)}, {
                            floor(y)}", pos=(20, 60))
            utils.draw_font(SCREEN, f"Tela:", pos=(0, 90))
            utils.draw_font(
                SCREEN,
                f"Dimensoes: {SCREEN.get_height()}, {SCREEN.get_width()}",
                pos=(20, 120),
            )
            utils.draw_font(SCREEN, f"Canos visiveis: {
                            len([]) - 1}", pos=(20, 150))
            utils.draw_font(SCREEN, f"FPS: {"{:.0f}".format(
                config.get_fps())}", pos=(20, 180))
            utils.draw_font(SCREEN, f"FPS: {"{:.0f}".format(
                BACKGROUND.ground_movement_x)}", pos=(20, 210))

    pygame.display.flip()
    config.clock_tick(60)

pygame.quit()
