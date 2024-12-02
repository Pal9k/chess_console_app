import unittest

from chess.input.input_parser import InputParser


class TestInputParser(unittest.TestCase):

    def test_parse_should_return_piece_type(self):
        expected_piece_type = "King"

        actual_piece_type, actual_position = InputParser.parse("   King,   D5")

        self.assertEqual(expected_piece_type, actual_piece_type)

    def test_parse_should_return_position(self):
        expected_position = "D5"

        actual_piece_type, actual_position = InputParser.parse("King, D5")

        self.assertEqual(expected_position, actual_position)

    def test_parse_should_raise_exception_when_given_invalid_input(self):
        expected_error_message = "Invalid input format. Expected 'piece_type, position' (e.g., 'King, D5')."

        with self.assertRaises(ValueError) as context:
            InputParser.parse("Abc")

        self.assertEqual(expected_error_message, str(context.exception))
