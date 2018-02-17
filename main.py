from config import HUMAN, BOT
from board import Board
from random import randint # Temp

def play():
    board = Board()

    while not board.game_over: 
        answer = None
        
        if board.current_player == HUMAN:
            answer = input('Choose a square between 0 and 8 : ')
        else: # AI
            answer = randint(0, 8) # Dumb random answer

        # Play the turn
        try:
            print(board.play(answer))
        except Exception as e:
            print(str(e))
            continue

        board.draw()
        # TODO : Game won & Game over

if __name__ == '__main__':
    play()
