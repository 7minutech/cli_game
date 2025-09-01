import unittest
from static.board import Board
from static.tile import Tile
from static.coordinate import Coordinate


class TestBoard(unittest.TestCase):

    def test_start_in_range(self):
        test_board = Board(5, 4, 1.0)
        self.assertTrue(test_board.start.row in range(test_board.rows) and test_board.start.col in range(test_board.cols))
    
    def test_end_in_range(self):
        test_board = Board(5, 4, 1.0)
        self.assertTrue(test_board.end.row in range(test_board.rows) and test_board.end.col in range(test_board.cols))
    
    def test_fill_positions(self):
        rows, cols = (5, 3)
        test_board = Board(rows, cols, 1.0)
        for i in range(rows):
            for j in range(cols):
                current_tile = test_board.positions[i][j]
                self.assertEqual(current_tile.coordinate, Coordinate((i,j)))
                self.assertIsInstance(current_tile, Tile)
    
    def test_create_neigbors_2x2(self):
        rows, cols = (2, 2)
        test_board = Board(rows, cols, 1.0)

        top_left = test_board.positions[0][0]
        bottom_left = test_board.positions[1][0]
        top_right = test_board.positions[0][1]
        bottom_right = test_board.positions[1][1]
        
        self.assertCountEqual(top_left.neighbors, [bottom_left, top_right])
        self.assertCountEqual(bottom_left.neighbors, [top_left, bottom_right])
        self.assertCountEqual(top_right.neighbors, [top_left, bottom_right])
        self.assertCountEqual(bottom_right.neighbors, [top_right, bottom_left])
    
    def test_create_neigbors_3x3(self):
        rows, cols = (3, 3)
        test_board = Board(rows, cols, 1.0)

        top_left, top_mid, top_right = (test_board.positions[0][0], test_board.positions[0][1], test_board.positions[0][2])
        mid_left, mid_mid, mid_right = (test_board.positions[1][0], test_board.positions[1][1], test_board.positions[1][2])
        bottom_left, bottom_mid, bottom_right = (test_board.positions[2][0], test_board.positions[2][1], test_board.positions[2][2])

        self.assertCountEqual(top_left.neighbors, [top_mid, mid_left])
        self.assertCountEqual(top_mid.neighbors, [top_left, top_right, mid_mid])
        self.assertCountEqual(top_right.neighbors, [top_mid, mid_right])

        self.assertCountEqual(mid_left.neighbors, [top_left, mid_mid, bottom_left])
        self.assertCountEqual(mid_mid.neighbors, [top_mid, mid_left, mid_right, bottom_mid])
        self.assertCountEqual(mid_right.neighbors, [top_right, mid_mid, bottom_right])

        self.assertCountEqual(bottom_left.neighbors, [mid_left, bottom_mid])
        self.assertCountEqual(bottom_mid.neighbors, [mid_mid, bottom_left, bottom_right])
        self.assertCountEqual(bottom_right.neighbors, [mid_right, bottom_mid])
    
    def test_display_5x5(self):
        board = Board(5,5, 1.0)
        expected = '\n⌌ ⎻ ⎻ ⎻ ⎻ ⎻ ⌍\n| ⎕ ⎕ ⎕ ⎕ ⎕ |\n| ⎕ ⎕ ⎕ ⎕ ⎕ |\n| ⎕ ⎕ ⎕ ⎕ ⎕ |\n| ⎕ ⎕ ⎕ ⎕ ⎕ |\n| ⎕ ⎕ ⎕ ⎕ ⎕ |\n⌎ ⎻ ⎻ ⎻ ⎻ ⎻ ⌏'
        self.assertEqual(board.format_board(), expected)
    
    def test_display_3x4(self):
        board = Board(3,4, 1.0)
        expected = '\n⌌ ⎻ ⎻ ⎻ ⎻ ⌍\n| ⎕ ⎕ ⎕ ⎕ |\n| ⎕ ⎕ ⎕ ⎕ |\n| ⎕ ⎕ ⎕ ⎕ |\n⌎ ⎻ ⎻ ⎻ ⎻ ⌏'
        self.assertEqual(board.format_board(), expected)

    def test_path_from_start_exists_false(self):
        board = Board(3,3, 1.0)
        board.start = Coordinate((2,2))
        target_tile = board.positions[0][0]
        target_tile.remove_neighbors()
        self.assertFalse(board.path_from_start_exists(target_tile))
        pass

    # def test_path_from_start_exists_true(self):
    #     board = Board(3,3, 1.0)
    #     board.start = Coordinate((2,2))
    #     target_tile = board.positions[0][0]
    #     self.assertTrue(board.path_from_start_exists(target_tile))    
    
    # def test_path_from_start_exists_true_complex(self):
    #     board = Board(3,3, 1.0)
    #     board.start = Coordinate((2,2))
    #     target_tile = board.positions[0][0]
    #     self.assertTrue(board.path_from_start_exists(target_tile))   