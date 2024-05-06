import pygame
from math import floor
from screeninfo import get_monitors
from scripts.bird import Bird
from scripts.background import Background
from scripts.pipe import Pipe
from utils import Utils
from time import time

""" ESPECIFICAÇÕES DOS SPRITES
passaro     34x24
background  288x512
chao        366x112
cano        x
"""

USER_SCREEN = get_monitors()[0]
WIDTH, HEIGHT = USER_SCREEN.width, USER_SCREEN.height

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

BG_SPRITE = pygame.image.load('./sprites/scenario/background.bmp')
GROUND_SPRITE = pygame.image.load('./sprites/scenario/ground.bmp')
SCALED_BG_IMAGE = pygame.transform.scale(BG_SPRITE, (HEIGHT, WIDTH))
BACKGROUND = Background(
    SCREEN,
    SCALED_BG_IMAGE,
    GROUND_SPRITE,
)

DOWNFLAP_SPRITE = pygame.image.load('./sprites/bird/downflap.bmp')
MIDFLAP_SPRITE = pygame.image.load('./sprites/bird/midflap.bmp')
UPFLAP_SPRITE = pygame.image.load('./sprites/bird/upflap.bmp')
BIRD_SPRITES = [
    DOWNFLAP_SPRITE,
    MIDFLAP_SPRITE,
    UPFLAP_SPRITE,
]

GROUND_HEIGHT = GROUND_SPRITE.get_rect().height
BIRD = Bird(
    SCREEN,
    BIRD_SPRITES,
    GROUND_HEIGHT,
)


"""geracao
de pipes funciona da seguinte forma: a cada segundo especificado em
generation_delay, um novo pipe é adicionado ao array de pipes;
dentro do loop do jogo, um for itera esses pipes e desenha cada um
"""
PIPE_SPRITE = pygame.image.load('./sprites/pipe/pipe.png')
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
                MIDFLAP_SPRITE.get_rect().height,
                PIPE_SPRITE
            )
            pipes.append(PIPE)

        for i in range(len(pipes) - 1):
            if pipes[i].is_in_screen_limit:
                pipes.pop(i)
            else:
                pipes[i].draw()

        BACKGROUND.draw_ground()
        BIRD.draw()
        if not BIRD.alive:
            paused = True
        BIRD.change_sprite()
        BIRD.apply_gravity()

    x, y = BIRD.get_position()
    utils.draw_font(SCREEN, f"Passaro:")
    utils.draw_font(
        SCREEN, 
        f"Aceleracao: {"{:.2f}".format(BIRD.get_acceleration())}", 
        pos=(20, 30),
    )
    utils.draw_font(SCREEN, f"Posicao: {floor(x)}, {floor(y)}", pos=(20, 60))

    utils.draw_font(SCREEN, f"Tela:", pos=(0, 90))
    utils.draw_font(
        SCREEN,
        f"Dimensoes: {SCREEN.get_height()}, {SCREEN.get_width()}",
        pos=(20, 120),
    )
    utils.draw_font(SCREEN, f"Canos visiveis: {len(pipes) - 1}", pos=(20, 150))
    utils.draw_font(SCREEN, f"FPS: {"{:.0f}".format(CLOCK.get_fps())}", pos=(20, 180))

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()
