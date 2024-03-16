import pygame
import math
from game import Game
pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 70

# generer la fenetre de notre jeu
pygame.display.set_caption("Jeu de chute de comete")
screen = pygame.display.set_mode((1080, 720))

# importer de charger l'arriere plan du jeu
background = pygame.image.load('PygameAssets-main/bg.jpg')

# importer charger notre banniere
banner = pygame.image.load('PygameAssets-main/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer charger notre bouton pour lancer la partie
player_button = pygame.image.load('PygameAssets-main/button.png')
player_button = pygame.transform.scale(player_button, (400, 150))
player_button_rect = player_button.get_rect()
player_button_rect.x = math.ceil(screen.get_width() / 3.33)
player_button_rect.y = math.ceil(screen.get_height() / 2)

# charger notre jeu
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    # verifier si notre jeu a commence ou non
    if game.is_playing:
        # declancher les instructions de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commence
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(player_button, player_button_rect)
        screen.blit(banner, banner_rect)


    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
            # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True

           # detecter si la touche espace est enclenchee pour lancer notre projectile
           if event.key == pygame.K_SPACE:
               if game.is_playing:
                    game.player.launch_projectile()
               else:
                   # mettre le jeu en mode "lancer"
                   game.start()
                   # jouer le son
                   game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton
            if player_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancer"
                game.start()
                # jouer le son
                game.sound_manager.play('click')
    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)