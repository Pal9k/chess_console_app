import unittest

from chess.chess_piece import ChessPiece
from chess.chess_piece_factory import ChessPieceFactory
from chess.king_move_strategy import KingMoveStrategy
from chess.pawn_move_strategy import PawnMoveStrategy
from chess.queen_move_strategy import QueenMoveStrategy
from chess.utils.piece_type import PieceType


class TestChessPieceFactory(unittest.TestCase):
    def test_create_piece_should_return_chess_piece_when_given_king_type(self):
        chess_piece = ChessPieceFactory().create_piece(PieceType.KING.value, 1, 2)

        self.assertIsInstance(chess_piece, ChessPiece)

    def test_create_piece_should_return_chess_piece_when_given_queen_type(self):
        chess_piece = ChessPieceFactory().create_piece(PieceType.QUEEN.value, 1, 2)

        self.assertIsInstance(chess_piece, ChessPiece)

    def test_create_piece_should_return_chess_piece_when_given_pawn_type(self):
        chess_piece = ChessPieceFactory().create_piece(PieceType.PAWN.value, 1, 2)

        self.assertIsInstance(chess_piece, ChessPiece)

    def test_create_piece_should_return_king_move_strategy_when_given_king_type(self):
        king_move_strategy = ChessPieceFactory().create_piece(PieceType.KING.value, 1, 2)

        self.assertIsInstance(king_move_strategy.move_strategy, KingMoveStrategy)

    def test_create_piece_should_return_queen_move_strategy_when_given_queen_type(self):
        queen_move_strategy = ChessPieceFactory().create_piece(PieceType.QUEEN.value, 1, 2)

        self.assertIsInstance(queen_move_strategy.move_strategy, QueenMoveStrategy)

    def test_create_piece_should_return_queen_move_strategy_when_given_pawn_type(self):
        pawn_move_strategy = ChessPieceFactory().create_piece(PieceType.PAWN.value, 1, 2)

        self.assertIsInstance(pawn_move_strategy.move_strategy, PawnMoveStrategy)
