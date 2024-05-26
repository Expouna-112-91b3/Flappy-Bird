from time import time
import pygame

from config import Config


class Bird:
    def __init__(self):
        self.__config = Config()
        self.__surface = self.__config.get_screen()["surface"]
        self.__ground = self.__config.get_ground()
        self.__user_screen = self.__config.get_monitor()

        self.__ground_height = self.__ground["height"]
        self.__gravity_force = 4

        self.__x = self.__user_screen["width"] / 3
        self.__total_ground_height = self.__user_screen["height"] - \
            self.__ground_height
        self.__y = self.__total_ground_height / 2

        self.__bird_sprites = self.__config.get_bird()["sprites"]
        self.__sprites = [
            self.__bird_sprites["downflap"],
            self.__bird_sprites["midflap"],
            self.__bird_sprites["upflap"],
        ]

        self.__current_sprite_index = 0
        self.__current_sprite_rect = (
            self.__sprites[self.__current_sprite_index].get_rect()
        )

        self.__last_sprite_change_time = time()
        self.__sprite_change_delay = .05

        self.__last_flap_time = time()
        self.__flap_delay = .15

        self.__alive = True
        self.__desired_height = None
        self.__flap_height = -self.__gravity_force * 2.5
        self.__acceleration = 0

    def get_acceleration(self): return self.__acceleration
    def get_position(self): return (self.__x, self.__y)
    def get_is_alive(self): return self.__alive

    def die(self): self.__alive = False

    def draw(self):
        """
        O passaro ficara virado pra baixo ao morrer,
        ele tem rotacao conforme a aceleracao atual
        """
        rotation = 0
        if not self.__alive:
            rotation = 180
        else:
            rotation = self.__acceleration * 3

        rotated_sprite = pygame.transform.rotate(
            self.__sprites[self.__current_sprite_index],
            rotation,
        )

        self.__surface.blit(
            rotated_sprite,
            (self.__x, self.__y),
        )

    def change_sprite(self):
        if not self.__alive:
            return

        """
        calcula o tempo atual menos o tempo da ultima mudanca de sprite,
        depois vê se o valor é menor que o delay de troca
        de sprites
        
        exemplo:
            current_time = .16
            last_sprite_change_time = 0.8
            self.__sprite_change_delay = 0.8
             
            .16 - .8 (output: .8)
            .8 < .8  (output: false) 
            
        ou seja, negando essa funcao retornaremos um true, indicando
        que não há mais delay entre a troca de sprites
        """
        current_time = time()
        in_sprite_change_delay = current_time - \
            self.__last_sprite_change_time < self.__sprite_change_delay

        if not in_sprite_change_delay:
            """
            troca o sprite atual com base no modulo entre o sprite atual mais um 
            e o tamanho do array de sprites

            exemplo 1:
                current_sprite_index = 2
                len(sprites) = 3

                (2 + 1) % 3 (output: 0)
                então volta pro sprite 0

            exemplo 2:
                current_sprite_index = 1
                len(sprites) = 3

                (1 + 1) %  3 (output: 2)
                então avança o sprite para o sprite 2
            """
            self.__current_sprite_index = (self.__current_sprite_index + 1) % \
                len(self.__sprites)

            self.sprite = self.__sprites[self.__current_sprite_index]
            self.__last_sprite_change_time = current_time

    def flap(self):
        if not self.__alive:
            return

        is_bird_in_game_max_height = (
            self.__y + self.__current_sprite_rect.height <= 0
        )

        if is_bird_in_game_max_height:
            return

        current_time = time()
        not_in_flap_delay = current_time - self.__last_flap_time >= self.__flap_delay

        if not_in_flap_delay:
            self.__last_flap_time = current_time
            self.__acceleration += .5
            if not self.__desired_height:
                self.__desired_height = self.__y + self.__flap_height * 6
                return

            self.__desired_height += self.__flap_height * 6

    def apply_gravity(self):
        if not self.__alive:
            return

        if self.__desired_height:  # se tiver uma altura desejada
            if self.__y > self.__desired_height:  # e se ainda não estiver nela
                """
                checa se a altura do passaro mais a hitbox dele
                está encostando no topo da tela
                """
                is_bird_in_game_max_height = (
                    self.__y + self.__current_sprite_rect.height <= 0
                )

                if is_bird_in_game_max_height:  # se sim, ele reseta a altura desejada e comeca a cair
                    self.__desired_height = None
                    return

                """
                se nao estiver na altura desejada, nem no topo da tela, vai tentar alcanca-la,
                aumentando a aceleração no processo
                """
                self.__y += self.__flap_height / 1.5
                self.__acceleration += .1
                return

            if self.__y <= self.__desired_height:  # caso ja estiver na altura desejada ou mais alto
                self.__desired_height = None     # reseta a altura desejada
                self.__acceleration += .1        # aumenta a aceleracao para efeito de planagem
                return

        """
        checa se a altura do passaro mais a hitbox dele
        está encostando no chao (ele vai morrer
        quando a ``barriga`` atingir no solo)
        """
        is_bird_in_death_condition = (
            self.__y + self.__current_sprite_rect.height
            > self.__total_ground_height
        )

        if is_bird_in_death_condition:
            self.die()
            return

        self.__acceleration -= .1
        self.__y += self.__gravity_force
