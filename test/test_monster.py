import unittest
from active.monster import Monster
from static.game import Game
from static.board import Board
from static.coordinate import Coordinate

class TestMonster(unittest.TestCase):

    def test_move_alaways_chase(self):
        my_game = Game(Board(1, 3), Monster(always_chase=True))
        my_game.place(my_game.player, Coordinate((0,2)))
        my_game.place(my_game.monster, Coordinate((0,0)))
        self.assertEqual(my_game.monster.move(my_game.player.tile), Coordinate((0,1)))
    
    def test_move_alaways_chase_monster_on_player(self):
        my_game = Game(Board(1, 3), Monster(always_chase=True))
        my_game.place(my_game.player, Coordinate((0,0)))
        my_game.place(my_game.monster, Coordinate((0,0)))
        self.assertIsNone(my_game.monster.move(my_game.player.tile))
    
    def test_contacted_monster_player(self):
        my_game = Game(Board(1, 3), Monster(always_chase=True))
        my_game.place(my_game.player, Coordinate((0,0)))
        my_game.place(my_game.monster, Coordinate((0,2)))
        self.assertTrue(my_game.contacted_monster(Coordinate((0,2))))
    
    def test_contacted_monster_monster(self):
        my_game = Game(Board(1, 3), Monster(always_chase=True))
        my_game.place(my_game.player, Coordinate((0,0)))
        my_game.place(my_game.monster, Coordinate((0,2)))
        self.assertTrue(my_game.contacted_monster(Coordinate((0,0))))

    def test_contacted_monster_false(self):
        my_game = Game(Board(1, 3), Monster(always_chase=True))
        my_game.place(my_game.player, Coordinate((0,0)))
        my_game.place(my_game.monster, Coordinate((0,2)))
        self.assertFalse(my_game.contacted_monster(Coordinate((0,1))))


