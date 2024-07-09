import pygame
from Modulos.const import *
from Modulos.menu import Menu
from Modulos.level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))

    def Run(self):

        while True:
            menu = Menu(self.screen)
            selected_option = menu.Run()
            print(selected_option)
            if selected_option in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.screen, "Level1", selected_option)
                level_return = level.Run()
            else:
                self.Quit_Game()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.Quit_Game()
            pass
    
    def Quit_Game(self):
        pygame.quit()
        quit()
        


