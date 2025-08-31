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
        self.positions = []
        self.tiles = []
        self.assign_start_end()
    
    def assign_start_end(self):
        self.start = (random.choice(range(self.rows)), random.choice(range(self.cols)))
        self.end = (random.choice(range(self.rows)), random.choice(range(self.cols)))
        while (self.end == self.start):
            self.end = (random.choice(range(self.rows)), random.choice(range(self.cols)))
    
    def create_tiles(self):
        for i in range(self.rows):
            self.positions.append([])
            rows = self.positions[i]
            for j in range(self.cols):
                tile = Tile(position=(i,j))
                rows.append(tile)
                self.tiles.append(tile)
    
    def create_neigbors(self):
        for tile in self.tiles:
            for position in self.possible_positions(tile):
                if self.valid_position(position):
                    target_tile = self.positions[position[0]][position[1]]
                    if tile not in target_tile.neighbors:
                        tile.neighbors.append(target_tile)
                        target_tile.neighbors.append(tile)
    
    def possible_positions(self, tile):
        row = tile.position[0]
        col = tile.position[1]
        return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

    def valid_position(self, position): 
        return (position[0] in range(self.rows) and position[1] in range(self.cols))                      



