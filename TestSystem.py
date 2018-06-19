from System import System

class TestSystem(System):
    def __init__(self):
        pass
    
    def canProcess(self,entity):
        return True

    def process(self,entity):
        print ("processed "+ str(entity.id))