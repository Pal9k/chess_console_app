import unittest

from chess.board.chess_board import ChessBoard
from chess.moves.moves_calculator import MoveCalculator


class TestMovesCalculator(unittest.TestCase):
    def test_get_possible_moves_should_return_moves_for_king_piece_type(self):
        expected_moves = ["C4", "C5", "C6", "D4", "D6", "E4", "E5", "E6"]

        actual_moves = MoveCalculator.get_possible_moves("King", "D5", ChessBoard(8, 8))

        self.assertEqual(sorted(expected_moves), sorted(actual_moves))

    def test_get_possible_moves_should_return_moves_for_queen_piece_type(self):
        expected_moves = ["A4", "B4", "C4", "D4", "F4", "G4", "H4", "E1", "E2", "E3", "E5", "E6", "E7", "E8", "A8",
                          "B7", "C6", "D5", "F3", "G2", "H1", "B1", "C2", "D3", "F5", "G6", "H7"]

        actual_moves = MoveCalculator.get_possible_moves("Queen", "E4", ChessBoard(8, 8))

        self.assertEqual(sorted(expected_moves), sorted(actual_moves))

    def test_get_possible_moves_should_return_moves_for_pawn_piece_type(self):
        expected_moves = ["G2"]

        actual_moves = MoveCalculator.get_possible_moves("Pawn", "G1", ChessBoard(8, 8))

        self.assertEqual(sorted(expected_moves), sorted(actual_moves))

    def test_get_possible_moves_should_return_empty_moves_for_pawn_piece_type(self):
        expected_moves = []

        actual_moves = MoveCalculator.get_possible_moves("Pawn", "H8", ChessBoard(8, 8))

        self.assertEqual(sorted(expected_moves), sorted(actual_moves))
