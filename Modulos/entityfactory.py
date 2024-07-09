from Modulos.background import Background

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:    
            case 'Level1':
                return Background(f'Level1', 'Ocean_7/6',position)