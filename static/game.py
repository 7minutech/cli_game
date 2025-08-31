from static.board import Board
from active.player import Player
from pynput.keyboard import Key, Listener
from constants.direction import *
import pdb

class Game:

    def __init__(self, board=Board(5, 5, 1.0), player=Player()):
        self.board = board
        self.player = player
        self.game_over = False
        self.place_player(self.board.start)
    
    def place_player(self, position):
        if self.player.coordinate != None:
            self.board.positions[self.player.coordinate.row][self.player.coordinate.col].owner = None
        self.board.positions[position.row][position.col].owner = self.player
        self.player.coordinate = position
    
    def move(self, key):

        if key == Key.right:
            self.place_player(self.player.coordinate + RIGHT)
        
        if key == Key.left:
            self.place_player(self.player.coordinate + LEFT)
        
        if key == Key.up:
            self.place_player(self.player.coordinate + UP)
        
        if key == Key.down:
            self.place_player(self.player.coordinate + DOWN)
        
        if key == Key.esc:
            quit()
        
        self.board.display()

    def play_game(self):
        self.board.display()
        with Listener(on_press = self.move) as listener:
            listener.join()
