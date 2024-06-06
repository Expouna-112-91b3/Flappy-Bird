import pygame
from config import Config
from time import time

from scripts.background import Background
from scripts.bird import Bird
from scripts.pipe import Pipe

from scenes.scenes import Scenes

from tools.debugger import Debugger

from score import Score

class Singleplayer:
    def __init__(self):
        self.__config = Config()
        self.__background = Background()
        self.__bird = Bird()
        self.__score = Score()

        self.__debugger = Debugger(self.__bird)
        
        """
        a geracao de pipes funciona da seguinte forma: a cada segundo especificado em
        generation_delay, um novo pipe é adicionado ao array de pipes;
        dentro do loop do jogo, um for itera esses pipes e desenha cada um

        quando um pipe sai do jogo, seu index dentro do array de pipes é inserido na
        variavel pipe_to_delete_index e, se existir, é deletado no inicio do loop do jogo
        """
        self.__last_generation_time = time()
        self.__generation_delay = 1
        self.__pipes = []
        self.__pipe_to_delete_index = None

    def reset(self):
        self.__config = Config()
        self.__background = Background()
        self.__bird = Bird()
        self.__score = Score()
        self.__debugger = Debugger(self.__bird)
        self.__last_generation_time = time()
        self.__generation_delay = 1
        self.__pipes = []
        self.__pipe_to_delete_index = None

    def run(self):
        if self.__pipe_to_delete_index:
            del self.__pipes[self.__pipe_to_delete_index]
            self.__pipe_to_delete_index = None

        KEYS = pygame.key.get_pressed()

        for _ in pygame.event.get():
            if KEYS[pygame.K_p]:
                self.__config.toggle_debug()

            if KEYS[pygame.K_ESCAPE]:
                self.__config.close_game()

        if KEYS[pygame.K_w]:
            self.__bird.flap()

        self.__background.draw_wallpaper()
        current_time = time()
        not_in_generation_delay = current_time - \
            self.__last_generation_time >= self.__generation_delay

        if not_in_generation_delay:
            self.__last_generation_time = current_time
            PIPE = Pipe()
            self.__pipes.append(PIPE)

        for i, pipe in enumerate(self.__pipes):
            pipe.draw()
            pipe.check_collision(self.__bird)
            if pipe.get_is_offscreen():
                self.__pipe_to_delete_index = i

        self.__background.draw_ground()

        self.__bird.draw()
        self.__bird.apply_gravity()
        self.__bird.change_sprite()

        self.__score.draw()

        if not self.__bird.get_is_alive():
            self.__score.push_score("Jaozin")
            self.__score.reset_score()
            self.__config.set_scene(Scenes.SCORE_BOARD.value)
            self.reset()

        if self.__config.get_is_debugging():
            self.__debugger.draw_debug(self.__pipes)