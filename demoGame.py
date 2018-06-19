from World import World
from Entity import Entity
from TestSystem import TestSystem
import pygame
from pygame.locals import *

clock = pygame.time.Clock()

class DemoGame():
    def __init__(self):
        self.world = World([])

    def run(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.world.processSystems()

            clock.tick(60)

        pygame.quit()
        
if __name__ == '__main__':
    game = DemoGame()
    game.run()