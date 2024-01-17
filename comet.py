import pygame
import random


class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        # self.surface = pygame.display.set_mode((1080,720))
        self.image = pygame.image.load('PygameAssets_main/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 4)
        self.rect.x = random.randint(0, 1000)
        self.rect.y = -random.randint(100, 200)
        # self.rect.y = -random.randint(0, self.surface.get_height())
        # self.rect.x = random.randint(0, self.surface.get_width())
        self.comet_event = comet_event
        

    def remove(self):
        self.comet_event.all_comets.remove(self)

        if len(self.comet_event.all_comets)==0:
            self.comet_event.reset_percent()
            self.comet_event.game.start()
        

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= random.randint(400, 420):
            self.remove()
            if len(self.comet_event.all_comets)==0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.remove()
            self.comet_event.game.player.damage(20)