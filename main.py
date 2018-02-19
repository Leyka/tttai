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
            answer = randint(0, 8) # Temporary a dumb random answer

        # Play the turn
        try:
            message = board.play(answer)
            # Game over or Game won
            if message is not None:
                print(message)
        except Exception as e:
            print(str(e))
            continue

        board.draw()

        # Play again?
        if board.game_over:
            play_again = input('Play again? (y/n) : ')
            if play_again == 'y':
                board.setup()
                print('\n', '========= NEW GAME =========')

if __name__ == '__main__':
    play()
