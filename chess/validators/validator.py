from chess.board.chess_board import ChessBoard
from chess.validators.piece_type_validator import PieceTypeValidator
from chess.validators.position_validator import PositionValidator


class Validator:
    @staticmethod
    def validate(piece_type: str, position: str, board: ChessBoard):
        if not PieceTypeValidator.validate(piece_type):
            return False, "Invalid Piece Type"

        if not PositionValidator.validate(position, board):
            return False, "Invalid Position"

        return True, "Success"
