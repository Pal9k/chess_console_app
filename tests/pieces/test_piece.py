import unittest

from chess.board.chess_board import ChessBoard
from chess.pieces.piece import Pieces
from chess.pieces.strategies.king_move_strategy import KingMoveStrategy


class TestPiece(unittest.TestCase):
    def test_get_possible_moves_should_return_moves_when_given_king_move_strategy(self):
        expected_moves = ['C6', 'D6', 'E6', 'C5', 'E5', 'C4', 'D4', 'E4']
        king = Pieces(3, 3, KingMoveStrategy())

        actual_moves = king.get_possible_moves(ChessBoard(8, 8))

        self.assertEqual(expected_moves, actual_moves)
