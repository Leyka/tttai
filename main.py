from config import HUMAN, BOT
from board import Board
from random import randint # Temp

def play():
    board = Board()

    while not board.game_over: 
        answer = None
        
        if board.current_player == HUMAN:
            print('* Your Turn *')
            answer = input('Choose a square between 0 and 8 : ')
        else: # AI
            print('* AI Turn *')
            answer = randint(0, 8) # Dumb random answer

        # Play the turn
        try:
            message = board.play(answer)
            if message is not None:
                print(message)
        except Exception as e:
            print(str(e))
            continue

        board.draw()
        # TODO : Game won & Game over

if __name__ == '__main__':
    play()
