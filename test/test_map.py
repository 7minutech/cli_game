import unittest
from static.board import Board
from static.tile import Tile

class TestMap(unittest.TestCase):

    def test_start_in_range(self):
        test_board = Board(5, 4, 1.0)
        self.assertTrue(test_board.start[0] in range(0, test_board.row) and test_board.start[1] in range(0, test_board.col))
    
    def test_end_in_range(self):
        test_board = Board(5, 4, 1.0)
        self.assertTrue(test_board.end[0] in range(0, test_board.row) and test_board.end[1] in range(0, test_board.col))
    
    def test_create_tiles(self):
        row, col = (5, 3)
        test_board = Board(row, col, 1.0)
        test_board.create_tiles()
        for i in range(row):
            for j in range(col):
                current_tile = test_board.tiles[i][j]
                self.assertEqual(current_tile.position, (i, j))
                self.assertIsInstance(current_tile, Tile)
        