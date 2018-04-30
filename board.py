from config import HUMAN, BOT, DEFAULT
import random

class Board:
    """
    Typical 3x3 tic tac toe board. Each square has an index like this:

    [0] | [1] | [2]
    ---------------
    [3] | [4] | [5]
    ---------------
    [6] | [7] | [8]
    ---------------

    """

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

    def who_starts(self):
        if random.getrandbits(1)  == 0:
            return HUMAN
        else:
            return BOT

    def draw(self):
        i = 0
        while i < self.SIZE:
            print(self.squares[i].value + ' ' + self.squares[i+1].value + ' ' + self.squares[i+2].value)
            i += 3

    def update_square(self, square_index):
        self.squares[square_index].value = self.current_player

    def empty_squares(self):
        return [s for s in self.squares if s.empty()]

    def change_player(self):
        self.current_player = HUMAN if self.current_player == BOT else BOT

    def check_game_won(self):
        squares = self.squares
        player = self.current_player
        for win in self.WIN_COMBOS:
            if squares[win[0]].value == player and squares[win[1]].value == player and squares[win[2]].value == player:
                self.game_over = True
                return True
        return False

    def check_game_tied(self):
        if len(self.empty_squares()) == 0:
            self.game_over = True
        return self.game_over

    def validates_move(self, answer):
        # Cast answer from string -> int if it's not already an int
        move = int(answer) if isinstance(answer, str) else answer
        if move <0 or move >8:
            raise Exception('Your answer must be between 0 and 8')
        # Check if move is in empty square
        if not self.squares[move].empty():
            raise Exception('The square #' + str(move) + ' is already taken')

        return move

    def play(self, answer):
        move = self.validates_move(answer)
        self.update_square(move)

        message = None
        if self.check_game_won():
            message = '~~ YOU WON !! w0000t w0000t ~~' if self.current_player == HUMAN else '~~ Aw! man you lost :( ~~'
        elif self.check_game_tied():
            message = '~ GAME OVER ~'
        else:
            # Keep playing
            self.change_player()
        return message

class Square:
    def __init__(self, index):
        self.index = index
        self.value = DEFAULT

    def empty(self):
        return self.value == DEFAULT
