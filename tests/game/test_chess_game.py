import unittest
from unittest.mock import patch

from chess.game.chess_game import ChessGame
from chess.utils.piece_type import PieceType


class TestChessGame(unittest.TestCase):
    def test_parse_input(self):
        game = ChessGame()
        piece_type, x, y = game.parse_input('Pawn, G1')

        self.assertEqual(piece_type, 'Pawn')
        self.assertEqual(x, 7)
        self.assertEqual(y, 6)

    def test_get_all_possible_moves(self):
        expected_moves = ['F2', 'G2', 'H2', 'F1', 'H1']
        game = ChessGame()

        actual_moves = game.get_possible_moves(PieceType.KING.value, 7, 6)

        self.assertEqual(expected_moves, actual_moves)

    @patch('builtins.input', return_value='Pawn, G1')
    @patch('builtins.print')
    def test_play(self, mock_print, mock_input):
        expected_output = 'Output - G2'
        game = ChessGame()

        game.play()

        mock_input.assert_called_once()
        mock_print.assert_called_once_with(expected_output)


