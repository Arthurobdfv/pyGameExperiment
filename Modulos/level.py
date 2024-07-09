import pygame
from Modulos.entityfactory import EntityFactory

class Level:
    def __init__(self, window: pygame.Surface, nome: str, menu_option: str):
        self.window :Surface = window 
        self.name = nome
        self.mode = menu_option
        self.entity_list: list[Entity2D] = []
        self.entity_list.append(EntityFactory.get_entity('Level1', (0,0)))

    def Run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
            pygame.display.flip()            
        pass