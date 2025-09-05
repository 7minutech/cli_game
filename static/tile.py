from active.player import Player
import pdb
from active.monster import Monster

class Tile:
    
    def __init__(self, coord, neighbors=None, owner=None):
        self.coord = coord
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
        if type(self.owner) is Monster:
            return(f"\u2622")
    
    def __repr__(self):
        return(f"Tile(coordinate:{self.coord}, owner:{self.owner})")

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

    
    def reconnect_neighbors(self, neighbors):
        for neighbor in neighbors:
            self.neighbors.append(neighbor)
            neighbor.neighbors.append(self)
