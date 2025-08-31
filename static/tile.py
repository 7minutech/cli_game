from active.player import Player

class Tile:
    
    def __init__(self, position, neighbors=None, owner=None):
        self.position = position
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
        self.owner = owner
    
    def __str__(self):
        if self.owner is None:
            return(f"\u2395")
        if type(self.owner) is Player:
            return(f"\u2302")
    
    def __repr__(self):
        return(f"Tile(position:{self.position}, owner:{self.owner})")
