from Modulos.entity2d import Entity2D
from pygame import *
from Modulos.const import *

class Background(Entity2D):
    def __init__(self, name:str, path: str, position:tuple):
        #self.window = window
        self.path = path[-1]
        Entity2D.__init__(self, name, 'Background/' + path, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.path]
        if(self.rect.right <= 0):
            self.rect.left = WIN_WIDTH
        pass