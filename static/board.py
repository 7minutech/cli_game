import random
from static.tile import Tile

class Board:

    def __init__(self, row, col, chaos):
        self.row = row
        self.col = col
        self.chaos = chaos
        self.start = None
        self.end = None
        self.tiles = []
        self.assign_start_end()
    
    def assign_start_end(self):
        self.start = (random.randint(0, self.row - 1,), random.randint(0, self.col - 1))
        self.end = (random.randint(0, self.row - 1,), random.randint(0, self.col - 1))
        while (self.end == self.start):
            self.end = (random.randint(0, self.row - 1,), random.randint(0, self.col - 1))
    
    def create_tiles(self):
        for i in range(self.row):
            self.tiles.append([])
            row = self.tiles[i]
            for j in range(self.col):
                row.append(Tile((i,j)))



