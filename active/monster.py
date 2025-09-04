from enum import Enum
from helpers.helpers import shortest_path_start

class AggroLevel(Enum):
    MILD = 1
    MODERATE = 2
    STRONG = 3
    EXTREME = 4

class Monster:

    def __init__(self, coord=None, aggro=AggroLevel.MILD, always_chase=False):
        self.coord = coord
        self.aggro = aggro
        self.always_chase = always_chase
        self.tile = None
    
    def move(self, player_tile):
        if shortest_path_start(self.tile, player_tile) is None:
            return None
        return shortest_path_start(self.tile, player_tile).coord