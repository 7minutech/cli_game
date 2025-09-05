from static.board import Board
from active.player import Player
from active.monster import Monster
from pynput.keyboard import Key, Listener
from constants.constants import RIGHT, LEFT, UP, DOWN
from helpers.helpers import shortest_path_start, furthest_coord
import pdb

class Game:

    def __init__(self, board=Board(5, 5, 1.0), player=Player(), monster=Monster()):
        self.board = board
        self.player = player
        self.game_over = False
        self.player_turn = True
        self.monster = monster
    
    def place(self, entity, position):
        if self.contacted_monster(position):
            print("game over")
        if entity.coord != None:
            self.board.positions[entity.coord.row][entity.coord.col].owner = None
        tile = self.board.positions[position.row][position.col]
        tile.owner = entity
        entity.coord = position
        entity.tile = tile
    
    def move(self, key):

        if key == Key.right:
            self.place(self.player, self.player.coord + RIGHT)
        
        if key == Key.left:
            self.place(self.player, self.player.coord + LEFT)q
        
        if key == Key.up:
            self.place(self.player, self.player.coord + UP)
        
        if key == Key.down:
            self.place(self.player, self.player.coord + DOWN)
        
        if key == Key.esc:
            quit()
        
        self.board.display()


    def valid_move(self, key):
        new_coord = None
        if key == Key.right:
            new_coord = self.player.coord + RIGHT
        
        if key == Key.left:
            new_coord = self.player.coord + LEFT

        if key == Key.up:
            new_coord = self.player.coord + UP

        if key == Key.down:
            new_coord = self.player.coord + DOWN

        if key == Key.esc:
            return True
        
        return (new_coord.row in range(self.board.rows) and new_coord.col in range(self.board.cols))

    def move_checked(self, key):
        if self.player_turn:
            if self.valid_move(key):
                self.move(key)   
            else:
                print("\nInvalid move")
    
    def place_entities_start(self):
        self.place(self.player, self.board.start.coord)
        self.place(self.monster, furthest_coord(self.board.start.coord, self.board.tiles))
    
    def contacted_monster(self, position):
        return self.board.positions[position.row][position.col].owner is not None
    
    def game_over(self):
        print("Game is over")


    def play_game(self):
        self.place_entities_start()
        self.board.display()
        with Listener(on_press = self.move_checked) as listener:
            listener.join()
            
