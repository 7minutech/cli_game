import unittest
from static.board import Board
from helpers.helpers import shortest_path_start, find_parent

class TestHelper(unittest.TestCase):

    # def test_shortest_path_line(self):
    #     my_board = Board(1, 3)
    #     start = my_board.positions[0][0]
    #     target = my_board.positions[0][2]
    #     shortest_path_tile = my_board.positions[0][1]
    #     self.assertEqual(shortest_path_start(start, target), shortest_path_tile)

    def test_shortest_path_line(self):
        parent_map = {
            "B": "A",
            "C": "A",
            "D": "B",
            "E": "D"
        }
        self.assertListEqual(find_parent("A", "E", parent_map), ["A", "B", "D", "E"])



