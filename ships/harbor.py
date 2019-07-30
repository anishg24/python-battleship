import random
import string

letter_list = list(string.ascii_uppercase)

class Ship:
    def __init__(self, warship_type, size, vertical=True):
        self.type = warship_type
        self.length = size
        self.vertical = vertical

    def place(self, board, location):
        grid = board.board
        self.column, self.row = location
        self.row -= 1
        try:
            grid[self.column][self.row]
        except:
            return print("You can't place the ship out of bounds!")
        if self.vertical:
            for _ in range(self.length):
                grid[self.column][self.row] = "▣"
                self.row += 1
        else:
            for _ in range(self.length):
                grid[self.column][self.row] = "▣"
                self.column = letter_list[letter_list.index(self.column)+1]
        print(board)
        
