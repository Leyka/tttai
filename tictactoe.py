class Square:
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def set_cross(self):
        self.value = 'x'

    def set_circle(self):
        self.value = 'o'

    def is_empty(self):
        return self.value == '_'


class Board:
    SIZE = 9
    def __init__(self):
        self.squares = []
        self.build()

    def build(self):
        for i in range(self.SIZE):
            self.squares.append(Square(i, '_'))

    def draw(self):
        i = 0
        while i < self.SIZE:
            print(self.squares[i].value + ' ' + self.squares[i+1].value + ' ' + self.squares[i+2].value)
            i += 3

def main():

    board = Board()
    board.draw()
    print(board.squares[0].is_empty())
    print('new board')
    board.squares[0].set_cross()
    board.squares[1].set_circle()
    board.draw()
    print(board.squares[0].is_empty())


if __name__ == '__main__':
    main()
