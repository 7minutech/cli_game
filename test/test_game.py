import unittest
from static.game import Game
from static.board import Board
from active.player import Player

class TestGame(unittest.TestCase):

    def test_place_player(self):
        my_game = Game(Board(3, 4, 1.0), Player())
        my_game.board.fill_positions()
        my_game.place_player((1,1))
        self.assertTrue(my_game.board.positions[1][1] == my_game.player)