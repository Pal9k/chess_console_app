import unittest

from chess.board.chess_board import ChessBoard


class TestChessBoard(unittest.TestCase):
    def test_chess_board_should_return_correct_height(self):
        expected_height = 8
        chess_board8x8 = ChessBoard(expected_height, 8)

        actual_height = chess_board8x8.get_height()

        self.assertEqual(expected_height, actual_height)

    def test_chess_board_should_return_correct_width(self):
        expected_width = 8
        chess_board8x8 = ChessBoard(8, expected_width)

        actual_width = chess_board8x8.get_width()

        self.assertEqual(expected_width, actual_width)

    def test_chess_board_should_return_correct_positions(self):
        expected_positions = [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
                              ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
                              ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
                              ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
                              ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
                              ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
                              ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
                              ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']]
        chess_board8x8 = ChessBoard(8, 8)

        actual_positions = chess_board8x8.get_chess_board()

        self.assertEqual(expected_positions, actual_positions)

    def test_chess_board_should_return_false_when_given_negative_values(self):
        chess_board8x8 = ChessBoard(8, 8)

        actual = chess_board8x8.is_valid_position(-1, -1)

        self.assertFalse(actual)

    def test_chess_board_should_return_true_when_given_valid_values(self):
        chess_board8x8 = ChessBoard(8, 8)

        actual = chess_board8x8.is_valid_position(7, 3)

        self.assertTrue(actual)

    def test_chess_board_should_return_false_when_given_invalid_values(self):
        chess_board8x8 = ChessBoard(8, 8)

        actual = chess_board8x8.is_valid_position(17, 3)

        self.assertFalse(actual)

    def test_get_item_should_return_row_when_given_row_index(self):
        expected_row = ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8']
        chess_board8x8 = ChessBoard(8, 8)

        actual_row = chess_board8x8[0]

        self.assertEqual(expected_row, actual_row)

    def test_get_item_should_return_cell_value_when_given_cell_indexes(self):
        expected_row = 'A8'
        chess_board8x8 = ChessBoard(8, 8)

        actual_row = chess_board8x8[0][0]

        self.assertEqual(expected_row, actual_row)

    def test_get_position_coordinates_should_return_correct_x_position(self):
        expected = 3
        chess_board = ChessBoard(8, 8)

        x, y = chess_board.get_position_coordinates('D5')

        self.assertEqual(expected, x)

    def test_get_position_coordinates_should_return_correct_y_position(self):
        expected = 3
        chess_board = ChessBoard(8, 8)

        x, y = chess_board.get_position_coordinates('D5')

        self.assertEqual(expected, y)

    def test_get_position_coordinates_should_raise_exception_when_given_invalid_position(self):
        expected_error_message = "Unknown position: Z9"
        chess_board = ChessBoard(8, 8)

        with self.assertRaises(ValueError) as context:
            chess_board.get_position_coordinates("Z9")

        self.assertEqual(expected_error_message, str(context.exception))
