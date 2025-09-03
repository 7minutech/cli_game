from enum import Enum

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