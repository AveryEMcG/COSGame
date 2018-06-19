from Entity import Entity
import pygame
from Systems.renderSystem import RenderSystem

class World:
    def __init__(self, templates):
        self.entities = []
        self.systems = []
        self.templates = templates
        self.display = pygame.display.set_mode((1024, 768))

        self.systems.append(RenderSystem(self.display))

    def processSystems(self):
        '''Iterates through systems, processing all entities'''
        for s in self.systems:
            s.preProcess()

            for e in self.entities:
                if s.canProcess(e):
                    s.process(e)

            s.postProcess()


