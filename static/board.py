import random
from static.tile import Tile
import pdb

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
    
    def create_neigbors(self):
        for i in range(self.row):
            for j in range(self.col):
                current_tile = self.tiles[i][j]
                above_position = (i - 1, j)
                below_position = (i + 1, j)
                right_position = (i, j + 1)
                left_position = (i, j - 1)
                positions = [above_position, below_position, right_position, left_position]
                for position in positions:
                    if (position[0] in range(0, self.row)) and (position[1] in range(0, self.col)):
                        target_tile = self.tiles[position[0]][position[1]]
                        if current_tile not in target_tile.neighbors:
                            current_tile.neighbors.append(target_tile)
                            target_tile.neighbors.append(current_tile)
                            



