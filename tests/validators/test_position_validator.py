import unittest

from chess.board.chess_board import ChessBoard
from chess.validators.position_validator import PositionValidator


class TestPositionValidator(unittest.TestCase):
    def test_validate_should_return_true_when_given_A1_position(self):
        is_valid = PositionValidator.validate("A1", ChessBoard(8, 8))

        self.assertTrue(is_valid)

    def test_validate_should_return_true_when_given_H8_position(self):
        is_valid = PositionValidator.validate("H8", ChessBoard(8, 8))

        self.assertTrue(is_valid)

    def test_validate_should_return_false_when_given_H9_position(self):
        is_valid = PositionValidator.validate("H9", ChessBoard(8, 8))

        self.assertFalse(is_valid)

    def test_validate_should_return_false_when_given_Z9_position(self):
        is_valid = PositionValidator.validate("Z9", ChessBoard(8, 8))

        self.assertFalse(is_valid)
