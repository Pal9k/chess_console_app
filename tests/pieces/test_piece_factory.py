import unittest

from chess.pieces.piece import Pieces
from chess.pieces.piece_factory import PieceFactory
from chess.pieces.strategies.king_move_strategy import KingMoveStrategy
from chess.pieces.strategies.pawn_move_strategy import PawnMoveStrategy
from chess.pieces.strategies.queen_move_strategy import QueenMoveStrategy
from chess.utils.piece_type import PieceType


class TestPieceFactory(unittest.TestCase):
    def test_create_piece_should_return_chess_piece_when_given_king_type(self):
        chess_piece = PieceFactory().create_piece(PieceType.KING.value, 1, 2)

        self.assertIsInstance(chess_piece, Pieces)

    def test_create_piece_should_return_chess_piece_when_given_queen_type(self):
        chess_piece = PieceFactory().create_piece(PieceType.QUEEN.value, 1, 2)

        self.assertIsInstance(chess_piece, Pieces)

    def test_create_piece_should_return_chess_piece_when_given_pawn_type(self):
        chess_piece = PieceFactory().create_piece(PieceType.PAWN.value, 1, 2)

        self.assertIsInstance(chess_piece, Pieces)

    def test_create_piece_should_return_king_move_strategy_when_given_king_type(self):
        king_move_strategy = PieceFactory().create_piece(PieceType.KING.value, 1, 2)

        self.assertIsInstance(king_move_strategy.move_strategy, KingMoveStrategy)

    def test_create_piece_should_return_queen_move_strategy_when_given_queen_type(self):
        queen_move_strategy = PieceFactory().create_piece(PieceType.QUEEN.value, 1, 2)

        self.assertIsInstance(queen_move_strategy.move_strategy, QueenMoveStrategy)

    def test_create_piece_should_return_queen_move_strategy_when_given_pawn_type(self):
        pawn_move_strategy = PieceFactory().create_piece(PieceType.PAWN.value, 1, 2)

        self.assertIsInstance(pawn_move_strategy.move_strategy, PawnMoveStrategy)
