
from unittest import TestCase
from tictactoe import Board

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
        for i in range(board.SIZE - 1):
            board.update(i, player)
        self.assertFalse(board.is_tied())
        # Complete the last square
        board.update(board.SIZE - 1, player)
        self.assertTrue(board.is_tied())
        self.assertTrue(board.game_over)

    def test_check_win(self):
        board = self.board
        player = board.current_player
        board.update(0, player)
        board.update(1, player)
        board.update(3, player)
        # Should not win
        self.assertFalse(board.check_win(player))
        # Should win
        board.update(2, player)
        self.assertTrue(board.check_win(player))
        self.assertTrue(board.game_over)
