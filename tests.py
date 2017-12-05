
from unittest import TestCase
from tictactoe import Board
from config import CROSS, CIRCLE

# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8

class BoardTest(TestCase):
    def setUp(self):
        self.board = Board()

    def test_game_tie(self):
        board = self.board
        player = board.current_player
        # Complete 8/9 squares
        for i in range(8):
            board.update_square(i, player)
        self.assertFalse(board.is_tied())
        # Complete the last square
        board.update_square(8, player)
        self.assertTrue(board.is_tied())
        self.assertTrue(board.game_over)

    def test_check_win(self):
        board = self.board
        player = board.current_player
        board.update_square(0, player)
        board.update_square(1, player)
        board.update_square(3, player)
        # Should not win
        self.assertFalse(board.check_win(player))
        # Should win
        board.update_square(2, player)
        self.assertTrue(board.check_win(player))
        self.assertTrue(board.game_over)

    def test_next_player(self):
        board = self.board
        first_player = board.current_player
        second_player = CROSS if first_player == CIRCLE else CIRCLE
        board.move(0)
        # Check if player has changed
        self.assertEqual(board.current_player, second_player)









