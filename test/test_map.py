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
    
    def test_create_neigbors_2x2(self):
        row, col = (2, 2)
        test_board = Board(row, col, 1.0)
        test_board.create_tiles()
        test_board.create_neigbors()

        top_left = test_board.tiles[0][0]
        bottom_left = test_board.tiles[1][0]
        top_right = test_board.tiles[0][1]
        bottom_right = test_board.tiles[1][1]
        
        self.assertCountEqual(top_left.neighbors, [bottom_left, top_right])
        self.assertCountEqual(bottom_left.neighbors, [top_left, bottom_right])
        self.assertCountEqual(top_right.neighbors, [top_left, bottom_right])
        self.assertCountEqual(bottom_right.neighbors, [top_right, bottom_left])
    
    def test_create_neigbors_3x3(self):
        row, col = (3, 3)
        test_board = Board(row, col, 1.0)
        test_board.create_tiles()
        test_board.create_neigbors()

        top_left, top_mid, top_right = (test_board.tiles[0][0], test_board.tiles[0][1], test_board.tiles[0][2])
        mid_left, mid_mid, mid_right = (test_board.tiles[1][0], test_board.tiles[1][1], test_board.tiles[1][2])
        bottom_left, bottom_mid, bottom_right = (test_board.tiles[2][0], test_board.tiles[2][1], test_board.tiles[2][2])

        print(top_left.neighbors)
        self.assertCountEqual(top_left.neighbors, [top_mid, mid_left])
        self.assertCountEqual(top_mid.neighbors, [top_left, top_right, mid_mid])
        self.assertCountEqual(top_right.neighbors, [top_mid, mid_right])

        self.assertCountEqual(mid_left.neighbors, [top_left, mid_mid, bottom_left])
        self.assertCountEqual(mid_mid.neighbors, [top_mid, mid_left, mid_right, bottom_mid])
        self.assertCountEqual(mid_right.neighbors, [top_right, mid_mid, bottom_right])

        self.assertCountEqual(bottom_left.neighbors, [mid_left, bottom_mid])
        self.assertCountEqual(bottom_mid.neighbors, [mid_mid, bottom_left, bottom_right])
        self.assertCountEqual(bottom_right.neighbors, [mid_right, bottom_mid])





        