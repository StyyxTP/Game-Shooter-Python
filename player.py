import pygame
from projectile import Projectile
import animation
#creer une premiere classe qui va etre notre joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 4
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 390

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()
        

    def launch_projectile(self):
        # if not self.game.check_collision(self, self.game.all_monsters):
            #creer une nouvelle instance de projectile
            self.all_projectiles.add(Projectile(self))
            self.strat_animation()
            self.game.sound_manager.play("tir")
            



    def move_right(self):
        #si le joueur n'est pas au cac d'un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    
    def move_left(self):
        # if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x -= self.velocity

    
    def update_health_bar(self, surface):
        #dessiner les hp, surface, couleur, emplacement
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 50, self.rect.y + 10, self.max_health, 7])
        pygame.draw.rect(surface,(111, 210, 46), [self.rect.x + 50, self.rect.y + 10, self.health, 7])
        
    def update_animation(self):
        self.animate()