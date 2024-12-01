import unittest

from chess.utils.piece_type import PieceType
from chess.validators.piece_type_validator import PieceTypeValidator


class TestPieceTypeValidator(unittest.TestCase):
    def test_validate_should_return_true_when_given_king_type(self):
        is_valid = PieceTypeValidator.validate(PieceType.KING.value)

        self.assertTrue(is_valid)

    def test_validate_should_return_true_when_given_queen_type(self):
        is_valid = PieceTypeValidator.validate(PieceType.QUEEN.value)

        self.assertTrue(is_valid)

    def test_validate_should_return_true_when_given_pawn_type(self):
        is_valid = PieceTypeValidator.validate(PieceType.PAWN.value)

        self.assertTrue(is_valid)

    def test_validate_should_return_false_when_given_invalid_type(self):
        is_valid = PieceTypeValidator.validate("Test")

        self.assertFalse(is_valid)
