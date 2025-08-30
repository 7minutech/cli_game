class Tile:
    
    def __init__(self, position, neigbors=None, owner=None):
        self.position = position
        self.neigbors = neigbors
        self.owner = owner
