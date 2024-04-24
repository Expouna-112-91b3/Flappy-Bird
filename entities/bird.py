import time

class Bird:
    def __init__(self, screen, sprites, ground_height):
        # informacoes da tela para desenho do passaro
        self.screen = screen
        self.screen_height = screen.get_height()
        self.screen_width = screen.get_width()
        self.ground_height = ground_height
        
        # gravidade sob o passaro
        self.gravity_force = 4.5
        
        # posicao x e y do passaro
        self.x = self.screen_width / 3
        self.y = (self.screen_height - self.ground_height) / 2
        
        # paint de sprites e respectivas logicas
        self.sprites = sprites
        self.current_sprite_index = 0
        self.current_sprite_rect = self.sprites[self.current_sprite_index].get_rect()
        self.last_sprite_change_time = time.time()
        self.sprite_change_delay = .15
        
        # status do passaro
        self.alive = True
        self.desired_height = None
        self.flap_height = -self.gravity_force * 2

    def draw(self):
        self.screen.blit(
            self.sprites[self.current_sprite_index],
            (self.x, self.y)
        )
        
    def change_sprite(self):
        if not self.alive: return
        
        current_time = time.time()
        not_in_sprite_change_delay = current_time - self.last_sprite_change_time >= self.sprite_change_delay
        if not_in_sprite_change_delay:
            self.current_sprite_index = (self.current_sprite_index + 1) % len(self.sprites)
            self.sprite = self.sprites[self.current_sprite_index]
            self.last_sprite_change_time = current_time

    def flap(self):
        if not self.desired_height:
            self.desired_height = self.y + self.flap_height
            return
        
        self.desired_height += self.flap_height

    def apply_gravity(self):
        # se houver uma altura desejada
        if self.desired_height:
            # e se ainda não estiver nela
            if self.y > self.desired_height:
                # vai tentar alcanca-la
                self.y += self.flap_height
                return
            
            # caso ja estiver na altura desejada ou mais alto,
            # reseta a altura desejada
            if self.y <= self.desired_height:
                self.desired_height = None
                return
        
        if not self.alive: return
        
        # checa se a (altura do passaro + a hitbox dele)
        # está encostando no chao, ou seja, ele vai morrer
        # quando a barriga encostar no solo
        is_bird_in_death_condition = (
            self.y + self.current_sprite_rect.height 
            > self.screen_height - self.ground_height
        )
        
        if is_bird_in_death_condition: 
            self.alive = False
            return
        
        self.y += self.gravity_force
