import unittest
from static.tile import Tile
from static.board import Board

class TestTile(unittest.TestCase):

    def test_remove_neigbor_3x3(self):
        board = Board(3,3, 1.0)
        target_tile = board.positions[0][0]
        target_neighbor = board.positions[1][0]
        target_tile.remove_neighbor(target_neighbor)
        self.assertNotIn(target_neighbor, target_tile.neighbors)
        self.assertNotIn(target_tile, target_neighbor.neighbors)
    
    def test_remove_neigbor_4x4(self):
        board = Board(4,4, 1.0)
        target_tile = board.positions[1][1]
        target_neighbor = board.positions[1][2]
        target_tile.remove_neighbor(target_neighbor)
        self.assertNotIn(target_neighbor, target_tile.neighbors)
        self.assertNotIn(target_tile, target_neighbor.neighbors)

    def test_remove_neigbors3x3(self):
        board = Board(3,3, 1.0)
        target_tile = board.positions[0][0]
        target_tile_neighbors= target_tile.neighbors.copy()
        target_tile.remove_neighbors()
        self.assertListEqual(target_tile.neighbors, [])
        for neigbor in target_tile_neighbors:
            self.assertNotIn(target_tile, neigbor.neighbors)
    
    def test_remove_neigbors4x4(self):
        board = Board(4,4, 1.0)
        target_tile = board.positions[1][1] 
        target_tile_neighbors= target_tile.neighbors.copy()
        target_tile.remove_neighbors()
        self.assertListEqual(target_tile.neighbors, [])
        for neigbor in target_tile_neighbors:
            self.assertNotIn(target_tile, neigbor.neighbors)
