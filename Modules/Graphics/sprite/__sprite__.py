import pygame
from pygame.locals import *
from renderer import Renderer

class SpriteRender(Renderer):
    def __init__(self, app, filePath):
        self.filePath = filePath
        self.app = app
        self.image :Surface = pygame.image.load(filePath)
        self.imgRect = self.image.get_rect()

    def Render(self):
        print('Render invoked!')

