from enum import Enum
from helpers.helpers import shortest_path_start, hit_roll
from constants.constants import MILD_MOVE_CHANCE, MODERATE_MOVE_CHANCE, STRONG_MOVE_CHANCE, EXTERME_MOVE_CHANCE
import random
import pdb

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
    
    def random_move(self):
        rand_tile = random.choice(self.tile.neighbors)
        return rand_tile.coord
    
    def move(self, player_tile):
        if shortest_path_start(self.tile, player_tile) is None:
            return None
        match (self.aggro):
            case AggroLevel.MILD:
                if (hit_roll(MILD_MOVE_CHANCE)):
                    return shortest_path_start(self.tile, player_tile).coord
                return self.random_move()
            case AggroLevel.MODERATE:
                if (hit_roll(MODERATE_MOVE_CHANCE)):
                    return shortest_path_start(self.tile, player_tile).coord
                return self.random_move()
            case AggroLevel.STRONG:
                if (hit_roll(STRONG_MOVE_CHANCE)):
                    return shortest_path_start(self.tile, player_tile).coord
                return self.random_move()
            case AggroLevel.EXTREME:
                if (hit_roll(EXTERME_MOVE_CHANCE)):
                    return shortest_path_start(self.tile, player_tile).coord
                return self.random_move()
            case _:
                raise Exception("Monster must have an AggroLevel")
        
