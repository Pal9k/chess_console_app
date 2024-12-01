import unittest

from chess.board.chess_board import ChessBoard
from chess.utils.piece_type import PieceType
from chess.validators.validator import Validator


class TestValidator(unittest.TestCase):
    def test_validate_should_return_true_when_given_valid_values(self):
        is_valid, message = Validator.validate(PieceType.QUEEN.value, "A1", ChessBoard(8, 8))

        self.assertTrue(is_valid)

    def test_validate_should_return_false_when_given_invalid_piece_type(self):
        is_valid, message = Validator.validate("Test", "A1", ChessBoard(8, 8))

        self.assertFalse(is_valid)

    def test_validate_should_return_error_message_when_given_invalid_piece_type(self):
        expected_error_message = "Invalid Piece Type"

        is_valid, actual_error_message = Validator.validate("Test", "A1", ChessBoard(8, 8))

        self.assertEqual(expected_error_message, actual_error_message)

    def test_validate_should_return_false_when_given_invalid_position(self):
        is_valid, message = Validator.validate(PieceType.KING.value, "Z1", ChessBoard(8, 8))

        self.assertFalse(is_valid)

    def test_validate_should_return_error_message_when_given_invalid_position(self):
        expected_error_message = "Invalid Position"

        is_valid, actual_error_message = Validator.validate(PieceType.KING.value, "A9", ChessBoard(8, 8))

        self.assertEqual(expected_error_message, actual_error_message)
