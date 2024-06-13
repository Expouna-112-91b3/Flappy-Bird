import pygame

from time import time

from scripts.bird import Bird
from scripts.background import Background
from scripts.pipe import Pipe

from tools.utils import Utils
from config import Config
from tools.debugger import Debugger

import mediapipe.python.solutions.hands as mp_hands

""" ESPECIFICAÇÕES DOS SPRITES
passaro     34x24
background  288x512
chao        366x112
cano        x
"""
config = Config()

pygame.init()
config.start_screen()
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

PIPE = Pipe()

DEBUGGER = Debugger(BIRD)
Utils.init_font()
running, paused = True, False

# Isto está aqui por conta que quando incluído em um Loop pode causar lag, pela minha experiência (Felipe)
with mp_hands.Hands(min_detection_confidence = 0.5, min_tracking_confidence=0.5, max_num_hands=1, static_image_mode= False) as hands:
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

            BIRD.handControl(hands)

            BACKGROUND.draw_wallpaper()

            #current_time = time()
            #not_in_generation_delay = current_time - \
            #    last_generation_time >= generation_delay

            #if not_in_generation_delay:
            #   last_generation_time = current_time
            #   PIPE = Pipe()
            #    pipes.append(PIPE)

            #for pipe in pipes:
            #    pipe.draw()
            #    pipe.check_collision(BIRD)

            PIPE.draw()
            PIPE.check_collision(BIRD)

            BACKGROUND.draw_ground()
            BIRD.draw()
            if not BIRD.get_is_alive():
                paused = True
            BIRD.change_sprite()
            #BIRD.apply_gravity()

            if config.get_is_debugging():
                DEBUGGER.draw_debug()

        pygame.display.flip()
        config.clock_tick(60)

pygame.quit()
