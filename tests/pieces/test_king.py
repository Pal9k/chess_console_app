import unittest

from chess.board.chess_board import ChessBoard
from chess.pieces.king import King


class TestKing(unittest.TestCase):
    def test_get_possible_moves_should_return_all_possible_moves_for_king(self):
        expected_possible_moves = ["C4", "C5", "C6", "D4", "D6", "E4", "E5", "E6"]
        king = King(3, 3)

        actual_possible_moves = king.get_possible_moves(ChessBoard(8, 8))

        self.assertEqual(sorted(expected_possible_moves), sorted(actual_possible_moves))
