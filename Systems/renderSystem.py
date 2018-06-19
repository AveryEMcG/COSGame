from System import System
import pygame

class RenderSystem(System):
    def __init__(self, display):
        self.display = display

    def canProcess(self,entity):
        return entity.hasComponent("Renderable")

    def preProcess(self):
        self.display.fill((255,0,255))

    def process(self,entity):
        # TODO set the renderable's position if this entity has a Transform component

        entity.draw(self.display)

    def postProcess(self):
        pygame.display.flip()