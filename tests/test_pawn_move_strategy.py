import unittest

from chess.chess_board import ChessBoard
from chess.pawn_move_strategy import PawnMoveStrategy


class TestPawnMoveStrategy(unittest.TestCase):
    def test_pawn_move_strategy_should_return_all_possible_moves(self):
        expected_possible_moves = ["G2"]
        pawn = PawnMoveStrategy()

        actual_possible_moves = pawn.get_possible_moves(7, 6, ChessBoard(8, 8))

        self.assertEqual(sorted(expected_possible_moves), sorted(actual_possible_moves))