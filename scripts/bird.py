from time import time
import pygame


class Bird:
    def __init__(self, screen, sprites, ground_height):
        self.screen = screen
        self.screen_height = screen.get_height()
        self.screen_width = screen.get_width()
        self.ground_height = ground_height

        self.gravity_force = 4

        self.x = self.screen_width / 3
        self.y = (self.screen_height - self.ground_height) / 2

        self.sprites = sprites
        self.current_sprite_index = 0
        self.current_sprite_rect = (
            self.sprites[self.current_sprite_index].get_rect()
        )

        self.last_sprite_change_time = time()
        self.sprite_change_delay = .05

        self.last_flap_time = time()
        self.flap_delay = .15

        self.alive = True
        self.desired_height = None
        self.flap_height = -self.gravity_force * 2.5
        self.acceleration = 0

    def get_acceleration(self): return self.acceleration
    def get_position(self): return (self.y, self.x)
    def get_is_alive(self): return self.alive

    def die(self): self.alive = False

    def draw(self):
        """o passaro
        ao morrer ficara virado pra baixo,
        ele tem rotacao conforme a aceleracao atual
        """
        rotation = 0
        if not self.alive:
            rotation = 180
        else:
            rotation = self.acceleration * 3

        rotated_sprite = pygame.transform.rotate(
            self.sprites[self.current_sprite_index],
            rotation,
        )

        self.screen.blit(
            rotated_sprite,
            (self.x, self.y),
        )

    def change_sprite(self):
        if not self.alive:
            return

        """calcula
        o tempo atual menos o tempo da ultima mudanca de sprite,
        depois vê se o valor é menor que o delay de troca
        de sprites
        
        exemplo:
            current_time = .16
            last_sprite_change_time = 0.8
            self.sprite_change_delay = 0.8
             
            .16 - .8 (output: .8)
            .8 < .8  (output: false) 
            
        ou seja, negando essa funcao retornaremos um true, indicando
        que não há mais delay entre a troca de sprites
        """
        current_time = time()
        in_sprite_change_delay = current_time - \
            self.last_sprite_change_time < self.sprite_change_delay

        if not in_sprite_change_delay:
            """troca
            o sprite atual com base no modulo entre o sprite atual mais um 
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
            self.current_sprite_index = (self.current_sprite_index + 1) % \
                len(self.sprites)

            self.sprite = self.sprites[self.current_sprite_index]
            self.last_sprite_change_time = current_time

    def flap(self):
        if not self.alive:
            return
        
        is_bird_in_game_max_height = (
            self.y + self.current_sprite_rect.height <= 0
        )

        if is_bird_in_game_max_height:
            return

        current_time = time()
        not_in_flap_delay = current_time - self.last_flap_time >= self.flap_delay

        if not_in_flap_delay:
            self.last_flap_time = current_time
            self.acceleration += .5
            if not self.desired_height:
                self.desired_height = self.y + self.flap_height * 6
                return

            self.desired_height += self.flap_height * 6

    def apply_gravity(self):
        if self.desired_height:  # se tiver uma altura desejada
            if self.y > self.desired_height:  # e se ainda não estiver nela
                
                """checa 
                se a altura do passaro mais a hitbox dele
                está encostando no topo da tela
                """
                is_bird_in_game_max_height = (
                    self.y + self.current_sprite_rect.height <= 0
                )

                if is_bird_in_game_max_height:  # se sim, ele reseta a altura desejada e comeca a cair
                    self.desired_height = None
                    return

                """se
                se nao estiver na altura desejada, nem no topo da tela, vai tentar alcanca-la,
                aumentando a aceleração no processo
                """
                self.y += self.flap_height / 1.5
                self.acceleration += .1
                return

            if self.y <= self.desired_height:  # caso ja estiver na altura desejada ou mais alto
                self.desired_height = None     # reseta a altura desejada
                self.acceleration += .1        # aumenta a aceleracao para efeito de planagem
                return

        if not self.alive:
            return

        """checa 
        se a altura do passaro mais a hitbox dele
        está encostando no chao (ele vai morrer
        quando a ``barriga`` atingir no solo)
        """
        is_bird_in_death_condition = (
            self.y + self.current_sprite_rect.height
            > self.screen_height - self.ground_height
        )

        if is_bird_in_death_condition:
            self.die()
            return

        self.acceleration -= .1
        self.y += self.gravity_force
