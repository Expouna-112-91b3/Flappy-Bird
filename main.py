import pygame

from time import time

from scripts.bird import Bird
from scripts.background import Background
from scripts.pipe import Pipe

from tools.utils import Utils
from config import Config
from tools.debugger import Debugger

""" ESPECIFICAÇÕES DOS SPRITES
passaro     34x24
background  288x512
chao        366x112
cano        x
"""
config = Config()

pygame.init()
config.start_screen()
config.setup_images()
SCREEN = config.get_screen()["surface"]
BACKGROUND = Background()
BIRD = Bird()

"""
a geracao de pipes funciona da seguinte forma: a cada segundo especificado em
generation_delay, um novo pipe é adicionado ao array de pipes;
dentro do loop do jogo, um for itera esses pipes e desenha cada um
"""
last_generation_time = time()
generation_delay = 1.5
pipes = []
off_screen_pipes = []

DEBUGGER = Debugger(BIRD)
Utils.init_font()

running, paused = True, False
while running:
    for pipe_index in off_screen_pipes:
        del pipes[pipe_index]
    off_screen_pipes.clear()

    KEYS = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if KEYS[pygame.K_PAUSE]:
                paused = not paused

            if KEYS[pygame.K_p]:
                config.toggle_debug()

            if not paused:
                if KEYS[pygame.K_w]:
                    BIRD.flap()

        if event.type == pygame.QUIT:
            running = False

    if KEYS[pygame.K_ESCAPE]:
                running = False

    if not paused:
        if KEYS[pygame.K_w]:
            BIRD.flap()

        BACKGROUND.draw_wallpaper()
        current_time = time()
        not_in_generation_delay = current_time - \
            last_generation_time >= generation_delay

        if not_in_generation_delay:
           last_generation_time = current_time
           PIPE = Pipe()
           pipes.append(PIPE)

        for i, pipe in enumerate(pipes):
            pipe.draw()
            pipe.check_collision(BIRD)
            if pipe.get_is_offscreen():
                off_screen_pipes.append(i)

        BACKGROUND.draw_ground()

        BIRD.draw()
        BIRD.apply_gravity()
        BIRD.change_sprite()
        if not BIRD.get_is_alive():
            paused = True

        if config.get_is_debugging():
            DEBUGGER.draw_debug(pipes)

    pygame.display.flip()
    config.clock_tick(60)


pygame.quit()
