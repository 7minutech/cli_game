from active.player import Player
import pdb

class Tile:
    
    def __init__(self, coordinate, neighbors=None, owner=None):
        self.coordinate = coordinate
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
        return(f"Tile(coordinate:{self.coordinate}, owner:{self.owner})")

    def remove_neighbor(self, target):
        if target in self.neighbors:
            for i in range(len(self.neighbors)):
                if self.neighbors[i] == target:
                    target_index = i
            self.neighbors.pop(target_index)
            target.remove_neighbor(self)
        return
    
    def remove_neighbors(self):
        for neighbor in self.neighbors.copy():
            self.remove_neighbor(neighbor)
