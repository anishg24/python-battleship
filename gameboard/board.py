import prettytable
import string

letter_list = list(string.ascii_uppercase)

class Board:
    def __init__(self, size):
        if size > 26:
            return print("You can't have a board bigger than 26x26!")
        if size < 10:
            return print("You need a board smaller than 10x10!")
        self.size = (size,size)
        self.rows = size
        self.columns = size
        self.board = {}
        self.make_board()
    
    def make_board(self):
        for i in range(self.rows):
            self.board[letter_list[i]] = ["■"] * self.columns

    def __str__(self):
        pt = prettytable.PrettyTable()
        pt.add_column("", [i+1 for i in range(self.rows)])
        for i in range(self.rows):
            pt.add_column(list(self.board.keys())[i],self.board[letter_list[i]])
        return str(pt)
    
    def __repr__(self):
        return "A Battleship Gameboard"
