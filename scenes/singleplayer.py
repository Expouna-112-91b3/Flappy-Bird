import pygame
from config import Config
from time import time

from scripts.background import Background
from scripts.bird import Bird
from scripts.pipe import Pipe
from scripts.score import Score

from scenes.scenes import Scenes

from tools.debugger import Debugger

class Singleplayer:
    def __init__(self):
        self.__config = Config()
        self.__background = Background()
        self.__bird = Bird()
        self.__score = Score()

        self.__debugger = Debugger(self.__bird)
        
        """
        a geracao de pipes funciona da seguinte forma: a cada ms especificado em
        GENERATE_PIPE_EVENT, um novo pipe é adicionado ao array de pipes;
        dentro do loop do jogo, um for itera esses pipes e desenha cada um

        quando um pipe sai do jogo, seu index dentro do array de pipes é inserido na
        variavel pipe_to_delete_index e, se existir, é deletado no inicio do loop do jogo
        """
        self.__pipes = []
        self.__pipe_to_delete_index = None

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
        self.__running = False

    def run(self):
        if not self.__running:
            pygame.time.set_timer(self.__GENERATE_PIPE_EVENT, 1000)
            self.__running = True

        if self.__pipe_to_delete_index:
            del self.__pipes[self.__pipe_to_delete_index]
            self.__pipe_to_delete_index = None

        KEYS = pygame.key.get_pressed()

        for _ in pygame.event.get():
            if _.type == self.__GENERATE_PIPE_EVENT:
                PIPE = Pipe()
                self.__pipes.append(PIPE)

            if KEYS[pygame.K_p]:
                self.__config.toggle_debug()

            if KEYS[pygame.K_ESCAPE]:
                self.__config.close_game()

        if KEYS[pygame.K_w]:
            self.__bird.flap()

        self.__background.draw_wallpaper()

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
            self.reset()
            self.__config.set_scene(Scenes.SCORE_BOARD.value)

        if self.__config.get_is_debugging():
            self.__debugger.draw_debug(self.__pipes)