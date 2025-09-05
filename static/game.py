from static.board import Board
from active.player import Player
from active.monster import *
from pynput.keyboard import Key, Listener
from pynput import keyboard
from constants.constants import RIGHT, LEFT, UP, DOWN
from helpers.helpers import furthest_coord
import pdb

class Game:

    def __init__(self, board=Board(5, 5, 1.0), player=Player(), monster=Monster(invisible=True)):
        self.board = board
        self.player = player
        self.game_active = False
        self.player_turn = True
        self.monster = monster
        self.playing = True
    
    def place(self, entity, position):
        if position is None:
            self.game_over()
        if self.contacted_monster(position):
            self.game_over()
        if type(entity) is Player and self.board.end.coord == position:
            self.game_active = False
            print("You escaped!")
        if self.game_active:
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
            self.place(self.player, self.player.coord + LEFT)
        
        if key == Key.up:
            self.place(self.player, self.player.coord + UP)
        
        if key == Key.down:
            self.place(self.player, self.player.coord + DOWN)
        
        if key == Key.esc:
            quit()

        last_monster_tile = self.monster.tile
        if self.monster.tile is not None:
            self.place_monster()
        self.board.display()
        self.remove_ping(last_monster_tile)

    def valid_move(self, key):
        new_coord = None
        match (key):
            case Key.right:
                new_coord = self.player.coord + RIGHT
            case Key.left:
                new_coord = self.player.coord + LEFT
            case Key.up:
                new_coord = self.player.coord + UP
            case Key.down:
                new_coord = self.player.coord + DOWN
            case Key.esc:
                return True
            case _:
                return False
    
        return (new_coord.row in range(self.board.rows) and new_coord.col in range(self.board.cols)) and self.board.positions[new_coord.row][new_coord.col] is not None

    def move_checked(self, key):
        if self.player_turn:
            if self.valid_move(key):
                self.move(key)
                if not self.game_active:
                    return False
            else:
                print("\nInvalid move")
    
    def place_entities_start(self):
        self.place(self.player, self.board.start.coord)
        self.place(self.monster, furthest_coord(self.board.start.coord, self.board.tiles))
    
    def contacted_monster(self, position):
        if position is None:
            return True
        tile = self.board.positions[position.row][position.col]
        if tile is None:
            return False
        return tile.owner is not None
    
    def remove_ping(self, last_monster_tile):
        if self.monster.tile is not None:
            last_monster_tile.pinged = False
    
    def place_monster(self):
        if self.monster.tile is not None:
            self.monster.tile.pinged = True
        self.place(self.monster, self.monster.move(self.player.tile))

    
    def game_over(self):
        self.game_active = False
        self.game_over_message()

    def play_once(self):
        self.playing = True
        self.game_active = True
        self.place_entities_start()
        self.board.display()

        def on_press(key):
            self.move_checked(key)
            if not self.game_active:
                listener.stop()

        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        listener.join()

    def game_over_message(self):
        print("\n\n\nThe monster caught you")
    
    def retry(self):
        response = (input("Play again? (y/n): ").lower())[-1]
        valid_responses = ["y", "n"]
        while response not in valid_responses:
            print("Invalid answer")
            response = input("Play again? (y/n): ")
        if response == "n":
            self.playing = False
        
    def change_board(self):
        new_board = Board(rows=(random.randint(3,6)),cols=(random.randint(3,6)))
        new_board.remove_random_tiles()
        self.board = new_board
    
    def play_game(self):
        self.play_once()
        self.retry()
        while self.playing:
            self.player.reset()
            self.monster.reset()
            self.change_board()
            self.play_once()
            self.game_over_message()
            self.retry()
        print("\n\n\nexiting...")
            
