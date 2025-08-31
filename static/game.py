from static.board import Board
from active.player import Player
from pynput.keyboard import Key, Listener

class Game:

    def __init__(self, board=Board(5, 5, 1.0), player=Player()):
        self.board = board
        self.player = player
        self.game_over = False
        self.place_player(self.board.start)
    
    def place_player(self, position):
        self.board.positions[position[0]][position[1]].owner = self.player
        self.player.position = position
    
    def move(self, key):

        if key == Key.right:
            print("right")
        
        if key == Key.left:
            print("left")
        
        if key == Key.up:
            print("up")
        
        if key == Key.down:
            print("down")
        
        if key == Key.esc:
            quit()


    def play_game(self):
        self.board.display()
        with Listener(on_press = self.move) as listener:
            listener.join()

    
