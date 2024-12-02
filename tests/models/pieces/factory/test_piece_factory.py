import unittest

from chess.models.pieces.factory.piece_factory import PieceFactory
from chess.models.pieces.king import King
from chess.models.pieces.pawn import Pawn
from chess.models.pieces.queen import Queen
from chess.utils.piece_type import PieceType


class TestPieceFactory(unittest.TestCase):
    def test_create_piece_should_return_king_chess_piece_when_given_king_type(self):
        chess_piece = PieceFactory().create_piece(PieceType.KING.value, 1, 2)

        self.assertIsInstance(chess_piece, King)

    def test_create_piece_should_return_queen_chess_piece_when_given_queen_type(self):
        chess_piece = PieceFactory().create_piece(PieceType.QUEEN.value, 1, 2)

        self.assertIsInstance(chess_piece, Queen)

    def test_create_piece_should_return_pawn_chess_piece_when_given_pawn_type(self):
        chess_piece = PieceFactory().create_piece(PieceType.PAWN.value, 1, 2)

        self.assertIsInstance(chess_piece, Pawn)

    def test_create_piece_should_raise_exception_when_give_invalid_type(self):
        expected_error_message = "Unknown piece type: Test"

        with self.assertRaises(ValueError) as context:
            PieceFactory().create_piece("Test", 1, 2)

        self.assertEqual(expected_error_message, str(context.exception))
