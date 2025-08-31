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
        if self.player.position != None:
            self.board.positions[self.player.position.row][self.player.position.col].owner = None
        self.board.positions[position.row][position.col].owner = self.player
        self.player.position = position
    
    def move(self, key):
        if key == Key.right:
            self.place_player(self.player.position + RIGHT)
        
        if key == Key.left:
            self.place_player(self.player.position + LEFT)
        
        if key == Key.up:
            self.place_player(self.player.position + UP)
        
        if key == Key.down:
            self.place_player(self.player.position + DOWN)
        
        if key == Key.esc:
            quit()


    def play_game(self):
        with Listener(on_press = self.move) as listener:
            listener.join()

    
