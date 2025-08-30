import random
from static.tile import Tile
import pdb

class Board:

    def __init__(self, rows, cols, chaos):
        self.rows = rows
        self.cols = cols
        self.chaos = chaos
        self.start = None
        self.end = None
        self.tiles = []
        self.assign_start_end()
    
    def assign_start_end(self):
        self.start = (random.randint(0, self.rows - 1,), random.randint(0, self.cols - 1))
        self.end = (random.randint(0, self.rows - 1,), random.randint(0, self.cols - 1))
        while (self.end == self.start):
            self.end = (random.randint(0, self.rows - 1,), random.randint(0, self.cols - 1))
    
    def create_tiles(self):
        for i in range(self.rows):
            self.tiles.append([])
            rows = self.tiles[i]
            for j in range(self.cols):
                rows.append(Tile((i,j)))
    
    def create_neigbors(self):
        for i in range(self.rows):
            for j in range(self.cols):
                current_tile = self.tiles[i][j]
                above_position = (i - 1, j)
                below_position = (i + 1, j)
                right_position = (i, j + 1)
                left_position = (i, j - 1)
                positions = [above_position, below_position, right_position, left_position]
                for position in positions:
                    if (position[0] in range(0, self.rows)) and (position[1] in range(0, self.cols)):
                        target_tile = self.tiles[position[0]][position[1]]
                        if current_tile not in target_tile.neighbors:
                            current_tile.neighbors.append(target_tile)
                            target_tile.neighbors.append(current_tile)
                            



