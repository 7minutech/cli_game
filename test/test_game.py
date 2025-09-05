import unittest
from io import StringIO
from unittest.mock import patch
from static.game import Game
from static.board import Board
from active.player import Player
from active.monster import Monster
from static.coordinate import Coordinate
from constants.constants import MAX_AGGRO
from helpers.helpers import furthest_coord
from pynput.keyboard import Key
import pdb

class TestGame(unittest.TestCase):

    def test_place_player(self):
        my_game = Game(Board(3, 4, 1.0), Player())
        my_game.place(my_game.player, Coordinate((1,1)))
        self.assertTrue(my_game.board.positions[1][1].owner == my_game.player)
    
    def test_move_right(self):
        start = Coordinate((1,1))
        my_game = Game(Board(3, 3, 1.0), Player())
        my_game.place(my_game.player, start)
        my_game.move(Key.right)
        self.assertTrue(my_game.board.positions[1][2].owner == my_game.player)

    def test_move_left(self):
        start = Coordinate((1,1))
        my_game = Game(Board(3, 3, 1.0), Player())
        my_game.place(my_game.player, start)
        my_game.move(Key.left)
        self.assertTrue(my_game.board.positions[1][0].owner == my_game.player)

    def test_move_up(self):
        start = Coordinate((1,1))
        my_game = Game(Board(3, 3, 1.0), Player())
        my_game.place(my_game.player, start)
        my_game.move(Key.up)
        self.assertTrue(my_game.board.positions[0][1].owner == my_game.player)

    def test_move_down(self):
        start = Coordinate((1,1))
        my_game = Game(Board(3, 3, 1.0), Player())
        my_game.place(my_game.player, start)
        my_game.move(Key.down)
        self.assertTrue(my_game.board.positions[2][1].owner == my_game.player)
    
    def test_valid_move_false(self):
        start = Coordinate((0,2))
        my_game = Game(Board(3, 3, 1.0), Player())
        my_game.place(my_game.player, start)
        self.assertFalse(my_game.valid_move(Key.right))
    
    def test_valid_move_true(self):
        start = Coordinate((0,2))
        my_game = Game(Board(3, 3, 1.0), Player())
        my_game.place(my_game.player, start)
        self.assertTrue(my_game.valid_move(Key.left))
    
    def test_move_checked_invalid(self):
        start = Coordinate((0,2))
        my_game = Game(Board(3, 3, 1.0), Player())
        my_game.place(my_game.player, start)
        invalid_message = "\nInvalid move\n"
        
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            my_game.move_checked(Key.right)
            output = mock_stdout.getvalue()
            self.assertEqual(output, invalid_message)
    
    def test_move_checked_valid(self):
        start = Coordinate((0,2))
        my_game = Game(Board(3, 3, 1.0), Player())
        my_game.place(my_game.player, start)
        invalid_message = "\nInvalid move\n"
        
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            my_game.move_checked(Key.down)
            output = mock_stdout.getvalue()
            self.assertNotEqual(output, invalid_message)
    
    def test_initial_monster_placement(self):
        my_game = Game(Board(3,3), Player(), Monster())
        my_game.place_entities_start()
        monster_start_coord = furthest_coord(my_game.board.start.coord, my_game.board.tiles)
        self.assertEqual(my_game.board.positions[monster_start_coord.row][monster_start_coord.col].owner, my_game.monster)


