import pygame
from Modulos.const import *
from Modulos.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))

    def Run(self):

        while True:
            menu = Menu(self.screen)
            menu.Run()
            pass


