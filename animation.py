import pygame
import random

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name, size=(200,200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'PygameAssets_main/{name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(name)
        self.animation = False
    
    def strat_animation(self):
        self.animation = True

    def animate(self, loop=False):
        if self.animation and loop==False:
            self.current_image += random.randint(1, 2)
            if self.current_image >= len(self.images):
                self.current_image = 0
                self.animation = False
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

        if self.animation and loop==True:
            self.current_image += random.randint(0, 1)
            if self.current_image >= len(self.images):
                self.current_image = 0
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)
            

def load_animation_images(name):
    images = []
    path = f'PygameAssets_main/{name}/{name}'
    for i in range(1, 24):
        image_path = f'{path}{i}.png'
        images.append(pygame.image.load(image_path))

    return images

animations = {
    'mummy' : load_animation_images('mummy'),
    'player' : load_animation_images('player'),
    'alien' : load_animation_images('alien')
}