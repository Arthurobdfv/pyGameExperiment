from Modulos.entity2d import Entity2D
from pygame import *

class Background(Entity2D):
    def __init__(self, name:str, path: str, position:tuple):
        #self.window = window
        Entity2D.__init__(self, name, 'Background/' + path, position)

    def move(self):
        pass