from Modulos.background import Background
from Modulos.const import *

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:    
            case 'Level1':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1', f'Ocean_7/{i+1}',position))
                    list_bg.append(Background(f'Level1', f'Ocean_7/{i+1}',(WIN_WIDTH, 0)))
                return list_bg