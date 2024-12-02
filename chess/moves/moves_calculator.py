from chess.models.board.chess_board import ChessBoard
from chess.models.pieces.factory.piece_factory import PieceFactory


class MoveCalculator:
    @staticmethod
    def get_possible_moves(piece_type: str, position: str, board: ChessBoard) -> list[str]:
        x, y = board.get_position_coordinates(position)
        chess_piece = PieceFactory.create_piece(piece_type, x, y)
        return chess_piece.get_possible_moves(board)
