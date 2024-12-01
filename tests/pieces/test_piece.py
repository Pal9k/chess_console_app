import unittest
from unittest.mock import MagicMock
from chess.board.chess_board import ChessBoard

from chess.pieces.piece import Piece


class MockPiece(Piece):
    def get_possible_moves(self, board: ChessBoard) -> list[str]:
        return ["A2", "A3", "A4"]


class TestPiece(unittest.TestCase):
    def setUp(self):
        self.mock_board = MagicMock(ChessBoard)
        self.piece = MockPiece(1, 1)  # Create an instance of MockPiece

    def test_initialization_coordinate_x(self):
        self.assertEqual(self.piece.x, 1)

    def test_initialization_coordinate_y(self):
        self.assertEqual(self.piece.y, 1)

    def test_get_possible_moves(self):
        possible_moves = self.piece.get_possible_moves(self.mock_board)
        self.assertEqual(possible_moves, ["A2", "A3", "A4"])
