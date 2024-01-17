import pygame
import random
import animation


class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=120):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = .3
        self.offset = offset
        self.image = pygame.image.load('PygameAssets_main/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1000, 1300)
        self.rect.y = random.randint(420, 430) - offset 
        self.strat_animation()
        
    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(5, self.default_speed)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = random.randint(1000, 1300)
            self.health = self.max_health
            self.velocity = random.randint(5, self.default_speed)
            self.rect.y = random.randint(420, 435) - self.offset
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()

        
    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        #dessiner les hp, surface, couleur, emplacement
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 12, self.rect.y - 30, self.max_health, 5])
        pygame.draw.rect(surface,(111, 210, 46), [self.rect.x + 12, self.rect.y - 30, self.health, 5])
        

    def forward(self):
        #le déplacement ne se fait que si il n'y a pas de collision avec un grp de joueurs
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else :
            self.game.player.damage(self.attack)

class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130), 0)
        self.set_speed(7)

class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 120)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(5)