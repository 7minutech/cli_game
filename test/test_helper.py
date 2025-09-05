import unittest
from static.board import Board
from helpers.helpers import shortest_path, path, shortest_path_start, coord_distance
from static.coordinate import Coordinate

class TestHelper(unittest.TestCase):

    def shortest_path_start_3x3(self):
        my_board = Board(2, 3)
        start = my_board.positions[0][0]
        target = my_board.positions[0][2]
        middle = my_board.positions[0][1]
        self.assertEqual(shortest_path_start(start, target), middle)
    
    def shortest_path_start_3x3(self):
        my_board = Board(2, 3)
        start = my_board.positions[0][0]
        target = my_board.positions[0][2]
        middle = my_board.positions[0][1]
        self.assertEqual(shortest_path_start(start, target), middle)

    def test_shortest_path_3x3(self):
        my_board = Board(2, 3)
        start = my_board.positions[0][0]
        target = my_board.positions[0][2]
        middle = my_board.positions[0][1]
        expected = [start, middle, target]
        self.assertListEqual(shortest_path(start, target), expected)

    def test_shortest_path_2_lines(self):
        my_board = Board(2, 3)
        start = my_board.positions[0][0]
        target = my_board.positions[0][2]
        middle = my_board.positions[0][1]
        expected = [start, middle, target]
        self.assertListEqual(shortest_path(start, target), expected)

    def test_shortest_path_line(self):
        my_board = Board(1, 3)
        start = my_board.positions[0][0]
        target = my_board.positions[0][2]
        middle = my_board.positions[0][1]
        expected = [start, middle, target]
        self.assertListEqual(shortest_path(start, target), expected)
    
    def test_shortest_path_start_is_end(self):
        my_board = Board(1, 3)
        start = my_board.positions[0][0]
        target = my_board.positions[0][0]
        self.assertIsNone(shortest_path(start, target))

    def test_path(self):
        parent_map = {
            "B": "A",
            "C": "A",
            "D": "B",
            "E": "D"
        }
        self.assertListEqual(path("A", "E", parent_map), ["A", "B", "D", "E"])
    
    def test_coord_distance_3x3(self):
        coord_1 = Coordinate((0,0))
        coord_2 = Coordinate((3,3))
        self.assertEqual(coord_distance(coord_1, coord_2), 18)
    
    def test_coord_distance_2x3(self):
        coord_1 = Coordinate((1,1))
        coord_2 = Coordinate((2,2))
        self.assertEqual(coord_distance(coord_1, coord_2), 2)



