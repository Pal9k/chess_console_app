from chess.board.chess_board import ChessBoard
from chess.pieces.piece import Piece


class Pawn(Piece):

    def get_possible_moves(self, board: ChessBoard) -> list[str]:
        directions = [(-1, 0)]
        possible_moves = [(self.x + dx, self.y + dy) for dx, dy in directions]
        return [board[nx][ny] for nx, ny in possible_moves if board.is_valid_position(nx, ny)]