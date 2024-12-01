from chess.utils.piece_type import PieceType


class PieceTypeValidator:
    @staticmethod
    def validate(piece_type: str) -> bool:
        return any(piece_type == piece.value for piece in PieceType)
