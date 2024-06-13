import pygame
from pygame.locals import *
from basehelpers import *
# Initializes pyGame
pygame.init()

W_WIDTH = 600
W_HEIGHT = 300
WHITE = (255, 255, 255)
# Pygame considers top left as coord (0,0)
GameWindow = pygame.display.set_mode(size=(W_WIDTH,W_HEIGHT))

Resource = LoadImage('./Assets/GridTile.png')
TileImage = Resource['Image']
TileRect = Resource['Rect']

Music = LoadSound('./Assets/musica.mp3')
# Draw to window

GameClock = pygame.time.Clock()
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.7)

while True:
    GameClock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
            quit();
            #sys.exit();
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        TileRect.centery -= 1
    if pressed_key[pygame.K_s]:
        TileRect.centery += 1
    if pressed_key[pygame.K_d]:
        TileRect.centerx += 1
    if pressed_key[pygame.K_a]:
        TileRect.centerx -= 1
    GameWindow.fill(WHITE)
    GameWindow.blit(source=TileImage, dest=TileRect)
    pygame.display.update()
