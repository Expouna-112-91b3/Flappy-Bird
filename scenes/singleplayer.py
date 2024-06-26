import pygame
from config import Config

from scripts.background import Background
from scripts.bird import Bird
from scripts.pipe import Pipe
from scripts.score import Score

from scenes.scenes import Scenes

from tools.debugger import Debugger

from scripts.coin import Coin

from random import random

from tools.utils import Utils

class Singleplayer:
    def __init__(self):
        self.__config = Config()
        self.__background = Background()
        self.__bird = Bird()
        self.__score = Score()

        self.__debugger = Debugger(self.__bird)
        
        """
        a geracao de pipes e coins funciona da seguinte forma: a cada ms especificado em
        GENERATE_PIPE_EVENT, um novo pipe é adicionado ao array de pipes;
        dentro do loop do jogo, um for itera esses pipes e desenha cada um
        há uma chance de 10% de a criação de pipe gerar uma moeda

        quando um pipe e/ou moeda sai do jogo, seu(s) index(es) dentro do array de seu(s) array(s) 
        é inserido na variavel (entidade)_to_delete_index e, se existir, é deletado no inicio do loop do jogo
        """
        self.__pipes = []
        self.__pipe_to_delete_index = None

        self.__coins = []
        self.__coin_to_delete_index = None
        self.__coin_event_count = 0

        self.__running = False

        self.__GENERATE_PIPE_EVENT = pygame.USEREVENT + 1

    def reset(self):
        self.__config = Config()
        self.__background = Background()
        self.__bird = Bird()
        self.__score = Score()
        self.__debugger = Debugger(self.__bird)

        pygame.time.set_timer(self.__GENERATE_PIPE_EVENT, 0)
        self.__pipes = []
        self.__pipe_to_delete_index = None

        self.__coins = []
        self.__coin_to_delete_index = None

        self.__running = False

    def run(self):
        if not self.__running:
            pygame.time.set_timer(self.__GENERATE_PIPE_EVENT, 1000)
            self.__running = True

        if self.__pipe_to_delete_index or self.__pipe_to_delete_index == 0:
            del self.__pipes[self.__pipe_to_delete_index]
            self.__pipe_to_delete_index = None

        if self.__coin_to_delete_index or self.__coin_to_delete_index == 0:
            del self.__coins[self.__coin_to_delete_index]
            self.__coin_to_delete_index = None

        KEYS = pygame.key.get_pressed()

        for _ in pygame.event.get():
            if _.type == self.__GENERATE_PIPE_EVENT:
                PIPE = Pipe()
                self.__pipes.append(PIPE)
            
                if Utils.Chances.random_chance(0.2):
                    COIN = Coin(300)
                    self.__coins.append(COIN)

            if KEYS[pygame.K_p]:
                self.__config.toggle_debug()

            if KEYS[pygame.K_ESCAPE]:
                self.__config.close_game()

        if KEYS[pygame.K_w]:
            self.__bird.flap()

        self.__background.draw_wallpaper()

        for i, pipe in enumerate(self.__pipes):
            pipe.draw()

            if pipe.check_collision(self.__bird):
                self.__bird.die()

            if pipe.check_flew_past(self.__bird):
                self.__score.increase()

            if pipe.get_offscreen():
                self.__pipe_to_delete_index = i

        for i, coin in enumerate(self.__coins):
            coin.draw()
            coin.change_sprite()
            if (coin.check_colision(self.__bird.get_current_sprite_rect())
                and not coin.get_collected()):
                coin.set_collected()
                self.__score.increase()
            
            if coin.get_collected():
                self.__coin_to_delete_index = i

        self.__background.draw_ground()

        self.__bird.draw()
        self.__bird.apply_gravity()
        self.__bird.change_sprite()

        self.__score.draw()
        
        if not self.__bird.get_is_alive():
            self.__score.push_score("Jaozin")
            self.__score.reset_score()
            self.reset()
            self.__config.set_scene(Scenes.SCORE_BOARD.value)

        if self.__config.get_is_debugging():
            self.__debugger.draw_debug(self.__pipes)