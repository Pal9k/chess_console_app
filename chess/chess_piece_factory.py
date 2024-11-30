from chess.chess_piece import ChessPiece
from chess.king_move_strategy import KingMoveStrategy
from chess.pawn_move_strategy import PawnMoveStrategy
from chess.queen_move_strategy import QueenMoveStrategy
from chess.utils.piece_type import PieceType


class ChessPieceFactory:
    @staticmethod
    def create_piece(piece_type: str, x: int, y: int) -> ChessPiece:
        if piece_type == PieceType.KING.value:
            return ChessPiece(x, y, KingMoveStrategy())
        elif piece_type == PieceType.QUEEN.value:
            return ChessPiece(x, y, QueenMoveStrategy())
        elif piece_type == PieceType.PAWN.value:
            return ChessPiece(x, y, PawnMoveStrategy())
        else:
            raise ValueError(f"Unknown piece type: {piece_type}")
