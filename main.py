import pygame
from math import floor
from screeninfo import get_monitors
from scripts.bird import Bird
from scripts.background import Background
from scripts.pipe import Pipe
from utils import Utils

""" ESPECIFICAÇÕES DOS SPRITES
passaro     34x24
background  288x512
chao        366x112
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

PIPE_SPRITE = pygame.image.load('./sprites/pipe/pipe.png')
PIPE = Pipe(SCREEN, PIPE_SPRITE)

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

        BACKGROUND.draw()
        BIRD.draw()
        BIRD.change_sprite()
        BIRD.apply_gravity()
        # PIPE.draw()

    x, y = BIRD.get_position()
    utils.draw_font(SCREEN, f"Aceleracao: {BIRD.get_acceleration()}")
    utils.draw_font(SCREEN, f"Posicao: {floor(x)}, {floor(y)}", pos=(0, 25))

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()
