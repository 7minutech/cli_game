import random
from static.tile import Tile
from static.coordinate import Coordinate
from constants.constants import RIGHT, LEFT, UP, DOWN, REMOVAL_SUBTLE_CHANCE, REMOVAL_NOTICEABLE_CHANCE, REMOVAL_INTENSE_CHANCE, REMOVAL_EXTREME_CHANCE
import pdb
from helpers.helpers import hit_roll, path_exists
from enum import Enum

class ChaosLevel(Enum):
    SUBTLE = 1,
    NOTICEABLE = 2,
    INTENSE = 3,
    EXTREME = 4

class Board:

    def __init__(self, rows, cols, chaos=ChaosLevel.SUBTLE):
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
        self.end.exit = True
        self.chance = REMOVAL_SUBTLE_CHANCE
    
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

    def removable_tile(self, tile):
        if tile == self.start or tile == self.end or self.start in tile.neighbors or self.end in tile.neighbors:
            return False
        tile_neighbors = tile.neighbors.copy()
        tile.remove_neighbors()
        if not path_exists(self, self.start, self.end):
            tile.reconnect_neighbors(tile_neighbors)
            return False
        for neighbor in tile_neighbors:
            if not path_exists(self, self.start, neighbor) and not path_exists(self, self.end, neighbor):
                tile.reconnect_neighbors(tile_neighbors)
                return False
        return True

    def handle_chaos(self):
        match self.chaos:
            case ChaosLevel.SUBTLE:
                self.chance = REMOVAL_SUBTLE_CHANCE
            case ChaosLevel.NOTICEABLE:
                self.chance = REMOVAL_NOTICEABLE_CHANCE
            case ChaosLevel.INTENSE:
                self.chance = REMOVAL_INTENSE_CHANCE
            case ChaosLevel.EXTREME:
                self.chance = REMOVAL_EXTREME_CHANCE
            case _:
                raise Exception("Chaos level not set")


    def remove_random_tiles(self):
        chances = (self.rows * self.cols)
        for i in range(chances):
            selected_tile = random.choice(self.tiles)
            if self.removable_tile(selected_tile) and hit_roll(self.chance):
                self.remove_tile(selected_tile)
