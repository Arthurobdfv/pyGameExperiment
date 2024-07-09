import pygame
from abc import ABC, abstractmethod

class Entity2D(ABC):
    def __init__(self, name:str, path:str,position: tuple):
        self.name = name
        self.position :tuple = position
        self.surf = pygame.image.load('./Modulos/Assets/' + path + '.png')
        self.rect = self.surf.get_rect(left=position[0],top=position[1])
        self.speed = 0 

    @abstractmethod
    def move(self):
        pass