from config import CROSS, CIRCLE
from board import Board

def play():
    board = Board()
    human = CROSS
    ai = CIRCLE

    while not board.game_over: 
        board.draw()
        if board.current_player == human: 
            answer = input('Choose a square between 0 and 8 : ')
            move = None
            try: 
                move = board.validates_move(answer)
            except Exception as e:
                print(str(e)) 
                continue
        else:  # AI
            board.current_player = human # For now, just play human
            continue

    # Game over

if __name__ == '__main__':
    play()
