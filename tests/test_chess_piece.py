import unittest

from chess.chess_board import ChessBoard
from chess.chess_piece import ChessPiece
from chess.king_move_strategy import KingMoveStrategy


class TestChessPiece(unittest.TestCase):
    def test_get_possible_moves_should_return_moves_when_given_king_move_strategy(self):
        expected_moves = ['C6', 'D6', 'E6', 'C5', 'E5', 'C4', 'D4', 'E4']
        king = ChessPiece(3, 3, KingMoveStrategy())

        actual_moves = king.get_possible_moves(ChessBoard(8, 8))

        self.assertEqual(expected_moves, actual_moves)
