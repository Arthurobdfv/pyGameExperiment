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
        self.menu_option = 0
        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.screen.blit(source=self.surf2, dest=self.rect)
            self.screen.blit(source=self.surf3, dest=self.rect)
            self.menu_text(50, "Mountain", ORANGE_TEXT_COLOR,(WIN_WIDTH/2, 70))
            
            self.render_menu(self.menu_option)
            pygame.display.flip()
            selected_input = self.handle_input()
            if(selected_input != None):
                return selected_input


    def handle_input(self):
        selected_option = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.menu_option = (self.menu_option + 1) % len(MENU_OPTION)
                if event.key == pygame.K_UP:
                    self.menu_option = (self.menu_option - 1) % len(MENU_OPTION)
                if event.key == pygame.K_RETURN:
                    selected_option = MENU_OPTION[self.menu_option]
        return selected_option

    def render_menu(self, selected_menu):
            for i in range(len(MENU_OPTION)):
                color = WHITE_TEXT_COLOR
                if(i == selected_menu):
                    color = YELLOW_TEXT_COLOR
                self.menu_text(20, MENU_OPTION[i], color,(WIN_WIDTH/2, 200 + 30*i))


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest= text_rect)