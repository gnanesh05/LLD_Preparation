from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [
            Player(input("enter player 1 name"), "X"),
            Player(input("enter player 2 name"), "O"),
        ]
        self.current = 0
    
    def play(self):
        while True:
            player = self.players[self.current]
            print(f"{player.name}'s turn - ({player.symbol})")
            self.board.display()
            row = int(input("enter row (0-2)"))
            col = int(input("enter col (0-2)"))

            if self.board.make_move(row, col, player.symbol):
                if self.board.check_winner(player.symbol):
                    self.board.display()
                    print(f"{player.name} - {player.symbol} wins!")
                    break
                elif self.board.is_draw():
                    self.board.display()
                    print("Draw game!")
                    break
                else:
                    self.current = 1 - self.current
            else:
                print("Invalid move!")



    