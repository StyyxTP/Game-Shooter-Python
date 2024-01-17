import pygame
import random
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent


class Game():
    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.comet_event = CometFallEvent(self)
        #grp de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        

    def start(self):
        self.random_grp_monstres = [1, random.randint(0,1),  random.randint(0,1)]
        for i in self.random_grp_monstres:
            if i == 1:
                self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        self.is_playing = True

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False
        


    def update(self, screen):
        #applique l'image du joueur
        screen.blit(self.player.image, self.player.rect)
        
        #actualiser les hp du joueur
        self.player.update_health_bar(screen)

        #actualise l'animation du joueur
        self.player.update_animation()

        #actualiser la bar d'evenement du jeu
        self.comet_event.update_bar(screen)

        #récuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()
            

        #récup les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        #récup les comets de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        #applique l'ensemble des images du grp de projectile
        self.player.all_projectiles.draw(screen)
        #applique l'ensemble des images du grp de monstre
        self.all_monsters.draw(screen)
        #applique l'ensemble des images du grp de cometes
        self.comet_event.all_comets.draw(screen)
        
        #verifier si le joueur go à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x <= screen.get_width()-self.player.rect.width:
            self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >= 0:
            self.player.move_left()

    def spawn_monster(self, monster_name):
        self.all_monsters.add(monster_name.__call__(self))
    

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
