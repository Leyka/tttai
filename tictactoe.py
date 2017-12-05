import random

# Tic Tac Toe squares indexes
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8

# Configuration
DEFAULT = '_'
CROSS = 'x'
CIRCLE = 'o'

class Square:
    def __init__(self, index):
        self.index = index
        self.value = DEFAULT

    def empty(self):
        return self.value == DEFAULT

class Board:
    SIZE = 9
    WIN_COMBOS = [
        [0,1,2], [3,4,5], [6,7,8], # columns
        [0,3,6], [1,4,7], [2,5,8], # rows
        [0,4,8], [2,4,6] # diagionals
    ]

    def __init__(self):
        self.setup()

    def setup(self):
        self.squares = []
        self.current_player = self.who_starts()
        for i in range(self.SIZE):
            self.squares.append(Square(i))

    # Returns Cross (human) or Circle (ai)
    def who_starts(self):
        if random.getrandbits(1)  == 0:
            return CROSS
        else:
            return CIRCLE

    def draw(self):
        i = 0
        while i < self.SIZE:
            print(self.squares[i].value + ' ' + self.squares[i+1].value + ' ' + self.squares[i+2].value)
            i += 3

    def update(self, square_id, player):
        self.squares[square_id].value = player

    def check_win(self, player):
        squares = self.squares
        for win in self.WIN_COMBOS:
            return squares[win[0]].value == player and squares[win[1]].value == player and squares[win[2]].value == player

    def empty_squares(self):
        return [s for s in self.squares if s.empty()]

    def is_tied(self):
        return len(self.empty_squares()) == 0:

def main():
    board = Board()
    human = CROSS
    ai = CIRCLE
    player = board.current_player

    print(len(board.empty_squares()))

if __name__ == '__main__':
    main()
