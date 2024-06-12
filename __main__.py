import pygame
from pygame.locals import *
# Initializes pyGame
pygame.init()

W_WIDTH = 600
W_HEIGHT = 300
WHITE = (255, 255, 255)
# Pygame considers top left as coord (0,0)
GameWindow = pygame.display.set_mode(size=(W_WIDTH,W_HEIGHT))

# Load image
TileImage = pygame.image.load('./Assets/GridTile.png').convert_alpha()
TileImage_rect = TileImage.get_rect()

# Draw to window

GameClock = pygame.time.Clock()

while True:
    GameClock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
            quit();
            #sys.exit();
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        TileImage_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        TileImage_rect.centery += 1
    if pressed_key[pygame.K_d]:
        TileImage_rect.centerx += 1
    if pressed_key[pygame.K_a]:
        TileImage_rect.centerx -= 1
    GameWindow.fill(WHITE)
    GameWindow.blit(source=TileImage, dest=TileImage_rect)
    pygame.display.update()