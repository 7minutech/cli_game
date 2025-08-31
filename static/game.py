from static.board import Board
from active.player import Player

class Game:

    def __init__(self, board, player):
        self.board = board
        self.player = player
    
    def place_player(self, position):
        self.board.positions[position[0]][position[1]] = self.player

