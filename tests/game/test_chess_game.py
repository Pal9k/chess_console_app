import unittest
from unittest.mock import patch

from chess.game.chess_game import ChessGame


class TestChessGame(unittest.TestCase):

    @patch('builtins.input', return_value='Pawn, G1')
    @patch('builtins.print')
    def test_play(self, mock_print, mock_input):
        expected_output = 'Output - G2'
        game = ChessGame()

        game.play()

        mock_input.assert_called_once()
        mock_print.assert_called_once_with(expected_output)
