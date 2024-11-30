import unittest

from chess.chess_board import ChessBoard


class TestChessBoard(unittest.TestCase):
    def test_chess_board_should_have_correct_height(self):
        expected_height = 8
        chess_board8x8 = ChessBoard(expected_height, 8)

        actual_height = chess_board8x8.get_height()

        self.assertEqual(expected_height, actual_height)

    def test_chess_board_should_have_correct_width(self):
        expected_width = 8
        chess_board8x8 = ChessBoard(8, expected_width)

        actual_width = chess_board8x8.get_width()

        self.assertEqual(expected_width, actual_width)

    def test_chess_board_should_have_correct_position(self):
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
