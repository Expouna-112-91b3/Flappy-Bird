import pygame
from screeninfo import get_monitors
from entities.bird import Bird
from entities.background import Background

# ESPECIFICAÇÕES DOS SPRITES (px)
# pássaro    = 34x24
# background = 288x512
# chao       = 366x112

# TAMANHO DA TELA DO USUÁRIO
USER_SCREEN = get_monitors()[0]
WIDTH, HEIGHT = USER_SCREEN.width, USER_SCREEN.height

# SETUP INICIAL DO PYGAME 
pygame.init()

# screen = LxA da tela
# clock  = fps
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# construção do background
bg_sprite = pygame.image.load('./sprites/scenario/background.bmp')
ground_sprite = pygame.image.load('./sprites/scenario/ground.bmp')
scaled_bg_image = pygame.transform.scale(bg_sprite, (HEIGHT, WIDTH))
background = Background(screen, scaled_bg_image, ground_sprite)

# construção do pássaro
bird_sprite = pygame.image.load('./sprites/bird/bird-midflap.bmp')
ground_height = ground_sprite.get_rect().height
bird = Bird(screen, bird_sprite, ground_height)

running = True
while running:
    # METODOS DE SAÍDA
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    # APLICANDO GRAVIDADE AO PÁSSARO        
    bird.apply_gravity()
        
    # SPRITES
    background.draw()
    bird.draw()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()