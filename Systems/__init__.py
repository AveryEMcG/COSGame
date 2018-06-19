import pygame

class spriteComponent():
    def __init__(self,filename, position=(0,0)):
        self.surface = pygame.image.load(filename)
        self.position = position
        
    def draw(self,display):
        display.blit(self.surface,self.position)

    def setPosition(self,position):
        self.position = position
