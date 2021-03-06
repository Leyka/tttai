from unittest import TestCase
from board import Board
from config import HUMAN, BOT 

class BoardTest(TestCase):
    def setUp(self):
        self.board = Board()

    def test_game_tie(self):
        board = self.board
        # Complete 8/9 squares
        for i in range(8):
            board.update_square(i)
        self.assertFalse(board.check_game_tied())
        # Complete the last square
        board.update_square(8)
        self.assertTrue(board.check_game_tied())
        self.assertTrue(board.game_over)

    def test_check_win(self):
        board = self.board
        board.update_square(0)
        board.update_square(1)
        board.update_square(3)
        # Should not win
        self.assertFalse(board.check_game_won())
        # Should win
        board.update_square(2)
        self.assertTrue(board.check_game_won())
        self.assertTrue(board.game_over)

    def test_next_player(self):
        board = self.board
        first_player = board.current_player
        second_player = BOT if first_player == HUMAN else HUMAN
        board.play(0)
        # Check if player has changed
        self.assertEqual(board.current_player, second_player)