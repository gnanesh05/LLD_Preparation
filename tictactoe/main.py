'''
Basic features:
1️⃣ 2 players take turns placing X and O on a 3×3 board.
2️⃣ The board should display the current state.
3️⃣ Validate moves (cell must be empty).
4️⃣ Check for win/draw after every move.
5️⃣ Support replay/reset.

Entities
    Player (X,O)
    Board (manages grid, validates moves, wins)
    Game (manages turns, input)
'''
from game import Game

class Demo:
    @staticmethod
    def run():
        try:
            game = Game()
            game.play()
        except KeyboardInterrupt:
            print("Ending Game")
            return

if __name__ == '__main__':
    Demo.run()