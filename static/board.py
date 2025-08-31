import random
from static.tile import Tile
from static.coordinate import Coordinate
from constants.direction import *
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
        self.fill_positions()
        self.create_neigbors()
    
    def assign_start_end(self):
        self.start = Coordinate((random.choice(range(self.rows)), random.choice(range(self.cols))))
        self.end = Coordinate((random.choice(range(self.rows)), random.choice(range(self.cols))))
        while (self.end == self.start):
            self.end = Coordinate((random.choice(range(self.rows)), random.choice(range(self.cols))))
    
    def fill_positions(self):
        for i in range(self.rows):
            self.positions.append([])
            rows = self.positions[i]
            for j in range(self.cols):
                tile = Tile(position=Coordinate((i,j)))
                rows.append(tile)
                self.tiles.append(tile)
    
    def create_neigbors(self):
        for tile in self.tiles:
            for position in self.possible_positions(tile):
                if self.valid_position(position):
                    target_tile = self.positions[position.row][position.col]
                    if tile not in target_tile.neighbors:
                        tile.neighbors.append(target_tile)
                        target_tile.neighbors.append(tile)
    
    def possible_positions(self, tile):
        return [tile.position + UP, tile.position + DOWN, tile.position + RIGHT, tile.position + LEFT]

    def valid_position(self, position): 
        return (position.row in range(self.rows) and position.col in range(self.cols))  

    def format_board(self):
        display_str = "\n\u230C " + " ".join(("\u23BB" * self.cols)) + " \u230D"
        for row in range(self.rows):
            display_str += "\n"
            row_arr = ["|"]
            for col in range(self.cols):
                row_arr.append(str(self.positions[row][col]))
            row_arr.append("|")
            display_str += (" ".join(row_arr))
        display_str += ("\n\u230E " + " ".join(("\u23BB" * self.cols)) + " \u230F")
        return (display_str)     

    def display(self):
        print(self.format_board())



