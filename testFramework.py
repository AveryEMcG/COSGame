from World import World
import unittest
from Entity import Entity
from TestSystem import TestSystem

class Test(unittest.TestCase):
    def testSample(self):
        testSystem = TestSystem()
        world = World([testSystem],[])
        
        testEntity = Entity()
        testEntity.id = 0
        world.entities.append(testEntity)

        testEntity2 = Entity()
        testEntity2.id = "This id should print too"
        world.entities.append(testEntity2)

        world.processSystems()
        
if __name__ == '__main__':
    unittest.main()