import pygame
from Modulos.const import *
from pygame.font import Font

class Menu:
    def __init__(self, screen: pygame.Surface):
        self.screen : pygame.Surface = screen 
        self.surf = pygame.image.load(".\Modulos\Assets\Background\Ocean_2\\2.png")
        self.surf2 = pygame.image.load(".\Modulos\Assets\Background\Ocean_2\\3.png")
        self.surf3 = pygame.image.load(".\Modulos\Assets\Background\Ocean_2\\4.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def Run(self):
        pygame.mixer_music.load(".\Modulos\Assets\Music\musica.mp3")
        pygame.mixer_music.play()
        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.screen.blit(source=self.surf2, dest=self.rect)
            self.screen.blit(source=self.surf3, dest=self.rect)
            self.menu_text(50, "Mountain",(255,128,0),(WIN_WIDTH/2, 70))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest= text_rect)