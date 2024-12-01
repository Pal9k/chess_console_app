import unittest

from chess.board.chess_board import ChessBoard
from chess.pieces.pawn import Pawn


class TestPawn(unittest.TestCase):
    def test_get_possible_moves_should_return_all_possible_moves_for_pawn(self):
        expected_possible_moves = ["G2"]
        pawn = Pawn(7, 6)

        actual_possible_moves = pawn.get_possible_moves(ChessBoard(8, 8))

        self.assertEqual(sorted(expected_possible_moves), sorted(actual_possible_moves))
