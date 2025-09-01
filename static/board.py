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
        self.fill_positions()
        self.assign_start_end()
        self.create_neigbors()
    
    def assign_start_end(self):
        self.start = self.positions[(random.choice(range(self.rows)))][random.choice(range(self.cols))]
        self.end = self.positions[(random.choice(range(self.rows)))][random.choice(range(self.cols))]
        while (self.end == self.start):
            self.end = self.positions[(random.choice(range(self.rows)))][random.choice(range(self.cols))]
    
    def fill_positions(self):
        for i in range(self.rows):
            self.positions.append([])
            rows = self.positions[i]
            for j in range(self.cols):
                tile = Tile(Coordinate((i,j)))
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
        return [tile.coord + UP, tile.coord + DOWN, tile.coord + RIGHT, tile.coord + LEFT]

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
        display_str = display_str.replace("None", " ")
        return (display_str)     

    def display(self):
        print(self.format_board())

    def remove_tile(self, target):
        target.remove_neighbors()
        self.positions[target.coord.row][target.coord.col] = None

    def path_exists(self, start, target, queue=None, visited=None):
        if queue is None and visited is None:
            queue = [start]
            visited = []
        current_tile = queue[0]
        if current_tile == target:
            return True
        for neighbor in current_tile.neighbors:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
        visited.append(queue.pop(0))
        if len(queue) == 0:
            return False
        return self.path_exists(target, start, queue, visited)
        


