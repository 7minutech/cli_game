from static.board import Board
from active.player import Player
from pynput.keyboard import Key, Listener
from constants.direction import *

class Game:

    def __init__(self, board=Board(5, 5, 1.0), player=Player()):
        self.board = board
        self.player = player
        self.game_over = False
        self.place_player(self.board.start)
    
    def place_player(self, position):
        if self.player.position != None:
            self.board.positions[self.player.position[0]][self.player.position[1]].owner = None
        self.board.positions[position[0]][position[1]].owner = self.player
        self.player.position = position
        self.board.display()
    
    def move(self, key):

        if key == Key.right:
            new_position = (self.player.position[0] + RIGHT[0], self.player.position[1] + RIGHT[1])
            self.place_player(new_position)
        
        if key == Key.left:
            new_position = (self.player.position[0] + LEFT[0], self.player.position[1] + LEFT[1])
            self.place_player(new_position)
        
        if key == Key.up:
            new_position = (self.player.position[0] + UP[0], self.player.position[1] + UP[1])
            self.place_player(new_position)
        
        if key == Key.down:
            new_position = (self.player.position[0] + DOWN[0], self.player.position[1] + DOWN[1])
            self.place_player(new_position)
        
        if key == Key.esc:
            quit()


    def play_game(self):
        with Listener(on_press = self.move) as listener:
            listener.join()

    
