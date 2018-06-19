''' Entity is composed of components'''


class Entity():
    '''template will initialize entity'''

    def __init__(self):
        self.id = ""
        self.components ={}

    def getComponents(self):
        return self.components.iterkeys()

    def hasComponent(self, id):
        return id in self.components

    def getComponent(self,id):
        return self.components[id]