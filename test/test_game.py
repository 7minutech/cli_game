import unittest
from static.game import Game
from static.board import Board
from active.player import Player
from static.coordinate import Coordinate
from pynput.keyboard import Key
import pdb

class TestGame(unittest.TestCase):

    def test_place_player(self):
        my_game = Game(Board(3, 4, 1.0), Player())
        my_game.place_player(Coordinate((1,1)))
        self.assertTrue(my_game.board.positions[1][1].owner == my_game.player)
    
    def test_move_right(self):
        start = Coordinate((1,1))
        my_game = Game(Board(3, 3, 1.0), Player())
        my_game.place_player(start)
        my_game.move(Key.right)
        self.assertTrue(my_game.board.positions[1][2].owner == my_game.player)

    def test_move_left(self):
        start = Coordinate((1,1))
        my_game = Game(Board(3, 3, 1.0), Player())
        my_game.place_player(start)
        my_game.move(Key.left)
        self.assertTrue(my_game.board.positions[1][0].owner == my_game.player)

    def test_move_up(self):
        start = Coordinate((1,1))
        my_game = Game(Board(3, 3, 1.0), Player())
        my_game.place_player(start)
        my_game.move(Key.up)
        self.assertTrue(my_game.board.positions[0][1].owner == my_game.player)

    def test_move_down(self):
        start = Coordinate((1,1))
        my_game = Game(Board(3, 3, 1.0), Player())
        my_game.place_player(start)
        my_game.move(Key.down)
        self.assertTrue(my_game.board.positions[2][1].owner == my_game.player)
