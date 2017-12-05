import random
from config import DEFAULT, CROSS, CIRCLE
# Tic Tac Toe squares indexes
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8


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
        self.game_over = False
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

    def update_square(self, square_idx, player):
        self.squares[square_idx].value = player

    # TODO rework this method
    def move(self, square_idx):
        if self.game_over:
            raise Exception("All squares are filled")

        self.update_square(square_idx, self.current_player)
        self.check_win(self.current_player)

        # Determine next player
        self.current_player = CIRCLE if self.current_player == CROSS else CROSS


    def draw(self):
        i = 0
        while i < self.SIZE:
            print(self.squares[i].value + ' ' + self.squares[i+1].value + ' ' + self.squares[i+2].value)
            i += 3

    def check_win(self, player):
        squares = self.squares
        for win in self.WIN_COMBOS:
            if squares[win[0]].value == player and squares[win[1]].value == player and squares[win[2]].value == player:
                self.game_over = True
                return True
        return False

    def empty_squares(self):
        return [s for s in self.squares if s.empty()]

    def is_tied(self):
        if len(self.empty_squares()) == 0:
            self.game_over = True
        return self.game_over

def main():
    board = Board()
    human = CROSS
    ai = CIRCLE
    player = board.current_player

if __name__ == '__main__':
    main()
