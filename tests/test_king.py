import unittest

from chess.chess_board import ChessBoard
from chess.king_move_strategy import KingMoveStrategy


class TestKing(unittest.TestCase):
    def test_king_should_return_all_possible_moves(self):
        expected_possible_moves = ["C4", "C5", "C6", "D4", "D6", "E4", "E5", "E6"]
        king = KingMoveStrategy()

        actual_possible_moves = king.get_possible_moves(3, 3, ChessBoard(8,8))

        self.assertEqual(sorted(expected_possible_moves), sorted(actual_possible_moves))
