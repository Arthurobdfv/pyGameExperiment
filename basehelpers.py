
import pygame

def LoadImage(filePath):
    image = pygame.image.load(filePath).convert_alpha()
    rect = image.get_rect()
    return { 'Image': image, 'Rect': rect }

def LoadSound(filePath):
    sound = pygame.mixer_music.load(filePath)
    return sound