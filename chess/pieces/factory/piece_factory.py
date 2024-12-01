from chess.pieces.piece import Piece
from chess.pieces.king import King
from chess.pieces.pawn import Pawn
from chess.pieces.queen import Queen
from chess.utils.piece_type import PieceType


class PieceFactory:
    @staticmethod
    def create_piece(piece_type: str, x: int, y: int) -> Piece:
        piece_classes_dic = {
            PieceType.KING.value: King,
            PieceType.QUEEN.value: Queen,
            PieceType.PAWN.value: Pawn,
        }

        if piece_type in piece_classes_dic:
            return piece_classes_dic[piece_type](x, y)
        else:
            raise ValueError("Unknown piece type: " + piece_type)
