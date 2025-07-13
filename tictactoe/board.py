class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [['' for _ in range(size)] for _ in range(size)]
    
    def display(self):
        for row in self.grid:
            print('|'.join(row))
            print('-' * (self.size*2-1))
            
    def make_move(self, row, col, symbol):
        if self.grid[row][col] == '':
            self.grid[row][col] = symbol
            return True
        return False
    
    def check_winner(self, symbol):
        #checks rows&columns
        for i in range(self.size):
            if all(self.grid[i][j] == symbol for j in range(self.size)) or all(self.grid[j][i] for j in range(self.size)):
                return True
        #checks diagonals
        if all(self.grid[i][i] == symbol for i in range(self.size)) or all(self.grid[i][self.size -1-i] for i in range(self.size)):
            return True
        return False
    
    def is_draw(self):
        return all(self.grid[i][j] !='' for i in range(self.size) for j in range(self.size))