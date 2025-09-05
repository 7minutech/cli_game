
class Player:

    def __init__(self, coord=None, tile=None):
        self.coord = coord
        self.tile = tile
        pass

    def reset(self):
        self.tile = None
        self.coord = None 
    