import pygame
from game import Game
pygame.init()

#def une clock (gerer les fps)
clock = pygame.time.Clock()
FPS = 60

#generer la fenetre de jeu
#nom du jeu en haut de la fenetre
pygame.display.set_caption("Shooter") 
#création de la fenetre (l,h)
screen = pygame.display.set_mode((1080,720))

#import et chargement du bg
background = pygame.image.load('PygameAssets_main/bg.jpg')

#charger le jeu
game = Game()

running = True

while running == True:

    #applique le bg du jeu
    screen.blit(background, (0,-307))

    #charger notre banniere
    banner = pygame.image.load('PygameAssets_main/banner.png')
    banner = pygame.transform.scale(banner, (500,500))
    banner_rect = banner.get_rect()
    banner_rect.x = screen.get_width()//4

    play_button = pygame.image.load('PygameAssets_main/button.png')
    play_button = pygame.transform.scale(play_button, (400,150))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = screen.get_width()//3.22
    play_button_rect.y = screen.get_height()//2

    #vérifier si le jeu a commencer ou non
    if game.is_playing:
        #déclencher les instruction de la partie
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    #maj de l'écran
    pygame.display.flip()

    for event in pygame.event.get():
        #permet de fermer la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est enclenché pour lancé projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
    #fixer le nb de fps sur la clock
    clock.tick(FPS)