import unittest

from chess.chess_board import ChessBoard
from chess.queen import Queen


class TestQueen(unittest.TestCase):
    def test_queen_should_return_all_possible_moves(self):
        expected_possible_moves = ["A4", "B4", "C4", "D4", "F4", "G4", "H4", "E1", "E2", "E3", "E5", "E6", "E7", "E8",
                                   "A8", "B7", "C6", "D5", "F3", "G2", "H1", "B1", "C2", "D3", "F5", "G6", "H7"]
        queen = Queen()

        actual_possible_moves = queen.get_possible_moves(4, 4, ChessBoard(8, 8))

        self.assertEqual(sorted(expected_possible_moves), sorted(actual_possible_moves))
