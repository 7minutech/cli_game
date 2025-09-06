from static.board import Board, ChaosLevel
from active.player import Player
from active.monster import *
from pynput.keyboard import Key, Listener
from pynput import keyboard
from constants.constants import RIGHT, LEFT, UP, DOWN
from helpers.helpers import furthest_coord
import questionary
import pdb

class Game:

    def __init__(self, board=Board(5, 5, 1.0), player=Player(), monster=Monster()):
        self.board = board
        self.player = player
        self.game_active = False
        self.player_turn = True
        self.monster = monster
        self.playing = True
        self.escapes = 0
        self.player_escaped = False
    
    def place(self, entity, position):
        if type(entity) is Player and self.board.end.coord == position:
            self.game_active = False
            self.escapes += 1
            self.player_escaped = True
            print("You escaped!")
        elif type(entity) is Monster and self.player.coord == position:
            self.game_over()
        elif type(entity) is Player and self.monster.coord == position:
            self.game_over()
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
        print(f"Escapes in a row: {self.escapes}")
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
        if self.game_active:
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
        print(f"Escapes in a row: {self.escapes}")
        self.board.display()

        def on_press(key):
            self.move_checked(key)
            if not self.game_active:
                listener.stop()

        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        listener.join()

    def game_over_message(self):
        self.escapes = 0
        print("\n\n\nThe monster caught you")
    
    def retry(self):
        self.player_escaped = False
        choice = questionary.select(
            "\nPlay again?",
            choices=["Yes", "No"],
        ).ask()
        if choice == "No":
            self.playing = False
        
    def change_board(self):
        new_board = Board(rows=(random.randint(5,8)),cols=(random.randint(5,8)))
        new_board.remove_random_tiles()
        self.board = new_board

    def board_chaos_selector(self):
        choice = questionary.select(
            "Play again?",
            choices=["Yes", "No"],
        ).ask()

    def show_config(self):
        choice = questionary.select(
            "Want to change setttings (difficulty, map randomness)",
            choices=["Yes", "No"],
        ).ask()
        if choice == "Yes":
            return True
        return False
    
    def configure_game(self):
        aggro = questionary.select(
            "Select Monster Chase Level",
            choices=["Mild", "Moderate", "Strong", "Extreme"]
        ).ask()
        self.configure_monster_aggro(aggro)

        board_randomness = questionary.select(
            "Select Map Randomness",
            choices=["Subtle", "Noticeable", "Intense", "Extreme"]
        ).ask()
        self.configure_board_randomness(board_randomness)


    def configure_monster_aggro(self, aggro):
        match aggro:
            case "Mild":
                self.monster.aggro = AggroLevel.MILD
            case "Moderate":
                self.monster.aggro = AggroLevel.MODERATE
            case "Strong":
                self.monster.aggro = AggroLevel.STRONG
            case "Extreme":
                self.monster.aggro = AggroLevel.EXTREME


    def configure_board_randomness(self, board_randomness):
        match board_randomness:
            case "Subtle":
                self.board.chaos = ChaosLevel.SUBTLE
            case "Noticeable":
                self.board.chaos = ChaosLevel.NOTICEABLE
            case "Intense":
                self.board.chaos = ChaosLevel.INTENSE
            case "Extreme":
                self.board.chaos = ChaosLevel.EXTREME


    def intro_message(self):
        print("This is a game where you reach the exit in green\nTry not to get caught by the monster " \
        "whose last move is highlighted in red\nYou and the monster can only move up, down, left, right use the arrow keys to move" \
        "\nPress esc to exit game at anytime")
    
    def play_game(self):
        self.intro_message()
        if self.show_config():
            self.configure_game()
        self.play_once()
        if not self.player_escaped:
            self.retry()
        while self.playing:
            self.player_escaped = False
            self.player.reset()
            self.monster.reset()
            self.change_board()
            self.play_once()
            if not self.player_escaped:
                self.retry()
        print("\n\n\nexiting...")
            
