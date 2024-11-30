import unittest

from chess.board.chess_board import ChessBoard
from chess.pieces.strategies.king_move_strategy import KingMoveStrategy


class TestKingMoveStrategy(unittest.TestCase):
    def test_king_move_strategy_should_return_all_possible_moves(self):
        expected_possible_moves = ["C4", "C5", "C6", "D4", "D6", "E4", "E5", "E6"]
        king = KingMoveStrategy()

        actual_possible_moves = king.get_possible_moves(3, 3, ChessBoard(8,8))

        self.assertEqual(sorted(expected_possible_moves), sorted(actual_possible_moves))
