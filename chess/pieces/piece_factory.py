from chess.pieces.piece import Pieces
from chess.pieces.strategies.king_move_strategy import KingMoveStrategy
from chess.pieces.strategies.pawn_move_strategy import PawnMoveStrategy
from chess.pieces.strategies.queen_move_strategy import QueenMoveStrategy
from chess.utils.piece_type import PieceType


class PieceFactory:
    @staticmethod
    def create_piece(piece_type: str, x: int, y: int) -> Pieces:
        if piece_type == PieceType.KING.value:
            return Pieces(x, y, KingMoveStrategy())
        elif piece_type == PieceType.QUEEN.value:
            return Pieces(x, y, QueenMoveStrategy())
        elif piece_type == PieceType.PAWN.value:
            return Pieces(x, y, PawnMoveStrategy())
        else:
            raise ValueError(f"Unknown piece type: {piece_type}")
