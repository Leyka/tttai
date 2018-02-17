from config import CROSS, CIRCLE
from board import Board
from random import randint # Temp

def play():
    board = Board()
    human = CROSS
    ai = CIRCLE
    while not board.game_over: 
        answer = None
        
        if board.current_player == human:
            print('* Your turn *')
            answer = input('Choose a square between 0 and 8 : ')
        else: # AI
            print('* AI turn *')
            answer = randint(0, 8) # Dumb random answer

        # Play the turn
        try:
            board.play(answer)
        except Exception as e:
            print(str(e))
            continue
        # TODO : Game won & Game over
        board.draw()

if __name__ == '__main__':
    play()
